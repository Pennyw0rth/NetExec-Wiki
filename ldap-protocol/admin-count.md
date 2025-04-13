# Admin Count

> **adminCount** Indicates that a given object has had its ACLs changed to a more secure value by the system because it was a member of one of the administrative groups (directly or transitively).

This will get you all user objects with the `adminCount` attribute set to `1`:

```bash
nxc ldap 192.168.255.131 -u adm -p pass --admin-count
```

If you want all objects in ldap you can query them manually:

```bash
nxc ldap 192.168.255.131 -u adm -p pass --query "(adminCount=1)" "sAMAccountName"
```

{% embed url="https://troopers.de/downloads/troopers19/TROOPERS19_AD_Fun_With_LDAP.pdf" %}
