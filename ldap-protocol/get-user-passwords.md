---
description: Retrieve plaintext or hashed passwords stored in LDAP user attributes
---

# Get User Passwords from LDAP Attributes

Some Active Directory environments store passwords in legacy LDAP attributes. The following modules check for credentials left in these fields.

## userPassword Attribute

Retrieves the `userPassword` attribute from all user objects. This attribute may contain plaintext passwords in non-standard or legacy configurations.

```bash
nxc ldap <ip> -u <user> -p <pass> -M get-userPassword
```

## unixUserPassword Attribute

Retrieves the `unixUserPassword` attribute from all user objects. Common in Unix-integrated Active Directory environments, this attribute may contain password hashes.

```bash
nxc ldap <ip> -u <user> -p <pass> -M get-unixUserPassword
```
