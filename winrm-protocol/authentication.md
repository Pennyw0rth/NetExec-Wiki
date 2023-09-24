# Authentication

### WinRM Authentication

#### Testing credentials

```
#~ nxc winrm 192.168.1.0/24 -u user -p password
```

Expected Results:

```
WINRM       192.168.255.131 5985   ROGER            [*] http://192.168.255.131:5985/wsman
WINRM       192.168.255.131 5985   ROGER            [+] GOLD\user:password (Pwn3d!)
```

If the SMB port is closed you can also use the flag `-d DOMAIN` to avoid an SMB connection

```
#~ nxc winrm 192.168.1.0/24 -u user -p password -d DOMAIN
```

Expected Results:

```
WINRM       192.168.255.131 5985   192.168.255.131  [*] http://192.168.255.131:5985/wsman
WINRM       192.168.255.131 5985   192.168.255.131  [+] GOLD\user:password (Pwn3d!)
```

### Example

Monteverde machine is a good example to test **WinRM** procotol with NetExec

{% embed url="https://www.hackthebox.eu/home/machines/profile/223" %}
