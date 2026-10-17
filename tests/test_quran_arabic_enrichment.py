"""Offline regressions for missing canonical Arabic during Quran search.

Text markers are synthetic fixtures, not Quran quotations. Only the retrieval
backend, settings and language detector are replaced; search/shaping are real.
"""

from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest
from fastmcp.exceptions import ToolError

from quran_mcp.lib.goodmem import GoodMemMemory
from quran_mcp.lib.quran.search import search_quran
from quran_mcp.lib.search.common import SearchEnrichmentError
from quran_mcp.mcp.tools import _search_orchestration as orchestration
from quran_mcp.mcp.tools.quran.search import (
    SearchQuranRequestState,
    _SEARCH_QURAN_PLAN,
)


KEYS = ("2:153", "2:155")


def memory(key: str, *, arabic: bool) -> GoodMemMemory:
    return GoodMemMemory(
        content=f"{'ARABIC' if arabic else 'TRANSLATION'}_FIXTURE_{key}",
        metadata={
            "ayah_key": key,
            "surah": 2,
            "ayah": int(key.split(":")[1]),
            "edition_id": "ar-uthmani" if arabic else "en-pickthall",
            "lang": "ar" if arabic else "en",
            "url": f"https://quran.com/{key}" + ("" if arabic else "?translations=19"),
        },
        relevance_score=0.9 if key == KEYS[0] else 0.8,
        source_space_name="quran" if arabic else "translation",
    )


@pytest.fixture
def backend(monkeypatch):
    settings = SimpleNamespace(
        goodmem=SimpleNamespace(
            space=SimpleNamespace(quran="quran", translation="translation")
        )
    )
    monkeypatch.setattr("quran_mcp.lib.quran.search.get_settings", lambda: settings)
    monkeypatch.setattr(
        "quran_mcp.lib.quran.search.detect_query_language", lambda _: ("en", 1.0)
    )

    def make(arabic_keys, *, cached_keys=(), no_hits=False):
        translations = [] if no_hits else [memory(key, arabic=False) for key in KEYS]

        async def retrieve(*, space_names, filter_expr=None, **kwargs):
            if space_names == ["translation"]:
                return translations
            if space_names == ["quran"]:
                keys = arabic_keys if filter_expr else cached_keys
                return [memory(key, arabic=True) for key in keys]
            raise AssertionError(f"Unexpected retrieval space: {space_names}")

        return SimpleNamespace(
            default_reranker_id=None, search_memories=AsyncMock(side_effect=retrieve)
        )

    return make


@pytest.mark.parametrize(
    "arabic_keys,missing",
    [
        ([], KEYS),
        ([KEYS[0]], (KEYS[1],)),
        ([KEYS[0], KEYS[0]], (KEYS[1],)),
        (["2:156"], KEYS),
    ],
    ids=[
        "missing",
        "partial",
        "duplicate-does-not-cover-gap",
        "unrelated-does-not-cover-gap",
    ],
)
@pytest.mark.asyncio
async def test_missing_arabic_fails_explicitly(backend, arabic_keys, missing):
    with pytest.raises(SearchEnrichmentError) as caught:
        await search_quran(backend(arabic_keys), "patience")

    assert caught.value.code == "search_enrichment_failure"
    assert "quran_arabic_text" in str(caught.value)
    for key in missing:
        assert key in str(caught.value)


@pytest.mark.parametrize("translations", [None, "en-pickthall"])
@pytest.mark.asyncio
async def test_complete_arabic_preserves_results_and_attribution(backend, translations):
    # Deliberately return Arabic in reverse order: identity must be by verse key.
    result = await search_quran(
        backend(list(reversed(KEYS))), "patience", translations=translations
    )

    assert [row.ayah_key for row in result.results] == list(KEYS)
    assert [row.relevance_score for row in result.results] == [0.9, 0.8]
    assert result.unresolved_editions == []
    assert result.translation_gaps == []
    for row in result.results:
        assert row.text == f"ARABIC_FIXTURE_{row.ayah_key}"
        assert (row.surah, row.ayah) == (2, int(row.ayah_key.split(":")[1]))
        assert row.url == f"https://quran.com/{row.ayah_key}?translations=19"
        assert row.source_space == "translation"
        if translations is None:
            assert row.translations == []
        else:
            assert len(row.translations) == 1
            translation = row.translations[0]
            assert translation.text == f"TRANSLATION_FIXTURE_{row.ayah_key}"
            assert translation.edition.id == "en-pickthall"
            assert translation.edition.author == "Muhammad Marmaduke Pickthall"
            assert translation.edition.lang == "en"
            assert (
                translation.url == f"https://quran.com/{row.ayah_key}?translations=19"
            )


