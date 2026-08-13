---
description: Using Kerberos authentication with NetExec
---

# Using Kerberos

## Using Kerberos

NetExec does support Kerberos authentication. There are two options:&#x20;

* Using password/hash which automatically takes care of handling the TGT/ST
* Using an existing ticket by specifying the file via the `KRB5CCNAME` environment variable

```bash
$ nxc smb zoro.gold.local -u bonclay -p Ocotober2022 -k
SMB         zoro.gold.local 445    ZORO             [*] Windows 10.0 Build 14393 (name:ZORO) (domain:gold.local) (signing:False) (SMBv1:False)
SMB         zoro.gold.local 445    ZORO             [+] gold.local\bonclay
```

Or, using `--use-kcache`

```bash
$ export KRB5CCNAME=/home/bonclay/impacket/administrator.ccache 
$ nxc smb zoro.gold.local --use-kcache
SMB         zoro.gold.local 445    ZORO             [*] Windows 10.0 Build 14393 (name:ZORO) (domain:gold.local) (signing:False) (SMBv1:False)
SMB         zoro.gold.local 445    ZORO             [+] gold.local\administrator (Pwn3d!)
$ nxc smb zoro.gold.local --use-kcache -x whoami
SMB         zoro.gold.local 445    ZORO             [*] Windows 10.0 Build 14393 (name:ZORO) (domain:gold.local) (signing:False) (SMBv1:False)
SMB         zoro.gold.local 445    ZORO             [+] gold.local\administrator (Pwn3d!)
SMB         zoro.gold.local 445    ZORO             [+] Executed command 
SMB         zoro.gold.local 445    ZORO             gold\administrator

$ export KRB5CCNAME=/home/bonclay/impacket/bonclay.ccache
$ nxc smb zoro.gold.local --use-kcache -x whoami
SMB         zoro.gold.local 445    ZORO             [*] Windows 10.0 Build 14393 (name:ZORO) (domain:gold.local) (signing:False) (SMBv1:False)
SMB         zoro.gold.local 445    ZORO             [+] gold.local\bonclay
```

Example with LDAP and option `--kdcHost`

```bash
nxc ldap poudlard.wizard -k --kdcHost dc01.poudlard.wizard 
SMB poudlard.wizard 445 DC01 [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:poudlard.wizard) (signing:True) (SMBv1:False) 
LDAP poudlard.wizard 389 DC01 [+] poudlard.wizard\
```

### NTP Server Time Sync

Use the `--ntp-server` option to specify a NTP server which NetExec will use the time from before performing Kerberos exchanges. This time is only applied inside NetExec and does not affect the computer which runs NetExec. This feature requires that the NTP server is reachable via UDP port 123. The NTP server is in almost all cases the KDC, e.g. the Domain Controller. 

```bash
nxc ldap dc.domain.local --ntp-server dc.domain.local
```

This is needed as some Kerberos exchanges require that the NetExec host is in time with the KDC. If this is not the case, the following error will be thrown:

```
KerberosError: Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)
```
