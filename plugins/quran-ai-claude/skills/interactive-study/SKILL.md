---
name: interactive-study
description: Open and continue Quran study through the interactive reader and embedded passage links, including personal discovery informed by past conversations, unexpected powerful verses for reflection, and open inquiry into the Quran's claims about God. Also use for reader navigation, selections, submitted annotations and multiple passage attachments, follow-up questions, and a bare quran.ai invocation.
---

# Interactive Quran study

Use `open_quran_reader` when the user wants to open the Quran for interactive reading or study. The reader supports ayah, word, and phrase selection.

## Read, select, ask, discover

The conversation and visual book form a continuing loop. For a personal Quran
discovery journey informed by past conversations, an unexpected powerful verse
to linger over, or an open inquiry into the Quran's claims about God, use the
[Onboarding skill](../onboarding/SKILL.md) to choose the approach, then carry it
out here. Recognize the purpose in the user's wording, including paraphrases.
These requests require both an appropriately opened reader and a substantive
grounded response in the same turn.

- Choose a fitting opening passage and fetch the canonical text, translation,
  and any interpretation needed under the grounding rules below. Open it with
  `open_quran_reader` at the chosen surah and ayah before the substantive response.
  Keep the book beside the conversation where the host supports it. Leave
  `render_mode` omitted unless an explicit preference or known host requirement
  calls for an override. If a reader is already open, use its supported current
  context and navigation instead of creating another merely for the introduction.
- Write an explanation connected to what the user can read there. Embed
  working Markdown deep links **inside the explanatory prose** wherever you
  introduce a passage, point to a phrase, or suggest a comparison. Each of the
  three starters should demonstrate navigation to the opening passage and
  another meaningful destination. A detached list of references or a promise
  that links will appear later does not deliver this experience. Follow
  **Reader links in answers** below for verified destinations and coordinates.
- Invite one concrete first interaction: identify a particular phrase in the
  opening passage, link to it when exact resolution is available, and suggest
  a useful question about it. Opening the link activates that passage; the
  user can ask about it or select a different phrase. Briefly explain the
  paperclip when retaining a fixed passage for a prompt would be useful;
  Quick send in Study tools sends the active selection with the question.
  Use the submitted passage or current reader context to identify the target.
  Leave the user free to choose a different phrase or direction.
- Offer a few specific ways to continue, tied to the passages just discussed.
  On the next turn, answer the user's actual question and selection using the
  scope rules below. Weave useful linked passages or phrases into that answer
  so the user can return to reading, select, and ask again. Carry the loop
  through later study exchanges without repeating a controls tour, forcing
  extra links into an unrelated answer, or reopening the reader after each reply.

Respect the user's request for a brief, text-only, or otherwise different
response. If the selected plugin's opener or verified links are unavailable,
state that limitation briefly and continue the supported part; do not substitute
another registration, invent links, or claim the interactive loop was completed.

## Opening and navigation

- When a submitted message explicitly invokes the quran.ai plugin or this skill without an accompanying question, location, or other request, call `open_quran_reader({})` exactly once. An accompanying request takes precedence: guided study starters follow the reader-and-response loop above, a requested location determines navigation, and an ordinary question determines the answer. Ordinary discussion about quran.ai or this skill is not an invocation.
- For an ordinary opening without a requested location, omit location, context, selection, and resume arguments. The server opens a fresh reader context at the first Lastmark in the user’s order, or Al-Anbiya 21:1 when none is saved. Browsing does not move Lastmarks. Opening activates that saved ayah; it does not restore a previous session’s selection. Exact session recovery remains the separate `resume=true` workflow supplied by current reader context.
- When a location is requested, pass one location form: `page`, `surah` with optional `ayah`, or `juz`. Do not combine mutually exclusive location fields.
- Opening the reader is navigation, not canonical evidence. It may happen before `fetch_grounding_rules`, but do not quote or interpret Quran text from the rendered widget alone.
- Do not narrate that the reader is opening. A bare opening or navigation request ends with the reader. A guided introduction or an accompanying study question still needs its substantive response after rendering; omit filler, not the requested answer.