@pytest.mark.asyncio
async def test_cached_arabic_does_not_require_backend_enrichment(backend):
    client = backend([], cached_keys=KEYS)
    result = await search_quran(client, "patience")
    assert [row.text for row in result.results] == [
        f"ARABIC_FIXTURE_{key}" for key in KEYS
    ]
    # Wide retrieval only; the existing cached edition covers both Arabic keys.
    assert client.search_memories.await_count == 2


@pytest.mark.asyncio
async def test_no_search_hits_remains_successful_empty_result(backend):
    result = await search_quran(backend([], no_hits=True), "patience")
    assert result.results == []
    assert result.translation_gaps == []


@pytest.mark.parametrize("arabic_keys", [[], [KEYS[0]]], ids=["missing", "partial"])
@pytest.mark.asyncio
async def test_search_boundary_uses_existing_enrichment_error(
    backend, monkeypatch, arabic_keys
):
    client = backend(arabic_keys)
    monkeypatch.setattr(
        orchestration, "resolve_search_runtime_context", lambda _: (None, client)
    )
    with pytest.raises(ToolError, match=r"^\[search_enrichment_failure\] "):
        await orchestration.execute_search_tool(
            ctx=None,
            continuation=None,
            explicit_state={},
            initial_state=SearchQuranRequestState(query="patience"),
            plan=_SEARCH_QURAN_PLAN,
        )


@pytest.mark.parametrize("cached", [False, True], ids=["lookup", "cached"])
@pytest.mark.parametrize("invalid", ["blank", "wrong-edition"])
@pytest.mark.asyncio
async def test_invalid_canonical_rows_cannot_satisfy_coverage(backend, cached, invalid):
    client = backend(KEYS, cached_keys=KEYS if cached else ())
    retrieve = client.search_memories.side_effect

    async def invalid_rows(**kwargs):
        rows = await retrieve(**kwargs)
        if kwargs["space_names"] == ["quran"]:
            for row in rows:
                if invalid == "blank":
                    row.content = " \t\n"
                else:
                    row.metadata["edition_id"] = "ar-simple"
        return rows

    client.search_memories.side_effect = invalid_rows
    with pytest.raises(SearchEnrichmentError, match="quran_arabic_text"):
        await search_quran(client, "SYNTHETIC QUERY")


@pytest.mark.asyncio
async def test_existing_fetch_helper_recovers_only_missing_key(backend):
    # Distinct duplicate records fill the initial two-row budget; B is available.
    client = backend([KEYS[0], KEYS[0]])
    retrieve = client.search_memories.side_effect

    async def with_recovery(**kwargs):
        expression = kwargs.get("filter_expr") or ""
        if kwargs["space_names"] == ["quran"] and "edition_type" in expression:
            assert "quran" in expression and "ar-uthmani" in expression
            assert "155" in expression and "153" not in expression
            assert kwargs["limit"] == 12
            assert kwargs["query"] == "content"
            row = memory(KEYS[1], arabic=True)
            row.metadata["edition_type"] = "quran"
            return [row]
        return await retrieve(**kwargs)

    client.search_memories.side_effect = with_recovery
    result = await search_quran(client, "SYNTHETIC QUERY", translations="en-pickthall")
    assert [r.ayah_key for r in result.results] == list(KEYS)
    assert [r.text for r in result.results] == [f"ARABIC_FIXTURE_{key}" for key in KEYS]
    assert [r.relevance_score for r in result.results] == [0.9, 0.8]
    assert all(r.translations[0].edition.id == "en-pickthall" for r in result.results)
    assert (
        client.search_memories.await_count == 5
    )  # wide x2, initial, recovery, translation


@pytest.mark.asyncio
async def test_blank_cached_arabic_can_be_recovered(backend):
    client = backend(KEYS, cached_keys=KEYS)
    retrieve = client.search_memories.side_effect

    async def blank_cache(**kwargs):
        rows = await retrieve(**kwargs)
        if kwargs["space_names"] == ["quran"] and not kwargs.get("filter_expr"):
            for row in rows:
                row.content = ""
        return rows

    client.search_memories.side_effect = blank_cache
    result = await search_quran(client, "SYNTHETIC QUERY")
    assert all(r.text == f"ARABIC_FIXTURE_{r.ayah_key}" for r in result.results)
    assert client.search_memories.await_count == 3


