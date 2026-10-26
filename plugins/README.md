# Plugins

quran.ai is available in Claude and ChatGPT. Both versions connect to the same
hosted MCP server at `https://mcp.quran.ai` and use the same three skills:
grounding rules, interactive study, and onboarding.

| Folder | Covers | Purpose |
|--------|--------|---------|
| [`quran-ai-claude/`](quran-ai-claude/) | Claude plugin bundle | The source Anthropic's plugin directory installs: manifest, listing icon, connector configuration, listing README, license, and skills. |

The `-claude` suffix marks the Claude packaging. The ChatGPT version is built
from a private package and distributed through OpenAI's app directory, so it
isn't published in the public repository. Its skills are byte-identical to the
ones in `quran-ai-claude/skills/`.

## Get quran.ai

- **Claude:** add the [quran.ai connector](https://claude.ai/directory/connectors/quran-ai)
  from Claude's directory. The plugin bundle, which adds the skills, is listed
  there once it is published.
- **ChatGPT:** add the
  [quran.ai app](https://chatgpt.com/plugins/plugin_asdk_app_69aca72176f4819197186bc55da38fe0).
- **Any other MCP client:** connect to `https://mcp.quran.ai`.