## Answering from the reader

- Read the whole submitted request before choosing what to discuss: the user's prompt, every passage attachment, each item's annotation, and any relevant current reader selection. A general request such as "explain the meaning in depth" applies to all submitted selections unless the user narrows the scope. Do not silently choose just the item matching the active ayah or the most recent reader position. Before finishing, check that every in-scope item was addressed, or explicitly say what remains.
- Follow explicit directions to add, compare, narrow, or replace passages. "Explain 6:2" asks about 6:2 even if Quick send supplies a different selection; "compare these with 6:2" keeps the submitted items and adds 6:2. A reference mentioned as background does not discard the other attachments. Interpret each annotation together with its own selected text and the accompanying prompt. Its text may be a label, note, question, or request; a reference inside one annotation applies to that item unless the user makes it global.
- Preserve each item's exact selected words and phrase boundaries. Complete ayahs, nearby words, and retrieved passages can supply supporting context or clearly identified comparisons; they do not become selected targets or replace other submitted items.
- A visible highlight or reading position is not proof of an attachment. Use attachments actually submitted with the question; do not restore a removed passage using earlier or saved context. Quick send supplies its own selected passage. Use available current selection context for an otherwise unresolved "this", or when the user asks to include it, without requiring a separate Attach action. An absent live selection does not invalidate submitted attachments.
- If a requested reader passage is still unidentified from the prompt and submitted items, and current context for the relevant reader is unavailable, call `get_interactive_study_context` exactly once to fill that missing reference. This can supply one missing part of a comparison without replacing its other items. Available context that says no selection is not unavailable; do not replace it with older saved state. If the reference remains unidentified, say the selection is unavailable and ask which passage they mean instead of guessing.
- Before the first canonical Quran data call, read and follow the `grounding-rules` skill if available, then pass its acknowledgment as `grounding_nonce`. If the skill is unavailable, call `fetch_grounding_rules` and use its returned nonce. Do not fetch rules already read. Reuse relevant canonical evidence already in the conversation and fetch only what is missing.
- Treat search excerpts as discovery leads; fetch the full Quran, translation, morphology, or tafsir passage before answering from it.
- Follow the recovery arguments in current widget context; use `open_quran_reader` even when an older reader names `interactive_study` as its resume tool. When the user asks to resume, make one recovery attempt with `open_quran_reader` using the requested handoff. If recovery is unavailable, follow the tool's documented fresh-opening fallback only when an explicit canonical location is known; do not guess missing state or claim it was restored. A bare successful resume ends with the app; if they also ask a study question, answer it using the restored context and grounding rules.

For help with selection, prompt attachments, contextual meaning, or settings, use the
[Onboarding skill](../onboarding/SKILL.md)'s relevant guidance without restarting
setup. Contextual meaning uses a fixed Word meanings or Ayah translation mode;
its pull handle and Collapse lane setting control visibility.

## Reader links in answers

Make the first useful occurrence of a discussed Quran reference a concise Markdown link **within the explanatory prose**, including related ayahs in other surahs. Use labels such as `Al-Imran 3:38` or `Maryam 19:3–11`. Link a surah introduction to its first ayah or the particular opening passage being discussed. Use separate links for different surahs or disjoint passages; avoid linking every repetition or the grounding footer.

Choose the destination from the current client:

- **Recognized ChatGPT:** use the verified Interactive Study destination supplied by current server or session guidance. Use `chatgpt_reader_url` in ChatGPT browsers or when ChatGPT is established but its native host is unknown. Use `desktop_reader_url` only with explicit native ChatGPT host evidence. `ClientHint.platform=desktop` is a device class, not native-host evidence.
- **Every other client**, including Claude, Codex, and unidentified hosts: use `https://quran.com/S:A` for one ayah or `https://quran.com/S:A-B` for a continuous same-surah span. For a phrase, link its containing ayah or ayah span. Quran.com links do not select individual words. Do not attach reader targets or ChatGPT parameters to them.

