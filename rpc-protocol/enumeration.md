# Enumeration Operations

## Enumerate Domain Users
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-users

SMB  192.168.1.100  445  DC01  [+] Found 25 user(s)
SMB  192.168.1.100  445  DC01  user:[Administrator] rid:[0x1f4]
SMB  192.168.1.100  445  DC01  user:[Guest] rid:[0x1f5]
SMB  192.168.1.100  445  DC01  user:[krbtgt] rid:[0x1f6]
```

## Enumerate Domain Groups
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-groups

SMB  192.168.1.100  445  DC01  [+] Found 15 group(s)
SMB  192.168.1.100  445  DC01  group:[Domain Admins] rid:[0x200]
SMB  192.168.1.100  445  DC01  group:[Domain Users] rid:[0x201]
SMB  192.168.1.100  445  DC01  group:[Domain Guests] rid:[0x202]
```

## Enumerate Local Groups
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-local-groups

SMB  192.168.1.100  445  DC01  [+] Found 20 alias group(s)
SMB  192.168.1.100  445  DC01  group:[Administrators] rid:[0x220]
SMB  192.168.1.100  445  DC01  group:[Users] rid:[0x221]
SMB  192.168.1.100  445  DC01  group:[Guests] rid:[0x222]
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

SMB  192.168.1.100  445  DC01  [+] User Administrator is a member of 3 group(s)
SMB  192.168.1.100  445  DC01  [*]   rid:[0x200] group:[Domain Admins]
SMB  192.168.1.100  445  DC01  [*]   rid:[0x201] group:[Domain Users]
```

## Query Group Information
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-group "Domain Admins"

SMB  192.168.1.100  445  DC01  Group Name: Domain Admins
SMB  192.168.1.100  445  DC01  Description: Designated administrators of the domain
SMB  192.168.1.100  445  DC01  Group Attributes: 7
SMB  192.168.1.100  445  DC01  Num Members: 3
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
SMB  192.168.1.100  445  DC01  share:[ADMIN$] type:[DISKTREE] comment:[Remote Admin]
SMB  192.168.1.100  445  DC01  share:[C$] type:[DISKTREE] comment:[Default share]
SMB  192.168.1.100  445  DC01  share:[IPC$] type:[IPC] comment:[Remote IPC]
```

## Query Share Information
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-share NETLOGON

SMB  192.168.1.100  445  DC01  Share NETLOGON:
SMB  192.168.1.100  445  DC01    Type: DISKTREE
SMB  192.168.1.100  445  DC01    Comment: Logon server share
SMB  192.168.1.100  445  DC01    Current users: 0
SMB  192.168.1.100  445  DC01    Path: C:\Windows\SYSVOL\sysvol\contoso.local\SCRIPTS
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