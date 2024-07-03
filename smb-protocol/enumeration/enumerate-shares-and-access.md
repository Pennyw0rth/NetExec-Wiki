# Enumerate Shares and Access

Enumerate permissions on all shares

```
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --shares
```

{% hint style="info" %}
By far one of the most useful feature of nxc
{% endhint %}

If you want to filter only by readable or writable share

```
#~ nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --shares --filter-shares READ WRITE
```
