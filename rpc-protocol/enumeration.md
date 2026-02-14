# Enumeration Operations

## Enumerate Domain Users
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-users

SMB  192.168.1.100  445  DC01  [+] Found 25 domain user(s)
SMB  192.168.1.100  445  DC01  RID    Username             BadPW  PW Last Set          PW Can Change        Description
SMB  192.168.1.100  445  DC01  500    Administrator        0      2021-08-31 00:51:58  2021-09-01 03:51:58  Built-in account for administering...
SMB  192.168.1.100  445  DC01  501    Guest                0      Never                Never                Built-in account for guest access...
SMB  192.168.1.100  445  DC01  502    krbtgt               0      2021-08-30 15:23:18  2021-08-31 15:23:18  Key Distribution Center Service...
```



## Enumerate Groups
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-groups

SMB  192.168.1.100  445  DC01  [+] Domain Groups (15)
SMB  192.168.1.100  445  DC01  RID    Group                          Members  Description
SMB  192.168.1.100  445  DC01  512    Domain Admins                  3        Designated administrators of the domain
SMB  192.168.1.100  445  DC01  513    Domain Users                   45       All domain users
SMB  192.168.1.100  445  DC01  514    Domain Guests                  0        All domain guests

SMB  192.168.1.100  445  DC01  [+] Builtin/Local Groups (20)
SMB  192.168.1.100  445  DC01  RID    Group                          Members  Description
SMB  192.168.1.100  445  DC01  544    Administrators                 4        Administrators have complete and unrestricted access
SMB  192.168.1.100  445  DC01  545    Users                          2        Users are prevented from making accidental changes
SMB  192.168.1.100  445  DC01  546    Guests                         1        Guests have the same access as members of the Users group
```



## Query User Information
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-user Administrator

SMB  192.168.1.100  445  DC01  User Name: Administrator
SMB  192.168.1.100  445  DC01  Full Name: 
SMB  192.168.1.100  445  DC01  Home Directory: 
SMB  192.168.1.100  445  DC01  Description: Built-in account for administering the computer/domain
SMB  192.168.1.100  445  DC01  User RID: 0x1f4
SMB  192.168.1.100  445  DC01  Primary Group RID: 0x201
SMB  192.168.1.100  445  DC01  Account Flags: 0x210
```

## Query User Groups
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-user-groups Administrator

SMB  192.168.1.100  445  DC01  [+] Groups for user Administrator (3 groups)
SMB  192.168.1.100  445  DC01    RID      ATTR   Name
SMB  192.168.1.100  445  DC01    -------- ------ ------------------------------
SMB  192.168.1.100  445  DC01    512      7      Domain Admins
SMB  192.168.1.100  445  DC01    513      7      Domain Users
SMB  192.168.1.100  445  DC01    520      7      Group Policy Creator Owners
```

## Query Group Information
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-group "Domain Admins"

SMB  192.168.1.100  445  DC01  [+] Group: Domain Admins
SMB  192.168.1.100  445  DC01    Description: Designated administrators of the domain
SMB  192.168.1.100  445  DC01    Attributes: 7
SMB  192.168.1.100  445  DC01    Member Count: 3
SMB  192.168.1.100  445  DC01    Members: Administrator, IT-Admin, backup
```

## Query Domain Information
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-dom-info

SMB  192.168.1.100  445  DC01  Domain: CONTOSO
SMB  192.168.1.100  445  DC01  Server: DC01
SMB  192.168.1.100  445  DC01  Comment: Primary Domain Controller
SMB  192.168.1.100  445  DC01  Domain SID: S-1-5-21-1234567890-1234567890-1234567890
```

## Query Password Policy
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-pass-pol

SMB  192.168.1.100  445  DC01  Min Password Length: 7
SMB  192.168.1.100  445  DC01  Password History: 24
SMB  192.168.1.100  445  DC01  Maximum Password Age: 42 days
SMB  192.168.1.100  445  DC01  Password Complexity: Enabled
```

## Enumerate Domain Trusts
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-trusts

SMB  192.168.1.100  445  DC01  [+] Found 2 domain trust(s)
SMB  192.168.1.100  445  DC01  CHILD.CONTOSO.LOCAL (external, forest: CHILD.CONTOSO.LOCAL)
SMB  192.168.1.100  445  DC01  PARTNER.COM (external, forest: PARTNER.COM)
```

## Enumerate Shares
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-shares

SMB  192.168.1.100  445  DC01  [+] Found 6 share(s)
SMB  192.168.1.100  445  DC01  Share           Type       Perms        Remark                         Path
SMB  192.168.1.100  445  DC01  ----------------------------------------------------------------------------------------------------
SMB  192.168.1.100  445  DC01  ADMIN$          Disk       READ,WRITE   Remote Admin                   C:\Windows
SMB  192.168.1.100  445  DC01  C$              Disk       READ,WRITE   Default share                  C:\
SMB  192.168.1.100  445  DC01  IPC$            IPC                     Remote IPC
SMB  192.168.1.100  445  DC01  NETLOGON        Disk       READ         Logon server share             C:\Windows\SYSVOL\sysvol\contoso.local\SCRIPTS
SMB  192.168.1.100  445  DC01  SYSVOL          Disk       READ         Logon server share             C:\Windows\SYSVOL\sysvol
```



## Enumerate Sessions
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-sessions

SMB  192.168.1.100  445  DC01  [+] Found 5 session(s)
SMB  192.168.1.100  445  DC01  user:Administrator from:192.168.1.50 time:2h15m idle:5m
SMB  192.168.1.100  445  DC01  user:jdoe from:192.168.1.120 time:4h idle:30m
```

## Enumerate Server Info
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-server-info

SMB  192.168.1.100  445  DC01  Server Information:
SMB  192.168.1.100  445  DC01  Server Name: DC01
SMB  192.168.1.100  445  DC01  Server Domain: CONTOSO
SMB  192.168.1.100  445  DC01  Server OS: Windows Server 2019 Standard
SMB  192.168.1.100  445  DC01  Server OS Build: 17763
```

## RID Brute Force
```bash
nxc smb 192.168.1.100 -u username -p password --rid-brute 1000

SMB  192.168.1.100  445  DC01  [+] Found 35 accounts via RID cycling:
SMB  192.168.1.100  445  DC01  500: Administrator (Built-in account for administering the computer/domain)
SMB  192.168.1.100  445  DC01  501: Guest (Built-in account for guest access to the computer/domain)
SMB  192.168.1.100  445  DC01  502: krbtgt (Key Distribution Center Service Account)
```