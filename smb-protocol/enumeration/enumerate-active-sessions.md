# Enumerate Active SMB Sessions

{% hint style="warning" %}
This most often requires admin privileges
{% endhint %}

Enumerate active SMB sessions (including RPC/DCOM over named pipes) on the remote target:

```
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --smb-sessions
```

As Windows might close the active SMB session after a short period of time (a few seconds to a minute) this has a high chance of false positives.&#x20;

{% hint style="info" %}
Previously `--sessions`
{% endhint %}
