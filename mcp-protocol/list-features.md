# Features listing

## List the MCP features

MCP servers can expose MCP tools, resources, prompts or resource templates, with different parameters and URIs. They can be listed.

```bash
netexec mcp 192.168.1.10 --port 31974 -u "" -p "" --list
MCP         192.168.1.10   31974  192.168.1.10    [*] MCP server: name='Test server' title=None version='1.0.0' description=None website_url=None icons=None
MCP         192.168.1.10   31974  192.168.1.10    [+] :"hiddenPassword"
MCP         192.168.1.10   31974  192.168.1.10    [*] TOOLS
MCP         192.168.1.10   31974  192.168.1.10      • execute_server_command(command)
MCP         192.168.1.10   31974  192.168.1.10        Execute a safe command on the server.

Keyword arguments:
command -- the command to execute (one of 'date', 'whoami', 'uptime')
MCP         192.168.1.10   31974  192.168.1.10      • fetch_data(url)
MCP         192.168.1.10   31974  192.168.1.10        Fetch data from an external URL.

Keyword arguments:
url -- the url to fetch data from.
MCP         192.168.1.10   31974  192.168.1.10    [*] RESOURCES
MCP         192.168.1.10   31974  192.168.1.10      • get_logs - URI: 'resource://logs'
MCP         192.168.1.10   31974  192.168.1.10        Provide the MCP server logs.
MCP         192.168.1.10   31974  192.168.1.10    [*] RESOURCE TEMPLATES
MCP         192.168.1.10   31974  192.168.1.10      • get_value - URI: 'value://{item}'
MCP         192.168.1.10   31974  192.168.1.10        Fetch item value from the database.

Keyword arguments:
item -- the item to fetch the value for.
MCP         154.57.164.71   31974  154.57.164.71    [*] PROMPTS
```