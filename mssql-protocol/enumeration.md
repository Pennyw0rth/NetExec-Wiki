# Enumerating encryption and channel binding token

## Enumerating encryption settings

By default MSSQL databases do not enforce TLS ciphering which makes eavesdroping possible. There are two configurations values that can be set:

* Force encryption: that will force establishing a TLS tunnel via the STARTTLS mechanism ;
* Force strict encryption: which will force a standard TLS tunnel without having to use the STARTTLS mechanism.

NetExec will tell you whether one of these two options is enabled via the EncryptionReq flag on the host enumeration:

```bash
nxc mssql 192.168.56.0/24
MSSQL       192.168.56.72   1433   SRV22            [*] Windows Server 2022 Build 20348 (name:SRV22) (domain:whiteflag.local) (EncryptionReq:True)
```

### Enumerating Channel Binding configuration

Having a valid account, it is possible to check whether CBT is required are not (and thus determine whether relay is possible or not) via the mssql_cbt module:

```bash
nxc mssql 192.168.56.72 -u username -p password -M mssql_cbt
MSSQL       192.168.56.72   1433   SRV22            [*] Windows Server 2022 Build 20348 (name:SRV22) (domain:whiteflag.local) (EncryptionReq:True)
MSSQL       192.168.56.72   1433   SRV22            [+] whiteflag.local\username:password 
MSSQL_CBT   192.168.56.72   1433   SRV22            Connection successful: Channel Binding Token NOT REQUIRED
```

If the result is anything but "Channel Binding token REQUIRED", then relaying will be possible.
