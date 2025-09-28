# Enumerate Null Sessions

Check if **Null Session**, also known as Anonymous session, is enabled on the network. Can be very useful on a Domain Controller to enumerate users, groups, password policies, etc.

```bash
nxc smb 10.10.10.161 -u '' -p ''
nxc smb 10.10.10.161 -u '' -p '' --shares
nxc smb 10.10.10.161 -u '' -p '' --pass-pol
nxc smb 10.10.10.161 -u '' -p '' --users
nxc smb 10.10.10.161 -u '' -p '' --groups
```

You can also reproduce this behavior with `smbclient` or `rpcclient`

```bash
smbclient -N -U "" -L \\10.10.10.161
```

```bash
rpcclient -N -U "" -L \\10.10.10.161
rpcclient $> enumdomusers
user:[bonclay] rid:[0x46e]
user:[zoro] rid:[0x46f]
```

{% embed url="https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj852200(v=ws.11)" %}

### Example

Forest or Monteverde machines are good examples to test **null session** authentication with NetExec

{% embed url="https://www.hackthebox.com/machines/forest" %}

{% embed url="https://www.hackthebox.com/machines/monteverde" %}


