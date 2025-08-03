# Enumerate Logged on Users

To enumerate logged on users on a remote target, the following options can be used.

## --loggedon-users

This option queries the Windows Workstation Service via the `\wkssvc` named pipe to retrieve the list of authenticated users and the Domain Controller they connected to.

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --loggedon-users
```

## --reg-sessions

This option uses the Remote Registry service through the `\winreg` pipe to check which user profiles are currently loaded in the user registry hive (HKEY_USERS), which includes local users.

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --reg-sessions
```

{% hint style="warning" %}
Having a user listed by `--loggedon-users` or `--reg-sessions` does not guarantee that you can impersonate them via `schtask_as`, because that module requires the user to have an **active interactive session**. These two options only indicate that the user has a primary token (login context) on the machine, not necessarily an interactive session.
{% endhint %}

## Filtering by username(s)

In case you want to hunt a specific user, you can specify a username. This works with both `--loggedon-users` and `--reg-sessions`:

```bash
nxc smb 192.168.1.0/24 -u UserName -p 'PASSWORDHERE' --loggedon-users username
```

For `--reg-sessions` you can also pass a file containing a list of usernames:

```bash
nxc smb 192.168.1.0/24 -u UserName -p 'PASSWORDHERE' --reg-sessions userfile
```