# MCP prompts

## Use MCP prompts

MCP servers can expose MCP prompts, that are user-controlled templates that guide the LLM's interaction.

```bash
netexec mcp 192.168.1.10 --port 32685 --prompt "spell_check" --prompt-args '{"text": "Helo"}'
MCP         192.168.1.10   32685  192.168.1.10    [*] MCP server: name='Test server' title=None version='1.0.0' description=None website_url=None icons=None
MCP         192.168.1.10   32685  192.168.1.10    Hello
```