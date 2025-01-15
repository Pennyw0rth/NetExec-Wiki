# Bloodhound Ingestor

NetExec has a build in bloodhound collector. To configure the name server, dns timeout or to use tcp for dns resolution take a look at the NetExec command line options for [dns](../getting-started/dns-options.md).

```
nxc ldap <ip> -u user -p pass --bloodhound --collection All
```

#### Specifying Bloodhound collection methods
```
nxc ldap <ip> -u user -p pass --bloodhound --collection Method1,Method2
```

The other collection methods can be found at the official Bloodhound.py docs [here](https://github.com/dirkjanm/BloodHound.py/blob/master/README.md#usage).
