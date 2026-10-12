# Enumerate Users

To enumerate all users via LDAP:

```bash
nxc ldap $ip -u $user -p $password --users
```

To export all users to a file:

```bash
nxc ldap $ip -u $user -p $password --users --export output.txt
```

> `--users-export` still works the same way but is deprecated in favor of `--users --export`.

To enumerate just the **active** users via LDAP:

```bash
nxc ldap $ip -u $user -p $password --active-users
```

To export just the active users to a file:

```bash
nxc ldap $ip -u $user -p $password --active-users --export output.txt
```

See the blog post by @TeRMaN (Mehmetcan Topal) on what exactly the differences are and why it was implemented: [https://medium.com/@mehmetcantopal/why-and-how-did-i-implement-an-active-users-ldap-feature-on-netexec-f5c7eff2cb79](https://medium.com/@mehmetcantopal/why-and-how-did-i-implement-an-active-users-ldap-feature-on-netexec-f5c7eff2cb79)
