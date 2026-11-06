# Admin Count

> **adminCount** Indicates that a given object has had its ACLs changed to a more secure value by the system because it was a member of one of the administrative groups (directly or transitively).

This will get you all user objects with the `adminCount` attribute set to `1`:

```bash
nxc adws 192.168.1.100 -u user -p password -d domain.local --admin-count
```

If you want all objects you can query them manually:

```bash
nxc adws 192.168.1.100 -u user -p password -d domain.local --query "(adminCount=1)" "sAMAccountName"
```
