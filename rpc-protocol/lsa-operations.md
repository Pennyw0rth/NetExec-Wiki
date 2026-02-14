# LSA Operations

## LSA Query
```bash
nxc smb 192.168.1.100 -u username -p password --lsa-query

SMB  192.168.1.100  445  DC01  Domain Name: CONTOSO
SMB  192.168.1.100  445  DC01  Domain SID: S-1-5-21-1234567890-1234567890-1234567890
```

## Enumerate LSA SIDs
```bash
nxc smb 192.168.1.100 -u username -p password --lsa-sids

SMB  192.168.1.100  445  DC01  [+] Found 15 SID(s)
SMB  192.168.1.100  445  DC01    S-1-5-21-xxx-500
SMB  192.168.1.100  445  DC01    S-1-5-21-xxx-512
SMB  192.168.1.100  445  DC01    S-1-5-32-544
SMB  192.168.1.100  445  DC01    S-1-1-0
```

## Enumerate Privileges
```bash
nxc smb 192.168.1.100 -u username -p password --lsa-privs

SMB  192.168.1.100  445  DC01  [+] Found 35 privilege(s)
SMB  192.168.1.100  445  DC01    SeCreateTokenPrivilege (0x2)
SMB  192.168.1.100  445  DC01    SeAssignPrimaryTokenPrivilege (0x3)
SMB  192.168.1.100  445  DC01    SeDebugPrivilege (0x14)
```

## Account Rights (Privileges)
```bash
nxc smb 192.168.1.100 -u username -p password --lsa-rights S-1-5-32-544

SMB  192.168.1.100  445  DC01  [+] Rights for S-1-5-32-544:
SMB  192.168.1.100  445  DC01    SeBackupPrivilege
SMB  192.168.1.100  445  DC01    SeRestorePrivilege
SMB  192.168.1.100  445  DC01    SeShutdownPrivilege
```

## Lookup SIDs to Names
```bash
nxc smb 192.168.1.100 -u username -p password --lsa-lookup-sids "S-1-5-21-xxx-500,S-1-5-21-xxx-512,S-1-1-0"

SMB  192.168.1.100  445  DC01  S-1-5-21-xxx-500 -> CONTOSO\Administrator (User)
SMB  192.168.1.100  445  DC01  S-1-5-21-xxx-512 -> CONTOSO\Domain Admins (Group)
SMB  192.168.1.100  445  DC01  S-1-1-0 -> Everyone (WellKnown)
```

## Create LSA Account
```bash
nxc smb 192.168.1.100 -u admin -p password --lsa-create-account S-1-5-21-xxx-1001

SMB  192.168.1.100  445  DC01  [+] Created LSA account for S-1-5-21-xxx-1001
```

## Query LSA Security
```bash
nxc smb 192.168.1.100 -u username -p password --lsa-query-security

SMB  192.168.1.100  445  DC01  revision: 1
SMB  192.168.1.100  445  DC01  type: 0x8004: SEC_DESC_DACL_PRESENT SEC_DESC_SELF_RELATIVE
SMB  192.168.1.100  445  DC01  DACL
SMB  192.168.1.100  445  DC01      ACL     Num ACEs:   9   revision:   2
SMB  192.168.1.100  445  DC01      ---
SMB  192.168.1.100  445  DC01      ACE
SMB  192.168.1.100  445  DC01          type: ACCESS ALLOWED (0) flags: 0x00
SMB  192.168.1.100  445  DC01          Permissions: 0xf1fff: WRITE_OWNER_ACCESS WRITE_DAC_ACCESS READ_CONTROL_ACCESS
SMB  192.168.1.100  445  DC01          SID: S-1-5-32-544
```