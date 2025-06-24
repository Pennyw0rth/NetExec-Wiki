# EventLog Creds

### Parses Windows Event ID 4688 Logs

{% hint style="warning" %}
You need at least local admin privilege on the remote target
{% endhint %}

This module parses Event ID 4688 logs (from "Audit Process Creation") to extract credentials from CMD and PowerShell commands. E.g. "net user username password /add"

```bash
nxc smb <ip> -u username -p password -M eventlog_creds
```

![image](https://github.com/user-attachments/assets/ea7b71d4-4ecb-4662-8ad8-d3a811ab5d42)
