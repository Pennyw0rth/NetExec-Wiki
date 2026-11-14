# 🆕 Password Never Expires

Use `--password-never-expires` to find LDAP accounts whose `userAccountControl` attribute includes the `DONT_EXPIRE_PASSWORD` flag.

```bash
nxc ldap <target> -u <username> -p <password> --password-never-expires
```

Each result includes the account name and whether the account is enabled or disabled. Disabled accounts are included in the results.

## Resources

* [UserAccountControl property flags (Microsoft Learn)](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/useraccountcontrol-manipulate-account-properties)
* [DONT_EXPIRE_PASSWORD (LDAPWiki)](https://ldapwiki.com/wiki/Wiki.jsp?page=DONT_EXPIRE_PASSWORD)
