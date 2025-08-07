# Enumerate Logged-On Users with the Remote Registry Service

This option uses the **Remote Registry Service** through the `\\winreg` pipe to check which user profiles are currently loaded in the user registry hive `HKEY_USERS`.

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --reg-sessions
```

{% hint style="warning" %}
Having a user listed by `--reg-sessions` does not guarantee that you can impersonate them via `schtask_as`, because that module requires the user to have an **active interactive session**. This option only indicate that the user has a primary token (login context) on the machine, not necessarily an interactive session.
{% endhint %}

## Filtering by username(s)

In case you want to hunt a specific user, you can specify a username: 

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --reg-sessions 'admin_user'
```

You can also pass a file containing a list of usernames:

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --reg-sessions './users.txt'
```