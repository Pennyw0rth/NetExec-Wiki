# WinRM Relay Module

This module allows relaying commands from one WinRM host to another.  
It can be used to execute commands on a relayed target by authenticating through another WinRM host.  

Options structure is as follows
```bash
REMOTE=<hostname or IP> <username> <password> <domain name>
```

For more than one relay
```bash
REMOTE=<hostname or IP> <username> <password> <domain name>,REMOTE=<hostname or IP> <username> <password> <domain name>,REMOTE=<hostname or IP> <username> <password> <domain name>
```
---

## Example 1: Relay with username and password (utilizing same username and password on remote machine)

### Command
```bash
nxc winrm 192.168.56.12 \
    -u user1 -p 'Passw0rd!' \
    -x whoami \
    -M winrm_relay \
    -o REMOTE=192.168.56.11
```

### Expected Response

```bash
[*] Authenticating to 192.168.56.12 as user1
[+] Authentication successful
[*] Relaying to 192.168.56.11
[+] whoami executed successfully
domain\user1
```

### Relay Alternate Usernames and Passwords Along with Alternate Domain (multiple relays)

```bash
nxc winrm 192.168.56.11 -u vagrant -p vagrant -x hostname -M winrm_relay -o REMOTE='192.168.56.12 admin P@ssw0rd! ESSOS.LOCAL','KINGSLANDING admin P@ssw0rd! sevenkingdoms.local'
```

### Expected Response

```bash
WINRM       192.168.56.11   5985   WINTERFELL       [*] Windows 10 / Server 2019 Build 17763 (name:WINTERFELL) (domain:north.sevenkingdoms.local) 
WINRM       192.168.56.11   5985   WINTERFELL       [+] north.sevenkingdoms.local\vagrant:vagrant (Pwn3d!)
WINRM_RELAY 192.168.56.11   5985   WINTERFELL       meereen: essos\admin
WINRM_RELAY 192.168.56.11   5985   WINTERFELL       KINGSLANDING.sevenkingdoms.local: sevenkingdoms\admin
```