If the destination or exact phrase scope needs resolution, call `resolve_reader_link` with the cited `ayahs` and optional exact Arabic `phrase` copied from canonical context. Use its `reader_url` unchanged; this selects the destination for the current client. The separate `quran_com_url` is always available. Null ChatGPT URL fields mean the current client is outside ChatGPT or this deployment has no configured ChatGPT destination; use Quran.com. Show one link per reference, without explaining URL selection or host limitations unless asked.

For ChatGPT, the verified destination formats are:

```text
https://chatgpt.com/plugins/<verified-plugin-id>/app/interactive_study?path=%2Fayah%2F<surah>%3A<ayah>
codex://plugins/<verified-plugin-id>/app/interactive_study?path=%2Fayah%2F<surah>%3A<ayah>
```

The `codex://` URL scheme here is for native ChatGPT navigation; it does not make a Codex client a ChatGPT client. Never infer a plugin ID from the MCP hostname, copy an ID from an unrelated registration, or use a development ID for the published app. If ChatGPT has no verified destination, use Quran.com.

For a continuous range in ChatGPT, include the end ayah: `?path=%2Fayah%2F3%3A37-41` for `Al-Imran 3:37–41`. The reader opens at the first ayah and activates the full passage, replacing the previous active selection. Copy, Locate, Park, and current reader context then use that passage. A separately retained prompt attachment stays unchanged.

For a specific phrase in ChatGPT, use exact QCF V2 printed-word endpoints already supplied by the current reader selection or a previous `resolve_reader_link` result. For that same contiguous span within one surah and at most three mushaf pages, build `/passage/{start_ayah}:{start_word}-{end_ayah}:{end_word}` and percent-encode it as the verified destination's `path` parameter; no new resolution call is needed. Keep disjoint spans as separate links. Do not treat morphology or concordance positions as reader coordinates, count words yourself, or infer endpoints for a smaller phrase inside the supplied span.

If those exact reader endpoints are unavailable, call `resolve_reader_link` with the containing `ayahs` (for example, `3:37-38`) and the exact canonical `phrase`. Prefer a related ayah or exact phrase over a broader passage when it directly supports the point. A ChatGPT phrase link opens and highlights the verified words, including spans crossing an ayah or page boundary. A Quran.com phrase link opens their containing ayah span. If the phrase is ambiguous, narrow the ayah scope or include more of the exact quotation; if it cannot be resolved, retain a whole-ayah link. A ChatGPT link activates the passage and supplies current reader context; a separate Attach press or composer chip is not required to ask about it. The paperclip retains a fixed copy for a prompt; sending from the reader carries the current selection with the question. Keep the existing tool-based citation line unchanged.

For ChatGPT links, preserve `reader_target` exactly when the reader-opening result, the question, or current reader context supplies it. The reader-opening result's `reader_target` addresses the reader it opens, so use it for links in that same answer. For a constructed link, append `?reader=<reader_target>` to the app-relative path before percent-encoding the entire path into the URL. When calling `resolve_reader_link`, pass the exact value and use its returned URL unchanged. Never substitute a context ID, instance ID, or resume token. Without a supplied target, use the configured global reader destination. The reader can forward a targeted destination to the original reader when available; the host controls which window or tab opens. Do not promise tab reuse or transfer of an originating conversation.

When supported host metadata/tools or the user supplies the originating conversation's full URL, pass it unchanged as `originating_chat_url` to `resolve_reader_link`. Preserve every part, including a Codex `hostId`. This optional return destination is separate from `reader_target`. Never guess it from a reader token, working directory, or recently listed conversation, and never replace it with the global relay's conversation when a link opens elsewhere. If unavailable, omit it without asking the user to find it. Use the returned link unchanged; the relay offers the return link and can ask its own conversation's assistant to present it. Neither passage delivery nor a message acknowledgement proves the original conversation was focused.

