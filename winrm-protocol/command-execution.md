# Command execution

Execute Command using WinRM

```
#~ nxc winrm 192.168.255.131 -u user -p 'password' -X whoami
WINRM       192.168.255.131 5985   ROGER            [*] http://192.168.255.131:5985/wsman
WINRM       192.168.255.131 5985   ROGER            [+] GOLD\user:password (Pwn3d!)
WINRM       192.168.255.131 5985   ROGER            [+] Executed command
WINRM       192.168.255.131 5985   ROGER            gold\user
```

## What next ?

Evil-winrm tool to pwn everything !

{% embed url="https://github.com/Hackplayers/evil-winrm" %}
