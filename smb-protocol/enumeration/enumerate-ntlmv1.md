# Enumerate NTLMv1
Enumerate the LmCompatibilityLevel on the remote target using a privileged user:
```bash
nxc smb <ip> -u user -p password -M ntlmv1
SMB         <ip>   445    <FQDN>            [*] Windows 10 / Server 2019 Build 17763 x64 (name:<FQDN>) (domain:<FQDN>) (signing:False) (SMBv1:None)
SMB         <ip>   445    <FQDN>            [+] <FQDN>\user:password (Pwn3d!)
NTLMV1      <ip>   445    <FQDN>            NTLMv1 allowed on: <ip> - LmCompatibilityLevel = 2
```

NTLMv1 is enabled when the target’s LmCompatibilityLevel is lower than 3.