Keep navigation and scholarly attribution separate: the Quran reference opens the passage, while the commentator's name or a short source label opens the exact cited tafsir passage. Preserve verified passage-specific source links, whether on quran.com, tafsir.app, turath.io, or another source. An author page, book homepage, or whole volume is not a direct citation. Never invent source URLs. A navigation link is not canonical evidence for a scholarly claim; use the Quran tools to verify text and claims.

## Word and phrase exploration

Use the selections established under **Answering from the reader**, including all in-scope submitted annotations. Apply the requested depth to each word or phrase; do not return to the live widget to choose a single replacement. Whole ayahs and nearby words provide context or identified comparisons, not additional selections. For words and phrases especially:

Start with the ayah key, then display the complete Arabic ayah **with tashkil** as a large Markdown heading. If the selection is a word or phrase rather than the full ayah, display it separately as another large heading.

For the selection, provide:

1. Direct, common translations.

2. The strongest meaning in context.

3. The full plausible semantic range of the word, including possible meanings beyond those discussed in classical tafsir, especially in light of modern knowledge such as astronomy. Separate the primary meaning from secondary possibilities, and distinguish established linguistic evidence from an exploratory connection. For example, the connection between f-l-k and an old Arabic word for a spindle whorl invites exploration of more than an orbit: something rotating around an axis. Check the lexical basis and explain what it supports. Morphology identifies the root and form; support an additional lexical sense with retrieved vocabulary commentary or linguistic tafsir selected using the shared guide or an available catalogue. Use `fetch_tafsir` to retrieve the relevant commentary. Explain separately any further inference from fetched occurrences or connection to modern knowledge. Do not limit exploration to connections discussed in the retrieved commentary, or assume it covers every plausible possibility.

4. Root, morphology, and visible word components, explained in plain language.

5. A familiar lexical bridge, when helpful. Use the user’s preferred language or, better still, an Arabic dialect they are familiar with, such as Masri, Khaliji, or Shami. Use what you already know about their language preferences; do not assume a dialect from the language they write in. When possible, connect the selected word or root to one short, natural modern sentence using a familiar form from the same root with a related meaning.

   Use this only as a lexical bridge. Never rewrite or paraphrase a Quranic ayah into an Arabic dialect—that is 3ayb. Briefly note if the modern dialect meaning is narrower than or has shifted from the Quranic usage.

   Another useful bridge is a different usage in the Quran, such as explaining “ألقت” in “وألقت ما فيها وتخلت” through “قال ألقها يا موسى”. Fetch the relevant occurrences and explain the connection.

6. Relevant translation differences and tafsir.

7. What it probably does not mean.

8. Comparisons with nearby or similar words, when useful.

9. Quran-wide root, lemma, and occurrence data, when useful.

Choose commentary using [Tafsir source guide](../grounding-rules/SKILL.md#tafsir-source-guide) and its source-selection guidance. For word study, distinguish a vocabulary gloss, competing grammatical parsings, a rhetorical choice, and the word's role in the surrounding passage. The guide includes sources for each, as well as broader commentators whose linguistic discussion may help. Questions about the wording can also require historical, theological, legal, or practical perspectives. Use the retrieved passage to judge whether a source addresses the question; attribute interpretations and preserve genuine disagreements.

Use Quran, translation, tafsir, morphology, paradigm, and concordance tools as needed. Never interpret from translation alone or rely on memory alone for morphology. Morphology and concordance tools provide supporting evidence; their annotations are not absolute or exhaustive. Reuse canonical material already present and fetch only what is missing.

Render all Arabic words and phrases as large Markdown headings for accessibility. Put transliteration and clear English immediately beneath them.
