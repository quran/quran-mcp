# Plugins

quran.ai is available in Claude and ChatGPT. Both connect to the same hosted
MCP server at `https://mcp.quran.ai` and use the same three skills: grounding
rules, interactive study, and onboarding.

| Folder | Covers | Purpose |
|--------|--------|---------|
| [`quran-ai/`](quran-ai/) | quran.ai plugin | The one plugin folder. Anthropic's plugin directory installs it as-is: Claude reads `.claude-plugin/plugin.json` and `.mcp.json`. The ChatGPT manifest (`plugin.json`, `mcp.json`), artwork and skill metadata sit beside them; ChatGPT packages are built from the same folder. |

## Get quran.ai

- **Claude:** add the [quran.ai connector](https://claude.ai/directory/connectors/quran-ai)
  from Claude's directory. The plugin, which adds the skills, is listed there
  once it is published.
- **ChatGPT:** add the
  [quran.ai app](https://chatgpt.com/plugins/plugin_asdk_app_69aca72176f4819197186bc55da38fe0).
- **Any other MCP client:** connect to `https://mcp.quran.ai`.
