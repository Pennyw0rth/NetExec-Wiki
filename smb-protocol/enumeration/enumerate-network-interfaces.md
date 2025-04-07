# 🆕 Enumerate Network Interfaces

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

Enumerate network interfaces on a host:

```bash
nxc smb 192.168.56.11 -u USERNAME -p 'PASSWORDHERE' --interfaces
```

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption><p>Example output of the interface enumeration</p></figcaption></figure>
