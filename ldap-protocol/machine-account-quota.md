# Machine Account Quota

The `maq` module retrieves the domain `ms-DS-MachineAccountQuota` value and checks the effective `SeMachineAccountPrivilege` configuration applied to Domain Controllers through GPOs.

```bash
nxc ldap <ip> -u user -p pass -M maq
```

The module analyzes GPOs linked to the Domain Controllers OU and the domain root, taking into account link order, enforced links, blocked inheritance and disabled links.
GPOs are displayed in priority order, with the highest-priority applicable GPOs shown first.

{% hint style="warning" %}
When using --schannel, MachineAccountQuota is still retrieved, but SeMachineAccountPrivilege is skipped because Schannel authentication does not provide reusable credentials for accessing SYSVOL over SMB.
{% endhint %}
