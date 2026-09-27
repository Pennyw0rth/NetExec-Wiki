# 🆕 Modify Group

If a user has privileges such as AddMember, AddSelf, etc. over a group, this module can add or remove users from that group.

{% hint style="warning" %}
SAMR only supports modification of Global security groups.
Domain Local and Universal groups require the LDAP protocol.
Cross-domain groups (e.g. Enterprise Admins) cannot be modified via SAMR, use LDAP instead.
{% endhint %}

### Add User to Group

Just specify the target user and target group name.

```bash
nxc smb <ip> -u user -p pass -M modify-group -o USER=TargetUser GROUP=TargetGroup
```

### Remove User from Group

If want to remove the target user from the group, just specify the `REMOVE=True` option.

```bash
nxc smb <ip> -u user -p pass -M modify-group -o USER=TargetUser GROUP=TargetGroup REMOVE=True
```
