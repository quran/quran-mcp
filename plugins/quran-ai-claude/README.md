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
  Quran text, translations, and tafsir faithfully. It also keeps scholarly
  interpretation separate from Claude's own reflection.
- **Interactive study skill**: opens the reader, follows your selections in it,
  and keeps the study loop going: read, select, ask, discover.
- **Onboarding skill**: three ways to begin (a personal discovery journey, an
  unexpected verse for reflection, or an open inquiry into what the Quran
  claims about God), plus help with the reader's controls and settings.

## Use it

After adding the plugin, connect the quran.ai connector from the plugin's
**Connectors** tab. No account is needed. Then ask Claude things like:

- "Open the Quran reader at Surah Al-Kahf."
- "Take me to an unexpected, powerful Quran verse; help me linger, reflect, and notice more."
- "What do the classical tafsirs say about 2:255?"
- "Find where the Quran talks about patience, with sources."

Answers link each cited ayah to quran.com.

## Data

The plugin's skills are instructions only. They run no code and send nothing
on their own. Every request goes through the quran.ai connector to the hosted
service at `https://mcp.quran.ai`, which:

- receives the tool inputs Claude sends, such as verse references, search
  terms, and your reader selections, and logs tool requests with their inputs
  and results for operation and improvement;
- sends search text to Google's Gemini API to match passages by meaning, and
  may send Arabic words and matching verse text to Voyage AI to rank
  concordance results;
- saves your reader position, selection, and options for 180 days after their
  last change, linked to a one-way hash of the conversation address Claude
  gives the reader;
- stores feedback only when you ask Claude to send it.

It doesn't ask for your name or email address and doesn't build advertising
profiles. The reader loads Quran page fonts from Quran Foundation's font server.
Full details and retention periods are in the
[privacy policy](https://mcp.quran.ai/privacy). Send privacy questions or
deletion requests to support@quran.ai. For help, see
[support](https://mcp.quran.ai/support).

## Sources and license

Quran text, translations, and tafsir come from Quran Foundation projects,
including quran.com. The plugin doesn't claim ownership of that content.
The plugin is licensed under the Quran Foundation General Public License
(QFGPL) 1.0; see [LICENSE.md](LICENSE.md).
