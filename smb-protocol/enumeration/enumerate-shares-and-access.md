# Enumerate Shares and Access

Enumerate permissions on all shares

```bash
nxc smb 192.168.1.0/24 -u user -p 'PASSWORDHERE' --shares
```

{% hint style="info" %}
By far one of the most useful feature of nxc
{% endhint %}

If you want to filter only by readable or writable share

```bash
nxc smb 192.168.1.0/24 -u user -p 'PASSWORDHERE' --shares READ,WRITE
nxc smb 192.168.1.0/24 -u user -p 'PASSWORDHERE' --shares READ
nxc smb 192.168.1.0/24 -u user -p 'PASSWORDHERE' --shares WRITE
```
