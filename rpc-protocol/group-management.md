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

## Query Group Information 
```bash
# Query domain group
nxc smb 192.168.1.100 -u username -p password --rpc-group "Domain Admins"

SMB  192.168.1.100  445  DC01  [+] Group: Domain Admins
SMB  192.168.1.100  445  DC01    Description: Designated administrators of the domain
SMB  192.168.1.100  445  DC01    Attributes: 7
SMB  192.168.1.100  445  DC01    Member Count: 3
SMB  192.168.1.100  445  DC01    Members: Administrator, IT-Admin, backup

# Query builtin/local group
nxc smb 192.168.1.100 -u username -p password --rpc-group "Administrators"

SMB  192.168.1.100  445  DC01  [+] Group: Administrators
SMB  192.168.1.100  445  DC01    Description: Administrators have complete and unrestricted access to the computer/domain
SMB  192.168.1.100  445  DC01    Attributes: 0
SMB  192.168.1.100  445  DC01    Member Count: 4
SMB  192.168.1.100  445  DC01    Members: Domain Admins, Administrator, Administrator, SYSTEM
```

