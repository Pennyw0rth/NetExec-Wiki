---
description: Execute MSSQL command using NetExec
---

# MSSQL command

### Execute MSSQL command

```
nxc mssql 10.10.10.52 -u admin -p 'm$$ql_S@_P@ssW0rd!' --local-auth -q 'SELECT name FROM master.dbo.sysdatabases;'
```

Expected Results:

```
MSSQL       10.10.10.52     1433   None             [+] admin:m$$ql_S@_P@ssW0rd! (Pwn3d!)
MSSQL       10.10.10.52     1433   None             name
MSSQL       10.10.10.52     1433   None             --------------------------------------------------------------------------------------------------------------------------------
MSSQL       10.10.10.52     1433   None             master
MSSQL       10.10.10.52     1433   None             tempdb
MSSQL       10.10.10.52     1433   None             model
MSSQL       10.10.10.52     1433   None             msdb
MSSQL       10.10.10.52     1433   None             orcharddb
```

{% hint style="info" %}
When playing with MSSQL, you can use the tool [MSDAT ](https://github.com/quentinhardy/msdat)from [quentinhardy](https://github.com/quentinhardy)
{% endhint %}

{% embed url="https://github.com/quentinhardy/msdat" %}

### Example

Mantis machine is a good example to test **MSSQL** procotol with NetExec

{% embed url="https://www.hackthebox.eu/home/machines/profile/98" %}
