---
description: Detect the BadSuccessor privilege escalation vulnerability in Active Directory
---

# BadSuccessor

The `badsuccessor` module checks if any user or group has dangerous permissions (such as `CreateChild`) over an Organizational Unit (OU) in Active Directory. This can be abused via Delegated Managed Service Accounts (DMSA) to escalate privileges.

Based on the research: [Abusing dMSA for Privilege Escalation in Active Directory](https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory)

{% hint style="warning" %}
This vulnerability requires at least one Windows Server 2025 Domain Controller in the domain.
{% endhint %}

```bash
nxc ldap <ip> -u <user> -p <pass> -M badsuccessor
```

The module enumerates OUs and analyzes their DACLs for the following dangerous rights:

* **GenericAll** / **GenericWrite**
* **CreateChild**
* **WriteProperties**
* **WriteDACL** / **WriteOwner**
* **AllExtendedRights**

Built-in administrative accounts (Domain Admins, Enterprise Admins, Builtin Administrators, SYSTEM) are excluded from results automatically.
