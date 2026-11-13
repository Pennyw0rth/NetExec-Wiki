# Authentication

By default, MCP does not require credentials. If yes, you can authenticate on the remote target using a local user via HTTP Basic Auth.

* When authentication fail => `COLOR RED`
* When authentication success => `COLOR GREEN`

## Anonymous Login

```bash
nxc mcp 192.168.1.10 --list
```

## Testing Credentials

```bash
nxc mcp 192.168.1.10 -u Username -p Password
```

## Specify Port

```bash
nxc mcp 192.168.1.10 --port 35000 -u Username -p Password
```