---
description: Check if host some vulnerabilities or important things.
---

# Scan for Vulnerabilities and Important Things.

## Scan for Vulnerabilities and Important Things.

When you start your internal pentest, these are the first modules you should try:

#### Badsuccessor
This LDAP module checks if a user has "Create all child objects" on any OU.
Based on https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory#credentials

```bash
nxc ldap <ip> -u username -p password -M badsuccessor
```

#### Check LDAP Signing

Using the module `ldap-checker` you can verify if LDAP require channel binding or not.

```bash
nxc ldap <ip> -u username -p password -M ldap-checker
```

#### userPassword Attribute
Get userPassword Attribute from all users for potentially credentials in plaintext.

```bash
nxc ldap <ip> -u username -p password -M get-userPassword
```

#### unixUserPassword Attribute 
Get unixUserPassword Attribute from all users for potentially credentials in plaintext.

```bash
nxc ldap <ip> -u username -p password -M get-unixUserPassword
```

#### Network
Extract subnet over an active directory environment.

```bash
nxc ldap <ip> -u username -p password -M get-network
nxc ldap <ip> -u username -p password -M get-network -o ONLY_HOSTS=true
nxc ldap <ip> -u username -p password -M get-network -o ALL=true
```

#### User Descriptions
This LDAP module to look for password inside the user's description.

```bash
nxc ldap <ip> -u username -p password -M get-desc-users
```
Three options are available:

* **FILTER**: To look for a string inside the description
* **PASSWORDPOLICY**: To look for password according to the complexity requirements of windows
* **MINLENGTH**: Choose the minimum length of the password (may be obtained from `--pass-pol`)

#### Find Computers
Find Computers in the domain.

```bash
nxc ldap <ip> -u username -p password -M find-computer
```

#### Machine Account Quota

This module retrieves the MachineAccountQuota domain-level attribute. It's useful to check this value because by default it permits unprivileged users to attach up to 10 computers to an Active Directory (AD) domain.

```bash
nxc ldap <ip> -u username -p password -M maq
```
