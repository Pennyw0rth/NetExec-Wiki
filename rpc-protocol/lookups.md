# Lookup Operations

## Lookup Names to SIDs
```bash
nxc smb 192.168.1.100 -u username -p password --lookup-names "Administrator,Guest"

SMB  192.168.1.100  445  DC01  Administrator -> S-1-5-21-xxx-500 (User)
SMB  192.168.1.100  445  DC01  Guest -> S-1-5-21-xxx-501 (User)
```

## LSA Lookup Names
```bash
nxc smb 192.168.1.100 -u username -p password --lsa-lookup-names "Administrator,Everyone"

SMB  192.168.1.100  445  DC01  Administrator -> CONTOSO\Administrator S-1-5-21-xxx-500 (User)
SMB  192.168.1.100  445  DC01  Everyone -> Everyone S-1-1-0 (WellKnown)
```

## LSA Lookup SIDs
```bash
nxc smb 192.168.1.100 -u username -p password --lsa-lookup-sids "S-1-5-21-xxx-500,S-1-1-0"

SMB  192.168.1.100  445  DC01  S-1-5-21-xxx-500 -> CONTOSO\Administrator (User)
SMB  192.168.1.100  445  DC01  S-1-1-0 -> Everyone (WellKnown)
```

## Lookup Domain SID
```bash
nxc smb 192.168.1.100 -u username -p password --lookup-domain CONTOSO

SMB  192.168.1.100  445  DC01  Domain CONTOSO -> SID S-1-5-21-1234567890-1234567890-1234567890
```

## SAM Lookup (Domain)
```bash
nxc smb 192.168.1.100 -u username -p password --sam-lookup domain "Administrator,Domain Admins"

SMB  192.168.1.100  445  DC01  Administrator S-1-5-21-xxx-500 (User: 1)
SMB  192.168.1.100  445  DC01  Domain Admins S-1-5-21-xxx-512 (Group: 2)
```

## SAM Lookup (Builtin)
```bash
nxc smb 192.168.1.100 -u username -p password --sam-lookup builtin "Administrators,Users"

SMB  192.168.1.100  445  DC01  Administrators S-1-5-32-544 (Alias: 4)
SMB  192.168.1.100  445  DC01  Users S-1-5-32-545 (Alias: 4)
```

## Query User Group Membership
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-user-groups Administrator

SMB  192.168.1.100  445  DC01  [+] User Administrator is a member of 3 group(s)
SMB  192.168.1.100  445  DC01  [*]   rid:[0x200] group:[Domain Admins] attr:[MANDATORY, ENABLED_BY_DEFAULT, ENABLED]
SMB  192.168.1.100  445  DC01  [*]   rid:[0x201] group:[Domain Users] attr:[MANDATORY, ENABLED_BY_DEFAULT, ENABLED]
```

## RID Brute Force
```bash
nxc smb 192.168.1.100 -u username -p password --rid-brute 1000

SMB  192.168.1.100  445  DC01  [+] Found 35 accounts via RID cycling:
SMB  192.168.1.100  445  DC01  500: Administrator (Built-in account for administering the computer/domain)
SMB  192.168.1.100  445  DC01  501: Guest (Built-in account for guest access to the computer/domain)
SMB  192.168.1.100  445  DC01  502: krbtgt (Key Distribution Center Service Account)
```