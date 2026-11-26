# quran.ai

Study the Quran with Claude. quran.ai pairs an interactive Quran reader with
tools that fetch verified Quran text, translations, authentic tafsir
(commentary), and word-level morphology from [quran.com](https://quran.com), so
Claude answers from canonical sources instead of from memory, names those
sources, and links each cited ayah.

## What's included

- **quran.ai connector**: the remote MCP server at `https://mcp.quran.ai`, the
  same server as the quran.ai connector in Claude's directory. It provides
  Quran, translation, and tafsir search and retrieval, word morphology and
  concordance, edition listings, and the interactive reader.
- **Grounding rules skill**: tells Claude how to quote, cite, and attribute
  Quran text, translations, and tafsir faithfully, and how to link cited ayahs
  and tafsir passages. It also keeps scholarly interpretation separate from
  Claude's own reflection.
- **Interactive study skill**: opens the reader, follows your selections in it,
  and keeps the study loop going: read, select, ask, discover.
- **Onboarding skill**: three ways to begin (a personal discovery journey, an
  unexpected verse for reflection, or an open inquiry into what the Quran
  claims about God), plus help with the reader's controls and settings.

## Use it

After adding the plugin, connect the quran.ai connector from the plugin's
**Connectors** tab. No account is needed to study. Signing in with a Quran
Foundation account is optional and keeps your notes, saved places, and reader
settings across conversations. Then ask Claude things like:

- "Open the Quran reader at Surah Al-Kahf."
- "Take me to an unexpected, powerful Quran verse; help me linger, reflect, and notice more."
- "What do the classical tafsirs say about 2:255?"
- "Find where the Quran talks about patience, with sources."

Answers link each cited ayah to quran.com.

## Data

The plugin's skills are instructions only. They run no code and send nothing
on their own. Every request goes through the quran.ai connector to the hosted
service at `https://mcp.quran.ai`. The service uses what it receives to answer
you, to keep itself running, and to see how much it is used:

- The service receives the tool inputs Claude sends, such as verse references,
  search terms, note text, and your reader selections. Its logs record each
  tool request with its inputs, so that it can run and its faults can be found
  and fixed. A separate diagnostic record keeps each tool request with the
  full result it returned for at most 12 hours, to find faults and to draw
  the samples below. The operator reads hourly summaries of the logs and of
  that record: how many requests each tool receives and from which AI app,
  how often the reader is opened, and a few sampled search queries, tafsir
  editions, passages and word lookups with personal material removed. The
  summaries, samples included, are kept until the operator deletes them.
- To answer a search, the service sends your search text to Google's Gemini
  API to match passages by meaning. To rank word-concordance results, it may
  send the Arabic word and matching verse text to Voyage AI.
- The reader saves your page, selection, and options so it can return you to
  your place. The service deletes that saved place 180 days after its last
  change.
- If you sign in with a Quran Foundation account, the service keeps your
  notes, saved places, and settings for you under your account, with the
  email address, name, and other profile details Quran Foundation provides,
  until they are deleted.
- When you use the reader's listening feature, your browser processes your
  voice on your own device. Your audio is never sent to the service. The
  listening page sends your open reader only the matched word positions, the
  page and selection to show, and memorization-test results. The service
  holds the latest of these in memory until your reader collects them, for
  at most 30 minutes after listening stops.
- The service stores feedback or a reader bug report only when you ask Claude
  to send feedback or press Send in the reader.

The reader loads Quran page fonts and recitation audio from Quran Foundation's
servers. The service shows no advertising, builds no profiles of you from your
content, and doesn't sell personal information. Full details and retention
periods are in the [privacy policy](https://mcp.quran.ai/privacy), and use of the service is
governed by the [terms of service](https://mcp.quran.ai/terms). Send privacy
questions or deletion requests to nour@quran.com. For help, see the
[documentation](https://mcp.quran.ai/documentation) and
[support](https://mcp.quran.ai/support).

## Sources and license

Quran text, translations, and tafsir come from Quran Foundation projects,
including quran.com. The plugin doesn't claim ownership of that content.
The plugin is licensed under the Quran Foundation General Public License
(QFGPL) 1.0; see [LICENSE.md](LICENSE.md).
