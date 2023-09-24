# Enumerate shares and access

Enumerate permissions on all shares

```
#~ nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --shares
```

{% hint style="info" %}
By fare one of the most useful feature of nxc
{% endhint %}

{% hint style="warning" %}
The following option is accessible to sponsors only
{% endhint %}

If you want to filter only by readable or writable share

```
#~ nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --shares --filter-shares READ WRITE
```
