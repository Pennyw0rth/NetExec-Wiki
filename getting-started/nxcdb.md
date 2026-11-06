
# nxcdb — The NetExec Database CLI

`nxcdb` is a dedicated command-line tool that ships alongside `nxc` and gives you a structured, interactive shell for querying, managing, and exporting everything that NetExec stores during an engagement like credentials, hosts, shares, groups, DPAPI blobs, and more.

Every scan and successful authentication `nxc` performs is automatically saved to a per-protocol SQLite database. `nxcdb` is how you get that data back out.

> [! Info ] 
> All workspaces and their databases are stored under `~/.nxc/workspaces/<workspace_name>/`

---

## Starting nxcdb

```bash
nxcdb
```

You will be dropped into an interactive prompt:

```
nxcdb (default) >
```

The word in parentheses is your **active workspace**. The default workspace is called `default`.

---

## Getting Help

Type `help` at any point to list available commands at the current level.

**At the workspace level:**

```
nxcdb (default) > help

Documented commands (type help <topic>):
========================================
exit  help  proto  workspace
```

**After selecting a protocol:**

```
nxcdb (default)(smb) > help

Documented commands (type help <topic>):
========================================
clear_database  creds  dpapi  exit  export  groups  help  hosts  shares  wcc

Undocumented commands:
======================
back  import
```

To get help on a specific command:

```
nxcdb (default)(smb) > help creds
```

---

## Workspaces

Workspaces provide logical separation between engagements, much like Metasploit workspaces. Any data collected by `nxc` is automatically saved to the active workspace, ensuring that results from different engagements remain isolated.

### Create a workspace

```
nxcdb (default) > workspace create shadowgate
[*] Creating workspace 'shadowgate'
nxcdb (shadowgate) >
```

### List workspaces

```
nxcdb (shadowgate) > workspace list
[*] Enumerating Workspaces
   default
   lacasa
 * shadowgate
```


The ` * ` marker indicates the currently active workspace.

### Switch workspace

```
nxcdb (shadowgate) > workspace default
nxcdb (default) >
```

>[!warning]
>Always check your active workspace before starting a new engagement. Data written to the wrong workspace cannot be automatically moved. 

---

## Selecting a Protocol Database

Switch into a protocol database with `proto`. Currently supported protocols are `smb`, `mssql`, and `winrm`:

```
nxcdb (shadowgate) > proto smb
nxcdb (shadowgate)(smb) >
```

