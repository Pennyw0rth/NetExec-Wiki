# `ssh_socks` Module

The `ssh_socks` module provides a **SOCKS5 proxy** over an existing SSH connection.  
It allows tunneling network traffic from your attacking host through the compromised SSH target.

---

## 📖 Description

- **Module name:** `ssh_socks`  
- **Purpose:** Expose a SOCKS5 proxy bound locally (default: `127.0.0.1:1080`).  
- **Protocols:** `ssh`  
- **OpSec safe:** ✅ Yes — works via existing SSH transport.  
- **Multiple hosts:** ❌ No — one SSH session at a time.  

---

## ⚙️ Options

| Option   | Default  | Description                                                                 |
|----------|----------|-----------------------------------------------------------------------------|
| `PORT`   | `1080`   | Local port to bind the SOCKS5 proxy.                                        |
| `KEX`    | *(none)* | Comma-separated list of key exchange algorithms to force (for legacy hosts). |
| `HOSTKEY`| *(none)* | Comma-separated list of hostkey algorithms to force (for legacy hosts).     |

---

## ▶️ Usage

### Basic usage (default SOCKS5 proxy)
Start a SOCKS5 proxy on `127.0.0.1:1080`:
```bash
nxc ssh <target> -u <user> -p <pass> -M ssh_socks
nxc ssh <target> -u <user> -p <pass> -M ssh_socks -o PORT=9050
nxc ssh <target> -u <user> -p <pass> -M ssh_socks -o KEX="diffie-hellman-group1-sha1,diffie-hellman-group-exchange-sha1"
nxc ssh <target> -u <user> -p <pass> -M ssh_socks -o HOSTKEY="ssh-rsa,ssh-dss"
nxc ssh <target> -u <user> -p <pass> -M ssh_socks -o PORT=1081,KEX="diffie-hellman-group1-sha1",HOSTKEY="ssh-rsa"
```
To stop proxy ctrl+c in terminal window
