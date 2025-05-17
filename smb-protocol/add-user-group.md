# 🆕 Add User Group

If a user with capabilities such as AddMember, AddSelf, etc. has control, this module can add or remove users from the target group.

### Add User to Group

Only need to specify target user and target group name.


```bash
nxc smb <ip> -u user -p pass -M add-group -o USER=TargetUser Group=TargetGroup
```

If want to remove the target user to group, just need to specify REMOVE true value.
```bash
nxc smb <ip> -u user -p pass -M add-group -o USER=TargetUser Group=TargetGroup REMOVE=True
```
