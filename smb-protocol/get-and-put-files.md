---
description: Get a remote file or send a remote file using NetExec
---

# Get and Put files

## Send a file to the remote target

Send a local file to the remote target

```
#~ nxc smb 172.16.251.152 -u user -p pass --put-file /tmp/whoami.txt \\Windows\\Temp\\whoami.txt
```

## Get a file from the remote target

Get a remote file on the remote target

```
#~ nxc smb 172.16.251.152 -u user -p pass --get-file  \\Windows\\Temp\\whoami.txt /tmp/whoami.txt
```
