---
description: Search for computers in the domain by name or operating system
---

# Find Computer

The `find-computer` module searches for computer objects in Active Directory matching a given text string against computer names or operating system fields. It also attempts DNS resolution to retrieve the IP address of each result.

```bash
nxc ldap <ip> -u <user> -p <pass> -M find-computer -o TEXT=<search_string>
```

| Option | Description | Required |
|--------|-------------|----------|
| TEXT   | String to match against computer name or operating system | Yes |

**Examples:**

```bash
# Find computers running Windows Server 2019
nxc ldap <ip> -u <user> -p <pass> -M find-computer -o TEXT="Server 2019"

# Find computers with a specific name pattern
nxc ldap <ip> -u <user> -p <pass> -M find-computer -o TEXT="DC"
```
