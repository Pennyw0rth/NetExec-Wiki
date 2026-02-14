# User Management

## Create User
```bash
nxc smb 192.168.1.100 -u admin -p password --create-user newuser:Password123!

SMB  192.168.1.100  445  DC01  [*] Creating user (createdomuser newuser)
SMB  192.168.1.100  445  DC01  [+] Created user newuser with RID 0x450
```

## Delete User
```bash
nxc smb 192.168.1.100 -u admin -p password --delete-user testuser

SMB  192.168.1.100  445  DC01  [*] Deleting user (deletedomuser testuser)
SMB  192.168.1.100  445  DC01  [+] Deleted user testuser
```

## Enable User
```bash
nxc smb 192.168.1.100 -u admin -p password --enable-user disableduser

SMB  192.168.1.100  445  DC01  [*] Enabling user account (setuserinfo2 disableduser)
SMB  192.168.1.100  445  DC01  [+] Enabled user disableduser (UAC: 0x202 -> 0x200)
```

## Disable User
```bash
nxc smb 192.168.1.100 -u admin -p password --disable-user targetuser

SMB  192.168.1.100  445  DC01  [*] Disabling user account (setuserinfo2 targetuser)
SMB  192.168.1.100  445  DC01  [+] Disabled user targetuser (UAC: 0x200 -> 0x202)
```

## Change Password (with old password)
```bash
nxc smb 192.168.1.100 -u username -p password --change-password targetuser:OldPass123:NewPass456!

SMB  192.168.1.100  445  DC01  [*] Changing password (chgpasswd targetuser)
SMB  192.168.1.100  445  DC01  [+] Changed password for targetuser
```

## Reset Password (administrative)
```bash
nxc smb 192.168.1.100 -u admin -p password --reset-password targetuser:NewPass456!

SMB  192.168.1.100  445  DC01  [*] Resetting password for targetuser
SMB  192.168.1.100  445  DC01  [+] Reset password for targetuser
```

## Query User Information
```bash
nxc smb 192.168.1.100 -u username -p password --rpc-user Administrator

SMB  192.168.1.100  445  DC01  User Name: Administrator
SMB  192.168.1.100  445  DC01  Full Name: 
SMB  192.168.1.100  445  DC01  Home Directory: 
SMB  192.168.1.100  445  DC01  Profile Path: 
SMB  192.168.1.100  445  DC01  Description: Built-in account for administering the computer/domain
SMB  192.168.1.100  445  DC01  User RID: 0x1f4
SMB  192.168.1.100  445  DC01  Primary Group RID: 0x201
SMB  192.168.1.100  445  DC01  Account Flags: 0x210
```