# Machine Account Quota

This module retrieves the MachineAccountQuota domain-level attribute. It's useful to check this value because by default it permits unprivileged users to attach up to 10 computers to an Active Directory (AD) domain.

```bash
nxc ldap <ip> -u user -p pass -M maq
```