>[!info"]
> `ftp`, `rdp`, `ldap`, and `ssh` are listed as unimplemented in `nxcdb`, use `nxc` output logs for those protocols for now. 

To return to the workspace root:

```
nxcdb (shadowgate)(smb) > back
nxcdb (shadowgate) >
```

---

## Querying the Database

### Hosts

List all discovered hosts:

```
nxcdb (shadowgate)(smb) > hosts
```

```markdown
+Hosts---+-----------+---------------+------------------+----------------------------+--------------------------------------+-------+---------+---------+-----------+------------+
| HostID | Admins    | IP            | Hostname         | Domain                     | OS                                   | SMBv1 | Signing | Spooler | Zerologon | PetitPotam |
+--------+-----------+---------------+------------------+----------------------------+--------------------------------------+-------+---------+---------+-----------+------------+
| 1      | 0 Cred(s) | 10.1.33.234   | DC01             | shadow.gate                | Windows Server 2022 Build 20348      | False | False   | None    | None      | None       |
| 2      | 0 Cred(s) | 10.1.39.169   | DC01             | DRY.MARTINI.BARS           | Windows 11 / Server 2025 Build 26100 | False | False   | None    | None      | None       |
| 3      | 0 Cred(s) | 172.16.100.7  | DCORP-STD607     | dollarcorp.moneycorp.local | Windows Server 2022 Build 20348      | False | False   | None    | None      | None       |
| 4      | 0 Cred(s) | 192.168.1.124 | MACS-MACBOOK-AIR | local                      | Windows 6.1 Build 7600               | False | True    | None    | None      | None       |
+--------+-----------+---------------+------------------+----------------------------+--------------------------------------+-------+---------+---------+-----------+------------+
```


**Subcommands:**

| Subcommand         | Description                             |
|--------------------|-----------------------------------------|
| `hosts dc`         | List all domain controllers             |
| `hosts spooler`    | List hosts with Spooler service enabled |
| `hosts zerologon`  | List hosts vulnerable to Zerologon      |
| `hosts petitpotam` | List hosts vulnerable to PetitPotam     |
| `hosts <filter>`   | Filter by IP or hostname (fuzzy match)  |

**Single-host drill-down** :  When a filter matches exactly one host (for example, by IP address), nxcdb displays an expanded host view that includes additional details, such as any credentials with administrative access associated with that host:

```
nxcdb (shadowgate)(smb) > hosts 10.1.33.234
```
```markdown
+Host----+-------------+----------+-------------+---------------------------------+------+-------+---------+---------+-----------+------------+
| HostID | IP          | Hostname | Domain      | OS                              | DC   | SMBv1 | Signing | Spooler | Zerologon | PetitPotam |
+--------+-------------+----------+-------------+---------------------------------+------+-------+---------+---------+-----------+------------+
| 1      | 10.1.33.234 | DC01     | shadow.gate | Windows Server 2022 Build 20348 | None | False | False   | None    | None      | None       |
+--------+-------------+----------+-------------+---------------------------------+------+-------+---------+---------+-----------+------------+

+Credential(s) with Admin Access-------+---------------+----------------------------------+
| CredID | CredType  | Domain          | UserName      | Password                         |
+--------+-----------+-----------------+---------------+----------------------------------+
| 35     | hash      |  shadow.gate    | Administrator | 4366ec0f86e29be2a4a5e87a1ba922ec |
+--------+-----------+-----------------+---------------+----------------------------------+
```

If a filter produces **multiple host matches (fuzzy matching)**, nxcdb returns the standard host listing rather than the detailed information for a single host.

```
nxcdb (shadowgate)(smb) > hosts DC01
```
```markdown
nxcdb (shadowgate)(smb) > hosts DC01

+Hosts---+-----------+-------------+----------+------------------+--------------------------------------+-------+---------+---------+-----------+------------+
| HostID | Admins    | IP          | Hostname | Domain           | OS                                   | SMBv1 | Signing | Spooler | Zerologon | PetitPotam |
+--------+-----------+-------------+----------+------------------+--------------------------------------+-------+---------+---------+-----------+------------+
| 1      | 0 Cred(s) | 10.1.33.234 | DC01     | shadow.gate      | Windows Server 2022 Build 20348      | False | False   | None    | None      | None       |
| 2      | 0 Cred(s) | 10.1.39.169 | DC01     | DRY.MARTINI.BARS | Windows 11 / Server 2025 Build 26100 | False | False   | None    | None      | None       |
+--------+-----------+-------------+----------+------------------+--------------------------------------+-------+---------+---------+-----------+------------+
```

---

### Credentials

List all stored credentials:

```
nxcdb (shadowgate)(smb) > creds
```
```markdown
+Credentials---------+-----------+------------------+------------+----------------------------------+
| CredID | Admin On  | CredType  | Domain           | UserName   | Password                         |
+--------+-----------+-----------+------------------+------------+----------------------------------+
| 1      | 0 Host(s) | plaintext | shadow.gate      | jtrueblood | blood_brothers                   |
| 2      | 0 Host(s) | hash      | shadow.gate      | bbrown     | 259745cb123a52aa2e693aaacca2db52 |
| 3      | 0 Host(s) | plaintext | shadow.gate      |            |                                  |
| 4      | 0 Host(s) | plaintext | DRY.MARTINI.BARS |            |                                  |
| 5      | 0 Host(s) | plaintext | DRY.MARTINI.BARS | guests     | guests                           |
| 6      | 0 Host(s) | plaintext | DRY.MARTINI.BARS | mprice     | *martini*                        |
+--------+-----------+-----------+------------------+------------+----------------------------------+
```



**Subcommands:**

| Subcommand                                                    | Description                      |
|---------------------------------------------------------------|----------------------------------|
| `creds plaintext`                                             | Show only plaintext credentials  |
| `creds hash`                                                  | Show only hashed credentials     |
| `creds <filter>`                                              | Filter by username (fuzzy match) |
| `creds add <domain> <user> <pass> [notes] [credType] [sid]`   | Manually add a credential        |
| `creds remove <credID>`                                       | Remove a credential by ID        |

**Single-credential drill-down**: When a filter matches exactly one credential, nxcdb displays an expanded view containing the credential details, associated group memberships, and any hosts where the credential has administrative access:

```
nxcdb (shadowgate)(smb) > creds bbrown
```
```markdown
+Credential(s)------+----------------------+-------------+----------+----------------------------------+
| CredID | CredType | Pillaged From HostID | Domain      | UserName | Password                         |
+--------+----------+----------------------+-------------+----------+----------------------------------+
| 2      | hash     | None                 | shadow.gate | bbrown   | 259745cb123a52aa2e693aaacca2db52 |
+--------+----------+----------------------+-------------+----------+----------------------------------+


+Member of Group(s)+------+
| GroupID | Domain | Name |
+---------+--------+------+


+Admin Access to Host(s)-+--------+----+
| HostID | IP | Hostname | Domain | OS |
+--------+----+----------+--------+----+
```



---

### Shares

List all enumerated shares:

```
nxcdb (shadowgate)(smb) > shares
```
```markdown
+---------+------+------------+---------------------------------------------+-------------+--------------+
| ShareID | host | Name       | Remark                                      | Read Access | Write Access |
+---------+------+------------+---------------------------------------------+-------------+--------------+
| 1       | DC01 | ADMIN$     | Remote Admin                                | 0 User(s)   | 0 Users      |
| 2       | DC01 | C$         | Default share                               | 0 User(s)   | 0 Users      |
| 3       | DC01 | CertEnroll | Active Directory Certificate Services share | 1 User(s)   | 0 Users      |
| 4       | DC01 | NETLOGON   | Logon server share                          | 2 User(s)   | 0 Users      |
| 5       | DC01 | SYSVOL     | Logon server share                          | 2 User(s)   | 0 Users      |
| 6       | DC01 | ADMIN$     | Remote Admin                                | 0 User(s)   | 0 Users      |
| 7       | DC01 | C$         | Default share                               | 0 User(s)   | 0 Users      |
| 8       | DC01 | NETLOGON   | Logon server share                          | 2 User(s)   | 0 Users      |
| 9       | DC01 | notes      |                                             | 2 User(s)   | 2 Users      |
| 10      | DC01 | SYSVOL     | Logon server share                          | 2 User(s)   | 0 Users      |
| 11      | DC01 | ADMIN$     | Remote Admin                                | 0 User(s)   | 0 Users      |
| 12      | DC01 | C$         | Default share                               | 0 User(s)   | 0 Users      |
| 13      | DC01 | NETLOGON   | Logon server share                          | 2 User(s)   | 0 Users      |
| 14      | DC01 | notes      |                                             | 2 User(s)   | 2 Users      |
| 15      | DC01 | SYSVOL     | Logon server share                          | 2 User(s)   | 0 Users      |
+---------+------+------------+---------------------------------------------+-------------+--------------+
```


**Single-share drill-down**: When a filter matches exactly one share, nxcdb displays an expanded view consisting of three tables: the share details, information about the host on which the share resides, and the users who have read access to the share.

```
nxcdb (shadowgate)(smb) > shares CertEnroll
```
```bash
+Share----+------------+---------------------------------------------+
| ShareID | Name       | Remark                                      |
+---------+------------+---------------------------------------------+
| 3       | CertEnroll | Active Directory Certificate Services share |
+---------+------------+---------------------------------------------+


+Share Location--------+----------+-------------+---------------------------------+------+
| HostID | IP          | Hostname | Domain      | OS                              | DC   |
+--------+-------------+----------+-------------+---------------------------------+------+
| 1      | 10.1.33.234 | DC01     | shadow.gate | Windows Server 2022 Build 20348 | None |
+--------+-------------+----------+-------------+---------------------------------+------+


+Users(s) with Read Access---------+------------+----------------+
| CredID | CredType  | Domain      | UserName   | Password       |
+--------+-----------+-------------+------------+----------------+
| 1      | plaintext | shadow.gate | jtrueblood | blood_brothers |
+--------+-----------+-------------+------------+----------------+
```


---

### Groups

List all enumerated domain groups:

```bash
nxcdb (shadowgate)(smb) > groups
```
```markdown
+Groups---+----------+-----------------------------------------+------+--------------------+------------+-----------------+
| GroupID | Domain   | Name                                    | RID  | Enumerated Members | AD Members | Last Query Time |
+---------+----------+-----------------------------------------+------+--------------------+------------+-----------------+
| 1       | CASADCSVR | Server Operators                        | 549  | 0                  | None       | None            |
| 2       | CASADCSVR | Account Operators                       | 548  | 0                  | None       | None            |
| 3       | CASADCSVR | Pre-Windows 2000 Compatible Access      | 554  | 0                  | None       | None            |
| 4       | CASADCSVR | Incoming Forest Trust Builders          | 557  | 0                  | None       | None            |
| 5       | CASADCSVR | Windows Authorization Access Group      | 560  | 0                  | None       | None            |
| 6       | CASADCSVR | Terminal Server License Servers         | 561  | 0                  | None       | None            |
| 7       | CASADCSVR | Administrators                          | 544  | 0                  | None       | None            |
| 8       | CASADCSVR | Users                                   | 545  | 0                  | None       | None            |
| 9       | CASADCSVR | Guests                                  | 546  | 0                  | None       | None            |
| 10      | CASADCSVR | Print Operators                         | 550  | 0                  | None       | None            |
| 11      | CASADCSVR | Backup Operators                        | 551  | 0                  | None       | None            |
| 12      | CASADCSVR | Replicator                              | 552  | 0                  | None       | None            |
| 13      | CASADCSVR | Remote Desktop Users                    | 555  | 0                  | None       | None            |
| 14      | CASADCSVR | Network Configuration Operators         | 556  | 0                  | None       | None            |
| 15      | CASADCSVR | Performance Monitor Users               | 558  | 0                  | None       | None            |
| 16      | CASADCSVR | Performance Log Users                   | 559  | 0                  | None       | None            |
| 17      | CASADCSVR | Distributed COM Users                   | 562  | 0                  | None       | None            |
| 18      | CASADCSVR | IIS_IUSRS                               | 568  | 0                  | None       | None            |
| 19      | CASADCSVR | Cryptographic Operators                 | 569  | 0                  | None       | None            |
| 20      | CASADCSVR | Event Log Readers                       | 573  | 0                  | None       | None            |
| 21      | CASADCSVR | Certificate Service DCOM Access         | 574  | 0                  | None       | None            |
| 22      | CASADCSVR | RDS Remote Access Servers               | 575  | 0                  | None       | None            |
| 23      | CASADCSVR | RDS Endpoint Servers                    | 576  | 0                  | None       | None            |
| 24      | CASADCSVR | RDS Management Servers                  | 577  | 0                  | None       | None            |
| 25      | CASADCSVR | Hyper-V Administrators                  | 578  | 0                  | None       | None            |
| 26      | CASADCSVR | Access Control Assistance Operators     | 579  | 0                  | None       | None            |
| 27      | CASADCSVR | Remote Management Users                 | 580  | 0                  | None       | None            |
| 28      | CASADCSVR | Storage Replica Administrators          | 582  | 0                  | None       | None            |
| 29      | CASADCSVR | Cert Publishers                         | 517  | 0                  | None       | None            |
| 30      | CASADCSVR | RAS and IAS Servers                     | 553  | 0                  | None       | None            |
| 31      | CASADCSVR | Allowed RODC Password Replication Group | 571  | 0                  | None       | None            |
| 32      | CASADCSVR | Denied RODC Password Replication Group  | 572  | 0                  | None       | None            |
| 33      | CASADCSVR | DnsAdmins                               | 1101 | 0                  | None       | None            |
| 34      | CASADCSVR | ADAuditPlusFS                           | 1314 | 0                  | None       | None            |
+---------+----------+-----------------------------------------+------+--------------------+------------+-----------------+
```


![](.gitbook/assets/nxcdb/09_groups.png)

Groups are populated when you run LDAP enumeration or use modules that enumerate AD groups. The `Enumerated Members` column shows how many members have been pulled. `Last Query Time` tracks when the group was last refreshed.

---

### DPAPI

List all DPAPI secrets recovered during the engagement:

```
nxcdb (shadowgate)(smb) > dpapi
```
```markdown
+DPAPI Secrets-------+------------+-----------------+----------------------------------+-------------------------+----------------------------------------------------------------------------------------------------+
| ID  | Host         | DPAPI Type | Windows User    | Username                         | Password                | URL                                                                                                |
+-----+--------------+------------+-----------------+----------------------------------+-------------------------+----------------------------------------------------------------------------------------------------+
| 24  | 10.10.10.144 | MSEDGE     |supervisor       | operations@lacasa.local          | Password@1              | https://www.globaltokingportal.com/Account/Logon                                                   |
| 26  | 10.10.10.144 | MSEDGE     |supervisor       | projects@lacasa.local            | None                    | https://www.velentral.com/Account/LogonReturnUrl=%2FDashboard                                      |
| 39  | 10.10.10.251 | MSEDGE     | k.nathan        | sam@lacasa.local                 | M7!qR2@vL9#xT4$k        | hhttps://admin.vertexcore.net/authenticate                                                         |
| 40  | 10.10.10.251 | MSEDGE     | k.nathan        | Manager		               | None                    | javascript:;                                                                                       |
| 41  | 10.10.10.251 | CREDENTIAL | k.nathan        | lACASA.SRV02\Administrator       | NeptCrypt02             | Domain:target=TERMSRV/10.10.10.146                                                                 |
| 42  | 10.10.10.251 | MSEDGE     | k.nathan        | 310924                           | None                    | https://secure.atlasindustrial.com/login                                                           |
| 43  | 10.10.10.251 | MSEDGE     | k.nathan        |                                  | None                    |                                                                                                    |
| 44  | 10.10.10.251 | CREDENTIAL | SYSTEM          | lACASA.LOCAL\k.nathan            | Iamsupportiv3           |                                                                                                    |
+-----+--------------+------------+-----------------+----------------------------------+-------------------------+----------------------------------------------------------------------------------------------------+
```

**Subcommands:**

| Subcommand          | Description                                |
|---------------------|--------------------------------------------|
| `dpapi browser`     | All secrets from any browser               |
| `dpapi chrome`      | Chrome-specific secrets                    |
| `dpapi msedge`      | Microsoft Edge secrets                     |
| `dpapi credentials` | Windows Credential Manager (user + system) |
| `dpapi iex`         | Internet Explorer secrets                  |
| `dpapi firefox`     | Firefox secrets                            |
| `dpapi <filter>`    | Filter by any term                         |

Example — querying Edge secrets:

```
nxcdb (lacasa)(smb) > dpapi msedge
```
```markdown
+DPAPI Secrets-------+------------+-----------------+----------------------------------+-------------------------+----------------------------------------------------------------------------------------------------+
| ID  | Host         | DPAPI Type | Windows User    | Username                         | Password                | URL                                                                                                |
+-----+--------------+------------+-----------------+----------------------------------+-------------------------+----------------------------------------------------------------------------------------------------+
| 24  | 10.10.10.144 | MSEDGE     |supervisor       | operations@lacasa.local          | Password@1              | https://www.globaltokingportal.com/Account/Logon                                                   |
| 26  | 10.10.10.144 | MSEDGE     |supervisor       | projects@lacasa.local            | None                    | https://www.velentral.com/Account/LogonReturnUrl=%2FDashboard                                      |
| 39  | 10.10.10.251 | MSEDGE     | k.nathan        | sam@lacasa.local                 | M7!qR2@vL9#xT4$k        | hhttps://admin.vertexcore.net/authenticate                                                         |
| 40  | 10.10.10.251 | MSEDGE     | k.nathan        | Manager		               | None                    | javascript:;                                                                                       |
| 41  | 10.10.10.251 | MSEDGE     | k.nathan        | Perla Kraetal                    | Spring2026!             | https://identity.hexaworks.io/login?session=9d71b4c8e2f563af                                       |
| 42  | 10.10.10.251 | MSEDGE     | k.nathan        | 310924                           | None                    | https://secure.atlasindustrial.com/login                                                           |
| 43  | 10.10.10.251 | MSEDGE     | k.nathan        |                                  | None                    |                                                                                                    |
| 44  | 10.10.10.251 | MSEDGE     | k.nathan        | support@lacasa.local             | Iamsupportiv3           | https://admin.vertexcore.net/auth?key=4b7e2c9d1a5f8e3c                                             |
+-----+--------------+------------+-----------------+----------------------------------+-------------------------+----------------------------------------------------------------------------------------------------+
```


>[!info]
Entries with `None` as the password indicate credentials that were saved by the browser but could not be decrypted, typically because the DPAPI master key for that user session was not recovered.


---

### WCC (Windows Configuration Checker)

Display results collected by the `wcc` module:

```
nxcdb (shadowgate)(smb) > wcc
```

By default shows IP, Hostname, Check name, and Status. For all columns:

```
nxcdb (shadowgate)(smb) > wcc full
```

To request specific columns only:

```
nxcdb (shadowgate)(smb) > wcc ip hostname check status reasons
```

---

## Exporting Data

Export any table to a file for reporting or further processing:

```
nxcdb (shadowgate)(smb) > export <table> <format> <filename>
```

### Supported tables and formats

| Table          | Formats                         | Notes                                                     |
|----------------|---------------------------------|-----------------------------------------------------------|
| `creds`        | `simple`, `detailed`            |                                                           |
| `hosts`        | `simple`, `detailed`, `signing` | `signing` writes a plain list of IPs with signing enabled |
| `shares`       | `simple`, `detailed`            |                                                           |
| `local_admins` | `simple`, `detailed`            |                                                           |
| `keys`         | `all`, `<id>`                   | DPAPI masterkeys                                          |

### Examples

Export credentials in detailed format:

```
nxcdb (shadowgate)(smb) > export creds detailed creds_shadowgate.csv
[+] Creds exported
```

Export a signing target list (useful for SMB relay attacks):

```
nxcdb (shadowgate)(smb) > export hosts signing signing_targets.txt
```

Export shares:

```
nxcdb (shadowgate)(smb) > export shares detailed shares_shadowgate.csv
```

>[!info]
>**`export keys` is currently broken.** Running `export keys all <filename>` throws the following error:
>```
>AttributeError: 'database' object has no attribute 'get_keys'
>```
>This is a bug in `nxcdb.py` — the `get_keys()` method is referenced in `do_export` but does not exist on the database object. Track it at [github.com/Pennyw0rth/NetExec/issues](https://github.com/Pennyw0rth/NetExec/issues). As a workaround, use `dpapi` subcommands to query secrets directly and export them via `export creds detailed`.

---

## Importing Data

Import a previously exported file back into the database:

```
nxcdb (shadowgate)(smb) > import creds_shadowgate.csv
```

---

## Clearing the Database

Wipe all data from the current protocol database:

```
nxcdb (shadowgate)(smb) > clear_database
```

>[!danger]
`clear_database` is irreversible. Export anything you need before running this command.


---

## Exiting nxcdb

```
nxcdb (shadowgate) > exit
```

You can also press `Ctrl+D` to exit cleanly.

---

## Tips

- Run `nxcdb` in a **separate terminal** during an engagement so you can query results while `nxc` scans are still running.
- Use **one workspace per client or engagement** — it keeps your data clean and makes reporting much easier.
- The `signing` export (`export hosts signing`) gives you a ready-made target list for SMB relay attacks.
- Filter commands like `hosts`, `creds`, and `shares` all accept a fuzzy search term — you don't need exact matches.
- All databases are plain SQLite files under `~/.nxc/workspaces/` , you can query them directly with `sqlite3` if you need something `nxcdb` doesn't expose yet.
