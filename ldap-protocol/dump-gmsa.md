---
description: Extract gmsa credentials accounts
---

# Dump gMSA

Using the protocol LDAP you can extract the password of a gMSA account if you have the right.

{% hint style="warning" %}
LDAPS is required to retrieve the password, using the --gmsa LDAPS is automatically selected
{% endhint %}

```
$ NetExec ldap <ip> -u <user> -p <pass> --gmsa
```
