---
description: Use NetExec safely with AI agents through scoped, mode-controlled MCP tools.
icon: microchip-ai
---

# NetExec MCP

**netexec-mcp** is an [MCP](https://modelcontextprotocol.io/) server that plugs NetExec directly into an AI agent: Claude Code, Cursor, opencode, or your own. The agent calls NetExec as one of its tools, inside the scope and mode you set.

Why use it instead of letting the agent type `nxc` commands in a shell:

* **Fewer tokens.** The agent sees 5 small meta-tools (about 1k tokens) and looks up the tool it needs, instead of parsing the `nxc` help or NetExec's source code to work out the right command. Small local models fit, and big ones cost less.
* **Scope enforced.** Every target is checked against `NXC_SCOPE`. Anything outside is refused.
* **Actions under control.** `NXC_MODE` decides what the agent may run, from suggesting commands only to full exploitation.
* **Structured results.** Shares, hashes and admin rights come back as JSON fields, not terminal text.
* **Audit log.** Every command, whether it ran, was previewed or was refused, is logged.

{% hint style="info" %}
netexec-mcp is a companion project by [@mpgn](https://x.com/mpgn_x64), installed separately from NetExec. It covers all ten protocols and NetExec's modules. Source: [github.com/mpgn/netexec-mcp](https://github.com/mpgn/netexec-mcp)
{% endhint %}

## Install

You need NetExec installed (see [Installation](/broken/pages/935cd9205d13a6828f6c00711a66e3ddfc291759)).

{% tabs %}
{% tab title="pipx" %}
```bash
pipx install netexec-mcp
```
{% endtab %}

{% tab title="uv" %}
```bash
uv tool install netexec-mcp
```
{% endtab %}
{% endtabs %}

On startup the server runs `nxc --version` and refuses to start if NetExec is not found. If `nxc` is not on your `PATH`, set `NXC_COMMAND` (e.g. `NXC_COMMAND="uv run --directory /opt/NetExec netexec"`).

## Configure

The server is configured with environment variables, passed by your agent (see below).

| Variable        | What it does                                                                     | Default                      |
| --------------- | -------------------------------------------------------------------------------- | ---------------------------- |
| `NXC_SCOPE`     | **Required.** Allowed targets: IPs, CIDRs, ranges or hostnames, comma-separated. | _none_                       |
| `NXC_MODE`      | `suggest`, `recon`, `loot` or `full` (see below).                                | `recon`                      |
| `NXC_AUDIT_LOG` | Path of the audit log file. Strongly recommended.                                | _none_                       |
| `NXC_COMMAND`   | How to launch NetExec, if it is not on your `PATH`.                              | `nxc` or `netexec` on `PATH` |
| `NXC_PROTOCOLS` | Restrict the tools to some protocols, e.g. `smb,ldap`.                           | all 10 protocols             |
| `NXC_PATH`      | NetExec home directory (config and workspace databases).                         | `~/.nxc`                     |

Each mode includes the previous one:

| Mode                | What the agent can run                                                        |
| ------------------- | ----------------------------------------------------------------------------- |
| `suggest`           | Nothing. Tools return the `nxc` command they would run, for you to run.       |
| `recon` _(default)_ | Read-only enumeration: hosts, shares, users, groups, policies...              |
| `loot`              | + credential collection: SAM, LSA, NTDS, GPP, Kerberoasting, AS-REP roasting. |
| `full`              | + everything else: command execution, uploads, spraying, coercion, exploits.  |

Scope and mode are read once at startup. The agent cannot change them; to raise them, edit the config and restart the server. More settings are listed in the [project README](https://github.com/mpgn/netexec-mcp#configuration-env-vars).

## Plug it into your agent

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add netexec \
  -e NXC_SCOPE=10.0.0.0/24 \
  -e NXC_MODE=recon \
  -e NXC_AUDIT_LOG=~/.netexec-mcp/audit.jsonl \
  -- netexec-mcp
```

Check with `claude mcp list`, or `/mcp` inside Claude Code.
{% endtab %}

{% tab title="Cursor" %}
Add to `~/.cursor/mcp.json` (all projects) or `.cursor/mcp.json` (one project):

```json
{
  "mcpServers": {
    "netexec": {
      "command": "netexec-mcp",
      "env": {
        "NXC_SCOPE": "10.0.0.0/24",
        "NXC_MODE": "recon",
        "NXC_AUDIT_LOG": "~/.netexec-mcp/audit.jsonl"
      }
    }
  }
}
```
{% endtab %}

{% tab title="opencode + Ollama (local)" %}
Add to `opencode.json`, next to your Ollama provider:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "netexec": {
      "type": "local",
      "command": ["netexec-mcp"],
      "environment": {
        "NXC_SCOPE": "10.0.0.0/24",
        "NXC_MODE": "recon",
        "NXC_AUDIT_LOG": "~/.netexec-mcp/audit.jsonl"
      }
    }
  }
}
```

Use a model with solid tool calling (Qwen3 14B is a good start) and at least 32k tokens of context.
{% endtab %}

{% tab title="Claude Desktop" %}
**Settings > Developer > Edit Config**, then add to `claude_desktop_config.json` and restart:

```json
{
  "mcpServers": {
    "netexec": {
      "command": "netexec-mcp",
      "env": {
        "NXC_SCOPE": "10.0.0.0/24",
        "NXC_MODE": "recon",
        "NXC_AUDIT_LOG": "~/.netexec-mcp/audit.jsonl"
      }
    }
  }
}
```

{% hint style="warning" %}
Desktop apps may not see your shell `PATH`. If the server does not start, use the absolute path of `netexec-mcp` (`which netexec-mcp`) and set `NXC_COMMAND` to the full path of `nxc`.
{% endhint %}
{% endtab %}

{% tab title="Your own agent (Python)" %}
Any MCP SDK works. With [Pydantic AI](https://github.com/pydantic/pydantic-ai) (`pip install pydantic-ai`):

```python
from fastmcp.client.transports import StdioTransport
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPToolset

netexec = MCPToolset(StdioTransport(
    command="netexec-mcp",
    args=[],
    env={"NXC_SCOPE": "10.0.0.0/24", "NXC_MODE": "recon"},
))

# Any Pydantic AI model works. "ollama:" reads OLLAMA_BASE_URL (e.g. http://localhost:11434/v1)
agent = Agent("ollama:qwen3:14b", toolsets=[netexec])

result = agent.run_sync("Which hosts in scope don't require SMB signing?")
print(result.output)
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Each action takes about two tool calls (find the tool, then run it). If your agent caps the number of steps per answer, raise it.
{% endhint %}

## Use it

Ask the agent to "run a NetExec health check": it should answer with your NetExec version. Then give it tasks:

* _"Which hosts in 10.0.0.0/24 don't require SMB signing?"_
* _"With robin / Summer2026!, which shares can I write to?"_
* _"Kerberoast the domain with these credentials."_ (needs `loot`)
* _"Dump LSA on 10.0.0.12 and see if anything lets me move further."_ (needs `loot`, `full` to run commands)

{% hint style="warning" %}
- **One `NXC_PATH` per engagement.** The agent can read credentials stored in NetExec's workspace database, including ones from a previous engagement.
- **Cloud models see your results.** Usernames, hashes and hostnames are sent to the model provider. Use a local model if the rules of engagement require it.
- **For authorized testing only.**
{% endhint %}

## Learn more

* [netexec-mcp on GitHub](https://github.com/mpgn/netexec-mcp): full configuration and tool list.
* [Building a MCP for NetExec](https://mpgn.fr/building-a-mcp-for-netexec/): the design in depth.
* [You're Building Your MCP Wrong](https://mpgn.fr/youre-building-your-mcp-wrong/): why dynamic mode exists, with benchmarks.
