---
description: Get a remote file or send a remote file using NetExec
---

# Get and Put Files

## Send a File to the Remote Target

Send a local file to the remote target

```
nxc ssh 172.16.251.152 -u user -p pass --put-file file.txt /tmp/file.txt
```

## Get a File From the Remote Target

Get a remote file on the remote target

```
nxc ssh 172.16.251.152 -u user -p pass --get-file /tmp/file.txt file.txt
```
