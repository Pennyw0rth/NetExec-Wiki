# Get User Descriptions

New LDAP module to look for password inside the user's description.

```
nxc ldap <hostname> -u <user> -p <pass> -M get-desc-users
```

Three options are available:

* **FILTER**: To look for a string inside the description
* **PASSWORDPOLICY**: To look for password according to the complexity requirements of windows
* **MINLENGTH**: Choose the minimum length of the password (may be obtained from `--pass-pol`)
