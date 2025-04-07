---
description: NetExec target formats
---

# Target Formats

## Target Formats

Every protocol supports targets by CIDR notation(s), IP address(s), IP range(s), hostname(s), a file containing a list of targets or combination of all of the latter:

```
nxc <protocol> poudlard.wizard
```

```
nxc <protocol> 192.168.1.0 192.168.0.2
```

```
nxc <protocol> 192.168.1.0/24
```

```
nxc <protocol> 192.168.1.0-28 10.0.0.1-67
```

```
nxc <protocol> ~/targets.txt
```
