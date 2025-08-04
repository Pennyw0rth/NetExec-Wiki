# Enumerate Logged-On Users with the Workstation Service

To enumerate logged on users on a remote target, the following option can be used:

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --loggedon-users
```

Note that if a username is returned, you will be able to impersonate that user's primary token to run commands on its behalf. 

In case you want to hunt a specific user, you can specify its username the following way:

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --loggedon-users username
```