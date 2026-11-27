---
description: Get a remote file or send a remote file using NetExec
---

# Get and Put Files

## Send a File to the Remote Target

Send a local file to the remote target

```bash
nxc psql 10.10.1.10 -u postgres -p postgres --put-file localfile /tmp/remotefile
```

## Get a File From the Remote Target

Get a remote file on the remote target

```bash
nxc psql 10.10.1.10 -u postgres -p postgres --get-file /tmp/remotefile localfile
```