@pytest.mark.parametrize(
    "failure", [TimeoutError("SYNTHETIC TIMEOUT"), RuntimeError("SYNTHETIC FAILURE")]
)
@pytest.mark.asyncio
async def test_recovery_backend_error_uses_enrichment_contract(backend, failure):
    client = backend([])
    retrieve = client.search_memories.side_effect

    async def failing_recovery(**kwargs):
        if "edition_type" in (kwargs.get("filter_expr") or ""):
            raise failure
        return await retrieve(**kwargs)

    client.search_memories.side_effect = failing_recovery
    with pytest.raises(SearchEnrichmentError, match="SYNTHETIC") as caught:
        await search_quran(client, "SYNTHETIC QUERY")
    assert caught.value.code == "search_enrichment_failure"


@pytest.mark.asyncio
async def test_complete_lookup_keeps_legacy_filters_and_call_count(backend):
    client = backend(KEYS)
    await search_quran(client, "SYNTHETIC QUERY")
    assert client.search_memories.await_count == 3
    lookup = client.search_memories.call_args_list[-1].kwargs
    assert lookup["limit"] == 2
    assert "ayah_key" in lookup["filter_expr"]
    assert "edition_type" not in lookup["filter_expr"]


@pytest.mark.asyncio
async def test_arabic_only_cached_search_remains_two_wide_calls(backend, monkeypatch):
    monkeypatch.setattr(
        "quran_mcp.lib.quran.search.detect_query_language", lambda _: ("ar", 1.0)
    )
    client = backend([], cached_keys=KEYS)
    retrieve = client.search_memories.side_effect

    async def arabic_only(**kwargs):
        if kwargs["space_names"] == ["translation"]:
            return []
        return await retrieve(**kwargs)

    client.search_memories.side_effect = arabic_only
    result = await search_quran(client, "SYNTHETIC QUERY")
    assert [r.ayah_key for r in result.results] == list(KEYS)
    assert all(r.source_space == "quran" for r in result.results)
    assert client.search_memories.await_count == 2


@pytest.mark.asyncio
async def test_initial_arabic_backend_failure_keeps_existing_contract(backend):
    client = backend([])
    retrieve = client.search_memories.side_effect

    async def fail_lookup(**kwargs):
        if kwargs["space_names"] == ["quran"] and kwargs.get("filter_expr"):
            raise TimeoutError("SYNTHETIC INITIAL LOOKUP TIMEOUT")
        return await retrieve(**kwargs)

    client.search_memories.side_effect = fail_lookup
    with pytest.raises(SearchEnrichmentError, match="SYNTHETIC INITIAL"):
        await search_quran(client, "SYNTHETIC QUERY")
    assert client.search_memories.await_count == 3


@pytest.mark.parametrize(
    "primary_text,cached_text,primary_arabic,expected",
    [
        (
            "SYNTHETIC_PRIMARY_ARABIC",
            "SYNTHETIC_PRIMARY_ARABIC",
            True,
            "SYNTHETIC_PRIMARY_ARABIC",
        ),
        (" \t\n", "SYNTHETIC_CACHED_ARABIC", True, "SYNTHETIC_CACHED_ARABIC"),
        (
            "SYNTHETIC_PRIMARY_ARABIC",
            "SYNTHETIC_DIFFERENT_CACHED_ARABIC",
            True,
            "SYNTHETIC_PRIMARY_ARABIC",
        ),
        (
            "SYNTHETIC_PRIMARY_TRANSLATION",
            "SYNTHETIC_CACHED_ARABIC",
            False,
            "SYNTHETIC_CACHED_ARABIC",
        ),
    ],
    ids=[
        "valid-primary",
        "blank-primary",
        "differing-canonical-records",
        "translation-primary",
    ],
)
@pytest.mark.asyncio
async def test_cached_arabic_preserves_valid_primary(
    backend, primary_text, cached_text, primary_arabic, expected
):
    client = backend([])
    primary = memory(KEYS[0], arabic=primary_arabic)
    primary.content, primary.relevance_score = primary_text, 0.95
    cached = memory(KEYS[0], arabic=True)
    cached.content, cached.relevance_score = cached_text, 0.5

    async def retrieve(**kwargs):
        assert not kwargs.get("filter_expr"), (
            "Valid cache must avoid enrichment requests"
        )
        if kwargs["space_names"] == ["quran"]:
            # Arrival order differs from ranking: cached canonical record is first.
            return [cached, primary] if primary_arabic else [cached]
        return [] if primary_arabic else [primary]

    client.search_memories.side_effect = retrieve
    result = await search_quran(client, "SYNTHETIC QUERY")
    assert len(result.results) == 1
    row = result.results[0]
    assert row.text == expected
    assert (row.ayah_key, row.surah, row.ayah) == (KEYS[0], 2, 153)
    assert row.relevance_score == 0.95
    assert row.url == primary.metadata["url"]
    assert client.search_memories.await_count == 2
