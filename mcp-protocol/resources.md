# MCP resource

## Use MCP resources

MCP servers can expose MCP resources, generally to read data from local sources. Resources use the default `resource://` URI.

```bash
netexec mcp 192.168.1.10 --port 32685 --resource "resource://logs"
MCP         192.168.1.10   32685  192.168.1.10    [*] MCP server: name='Test server' title=None version='1.0.0' description=None website_url=None icons=None
MCP         192.168.1.10   32685  192.168.1.10    2025-05-12 14:56:59.941202: MCP server starting...
2025-05-12 14:57:00.183027: Startup complete.
```

## Use MCP resource templates

MCP servers can expose MCP resource templates, generally to read data from various sources. Resource templates use custom URIs with controllable parameters.

```bash
netexec mcp 192.168.1.10 --port 32685 --resource "value://test"
MCP         192.168.1.10   32685  192.168.1.10    [*] MCP server: name='Test server' title=None version='1.0.0' description=None website_url=None icons=None
MCP         192.168.1.10   32685  192.168.1.10    Test=1
```