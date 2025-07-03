# Check LDAP Signing

{% hint style="danger" %}
REMOVED: Checking for signing and channel binding is now done on the host enumeration, see host banner
{% endhint %}

Using the module `ldap-checker` you can verify if ldap require channel binding or not

```bash
nxc ldap <ip> -u user -p pass -M ldap-checker
```
