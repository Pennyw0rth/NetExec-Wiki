# 🆕 Enumerating Channel Binding configuration

Having a valid account, it is possible to check whether CBT is required are not (and thus determine whether relay is possible or not) via the mssql\_cbt module:

```bash
> nxc mssql 192.168.56.72 -u username -p password -M mssql_cbt
MSSQL       192.168.56.72   1433   SRV22            [*] Windows Server 2022 Build 20348 (name:SRV22) (domain:whiteflag.local) (EncryptionReq:True)
MSSQL       192.168.56.72   1433   SRV22            [+] whiteflag.local\username:password 
MSSQL_CBT   192.168.56.72   1433   SRV22            Connection successful: Channel Binding Token NOT REQUIRED
```

If the result is anything but "Channel Binding token REQUIRED", then relaying is possible.
