---
description: Get a remote file or send a remote file using NetExec
---

# Get and Put Files

## Send a File to the Remote Target

Send a local file to the remote target

```bash
nxc smb 172.16.251.152 -u user -p pass --put-file /tmp/whoami.txt \\Windows\\Temp\\whoami.txt
```

## Get a File From the Remote Target

Get a remote file on the remote target

```bash
nxc smb 172.16.251.152 -u user -p pass --get-file \\Windows\\Temp\\whoami.txt /tmp/whoami.txt
```
