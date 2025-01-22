---
description: Using Certificates authentication with NetExec
---

# Using Certificates

```
netexec smb 192.168.0.1 --pfx-cert user.pfx -u user 
```

```
netexec smb 192.168.0.1 --pfx-cert user.pfx --pfx-pass password -u user 
```

```
netexec smb 192.168.0.1 --pfx-base64 user.pfx -u user 
```

```
netexec smb 192.168.0.1 --pem-cert user.pem --pem-key key.pem -u user 
```

{% hint style="info" %}
When authenticate with a certificate, nxc will generate a ccache file inside nxc home directory, you can also use this ccache to authenticate with kerberos for other tools
{% endhint %}

