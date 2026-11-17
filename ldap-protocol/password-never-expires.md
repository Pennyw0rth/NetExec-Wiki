# 🆕 Password Never Expires

Use `--password-never-expires` to find LDAP accounts whose `userAccountControl` attribute includes the `DONT_EXPIRE_PASSWORD` flag.

```bash
nxc ldap <target> -u <username> -p <password> --password-never-expires
```

Only enabled accounts are included in the results. Each result shows the account name and when its password was last set. A value of `<never>` means the password has never been set.

## Resources

* [UserAccountControl property flags (Microsoft Learn)](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/useraccountcontrol-manipulate-account-properties)
* [DONT_EXPIRE_PASSWORD (LDAPWiki)](https://ldapwiki.com/wiki/Wiki.jsp?page=DONT_EXPIRE_PASSWORD)
