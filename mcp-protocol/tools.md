# MCP tool

## Use MCP tools

MCP servers can expose MCP tools to perform operations.

```bash
netexec mcp 192.168.1.10 --port 32685 --tool execute_server_command --tool-args '{"command": "date"}'
MCP         192.168.1.10   32685  192.168.1.10    [*] MCP server: name='Test server' title=None version='1.0.0' description=None website_url=None icons=None
MCP         192.168.1.10   32685  192.168.1.10    Sun Oct  4 16:05:42 UTC 2026
```