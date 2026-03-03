# Enumerate NTLMv1

{% include "../../.gitbook/includes/admin-privs.md" %}

Enumerate the LmCompatibilityLevel on the remote target via the remote registry:

```bash
nxc smb <ip> -u user -p password -M ntlmv1
SMB         <ip>   445    <FQDN>            [*] Windows 10 / Server 2019 Build 17763 x64 (name:<FQDN>) (domain:<FQDN>) (signing:False) (SMBv1:None)
SMB         <ip>   445    <FQDN>            [+] <FQDN>\user:password (Pwn3d!)
NTLMV1      <ip>   445    <FQDN>            NTLMv1 allowed on: <ip> - LmCompatibilityLevel = 2
```

Outgoing NTLMv1 connections are enabled when the target’s LmCompatibilityLevel is lower than 3.

{% embed url="https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/network-security-lan-manager-authentication-level" %}
