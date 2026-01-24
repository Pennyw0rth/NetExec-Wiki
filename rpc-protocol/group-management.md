# Group Management

## Create Group
```bash
nxc smb 192.168.1.100 -u admin -p password --create-group "IT Support"

SMB  192.168.1.100  445  DC01  [*] Creating group (createdomgroup IT Support)
SMB  192.168.1.100  445  DC01  [+] Created group IT Support with RID 0x450
```

## Delete Group
```bash
nxc smb 192.168.1.100 -u admin -p password --delete-group "Old Team"

SMB  192.168.1.100  445  DC01  [*] Deleting group (deletedomgroup Old Team)
SMB  192.168.1.100  445  DC01  [+] Deleted group Old Team
```

## Add User to Group
```bash
nxc smb 192.168.1.100 -u admin -p password --add-to-group "john.doe:IT Support"

SMB  192.168.1.100  445  DC01  [*] Adding john.doe to group IT Support
SMB  192.168.1.100  445  DC01  [+] Added john.doe to IT Support
```

## Remove User from Group
```bash
nxc smb 192.168.1.100 -u admin -p password --remove-from-group "john.doe:IT Support"

SMB  192.168.1.100  445  DC01  [*] Removing john.doe from group IT Support
SMB  192.168.1.100  445  DC01  [+] Removed john.doe from IT Support
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

## Query Group Information
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-group "Domain Admins"

SMB  192.168.1.100  445  DC01  Group Name: Domain Admins
SMB  192.168.1.100  445  DC01  Description: Designated administrators of the domain
SMB  192.168.1.100  445  DC01  Group Attributes: 7
SMB  192.168.1.100  445  DC01  Num Members: 3
```