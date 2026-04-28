---
description: >-
  Instructions for using FTP commands to access and transfer files using
  NetExec.
---

# File Upload & Download

## Download a File

Download a file from the FTP server.

```bash
nxc ftp <ip> -u <username> -p <password> --get <filename>
```

Expected Results:

```bash
nxc ftp 10.10.176.246 -u frank -p D2xc9CgD --get ftp_flag.thm
FTP         10.10.176.246   21     10.10.176.246    [*] Banner: (vsFTPd 3.0.3)
FTP         10.10.176.246   21     10.10.176.246    [+] frank:D2xc9CgD
FTP         10.10.176.246   21     10.10.176.246    [+] Downloaded: ftp_flag.thm
```

## Upload a File

Upload a file to the FTP server providing you have relevant permissions. The first argument after `--put` will be the location of the file on your local machine to upload. The second argument determines the path and filename:

```bash
nxc ftp <ip> -u <username> -p <password> --put <local-file> <remote-path>
```

Expected Results:

```bash
nxc ftp 10.10.176.246 -u frank -p D2xc9CgD --put test.txt test.txt
FTP         10.10.176.246   21     10.10.176.246    [*] Banner: (vsFTPd 3.0.3)
FTP         10.10.176.246   21     10.10.176.246    [+] frank:D2xc9CgD
FTP         10.10.176.246   21     10.10.176.246    [+] Uploaded: test.txt to test.txt
```
