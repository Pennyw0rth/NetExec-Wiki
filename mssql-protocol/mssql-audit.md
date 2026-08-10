---
description: Audit MSSQL servers for exploitable configurations
---

# MSSQL Audit Module

## Audit MSSQL for exploitable configurations

The `mssql_audit` module performs quick checks of targeted MSSQL servers to identify common misconfigurations and attack paths.
```bash
nxc mssql 10.10.10.52 -u admin -p 'password' -M mssql_audit
```

### Expected Results:
```bash
MSSQL       10.10.10.52     1433   SQL01            [*] Windows 10 / Server 2019 Build 17763 (name:SQL01) (domain:CORP.LOCAL)
MSSQL       10.10.10.52     1433   SQL01            [+] CORP.LOCAL\admin:password (Pwn3d!)
MSSQL_AUDIT 10.10.10.52     1433   SQL01            Service Account:          CORP\sqlsvc (Domain Account)
MSSQL_AUDIT 10.10.10.52     1433   SQL01            [+] Sysadmin Access:          YES
MSSQL_AUDIT 10.10.10.52     1433   SQL01            [+] xp_dirtree:               EXPLOITABLE
MSSQL_AUDIT 10.10.10.52     1433   SQL01            [+] xp_fileexist:             EXPLOITABLE
MSSQL_AUDIT 10.10.10.52     1433   SQL01            [+] MSSQL Relay:              EXPLOITABLE (Extended Protection: OFF)
MSSQL_AUDIT 192.168.56.12   1433   SQL01            [*] Impersonation:            1 user(s) can impersonate
MSSQL_AUDIT 192.168.56.12   1433   SQL01              → test_user can impersonate sa
MSSQL_AUDIT 10.10.10.52     1433   SQL01            [+] Linked servers found:
MSSQL_AUDIT 10.10.10.52     1433   SQL01            [+]   → PROD-SQL (Remote Login: sa) [SA, RPC]

```
___

## What it checks

The module identifies the following security issues:

* **Service Account** - Detects account the MSSQL service is running as (fingers crossed it's a privileged domain user)
* **Sysadmin Access** - Verifies if current user has sysadmin privileges
* **xp_dirtree / xp_fileexist** - Checks for default config allowing public execution of xp_dirtree and xp_fileexists stored procedures (opening the door for UNC Path injection attacks to intercept and/or relay the Net-NTLMv2 hash for the account running the MSSQL service)
* **Extended Protection** - Checks for MSSQL Extended protection configuration (to see if MSSQL relays are feasible)
* **Impersonation** - Enumerates privilege escalation paths via impersonation
* **Linked Servers** - Maps linked servers to identify authenticated context of linked DB from current access.
___
