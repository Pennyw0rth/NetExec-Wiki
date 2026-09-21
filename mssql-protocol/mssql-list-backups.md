---
description: Dumping databases backups paths and encryption status
---

Using the --list-backups it is now possible to determine if databases were backed up, where and whether they are encrypted or not:

```bash
 $ nxc <ip> -u user -p password --list-backups
MSSQL       192.168.56.72   54830  SRV22            [*] Windows Server 2022 Build 20348 (name:NAME) (domain:FQDN.local) (EncryptionReq:True) 
MSSQL       192.168.56.72   54830  SRV22            [+] FQDN\user:password (Pwn3d!)
MSSQL       192.168.56.72   54830  SRV22            [*] Enumerated backups
MSSQL       192.168.56.72   54830  SRV22            Backup Name          Encryption      Backup Path
MSSQL       192.168.56.72   54830  SRV22            -----------          ----------      -----------
MSSQL       192.168.56.72   54830  SRV22            db_target            Unencrypted     C:\Windows\Temp\db_target_20260921.bak
MSSQL       192.168.56.72   54830  SRV22            test                 Unencrypted     C:\Windows\Temp\test_20260921.bak
```

