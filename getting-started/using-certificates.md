---
description: Using Certificates authentication with NetExec
---

# Using Certificates

```
netexec smb 192.168.0.1 --cert-pfx user.pfx -u user 
```

```
netexec smb 192.168.0.1 --cert-pfx user.pfx --pfx-pass password -u user 
```

```
netexec smb 192.168.0.1 --pfx-base64 user.pfx -u user 
```

```
netexec smb 192.168.0.1 --cert-pem user.pem --key-pem key.pem -u user 
```

{% hint style="info" %}
When authenticate with a certificate, nxc will generate a ccache file inside nxc home directory, you can also use this ccache to authenticate with kerberos for other tools
{% endhint %}
