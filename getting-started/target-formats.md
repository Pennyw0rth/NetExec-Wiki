---
description: NetExec target formats
---

# Target Formats

## Target Formats

Every protocol supports targets by CIDR notation(s), IP address(s), IP range(s), hostname(s), a file containing a list of targets or combination of all of the latter:

```bash
nxc <protocol> poudlard.wizard
```

```bash
nxc <protocol> 192.168.1.0 192.168.0.2
```

```bash
nxc <protocol> 192.168.1.0/24
```

```bash
nxc <protocol> 192.168.1.0-28 10.0.0.1-67
```

```bash
nxc <protocol> ~/targets.txt
```
