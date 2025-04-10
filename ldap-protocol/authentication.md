# Authentication

### LDAP Authentication

Testing if an account exists without kerberos protocol

```bash
nxc ldap 192.168.1.0/24 -u users.txt -p '' -k
```

#### Testing credentials

```bash
nxc ldap 192.168.1.0/24 -u user -p password
```

```bash
nxc ldap 192.168.1.0/24 -u user -H A29F7623FD11550DEF0192DE9246F46B
```

Expected Results:

```bash
LDAP        192.168.255.131 5985   ROGER            [+] GOLD\user:password
```

{% hint style="warning" %}
Domain name resolution is expected
{% endhint %}

By default, the ldap protocol will get the domain name by making connection to the SMB share (of the dc), if you don't want that initial connection, just add the option `--no-smb`
