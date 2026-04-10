---
description: >-
  Instructions for using FTP commands to access and transfer files using
  NetExec.
---

# File Upload & Download

## List Files in a Directory

List files in a specific directory using FTP.

```bash
nxc ftp 10.10.176.246 -u frank -p D2xc9CgD --ls
```

Expected Results:

```bash
FTP         10.10.176.246   21     10.10.176.246    [*] Banner: (vsFTPd 3.0.3)
FTP         10.10.176.246   21     10.10.176.246    [+] frank:D2xc9CgD
FTP         10.10.176.246   21     10.10.176.246    [*] Directory Listing
FTP         10.10.176.246   21     10.10.176.246    drwx------   10 1001     1001         4096 Sep 15  2021 Maildir
FTP         10.10.176.246   21     10.10.176.246    -rw-rw-r--    1 1001     1001         4006 Sep 15  2021 README.txt
FTP         10.10.176.246   21     10.10.176.246    -rw-rw-r--    1 1001     1001           39 Sep 15  2021 ftp_flag.thm
```

## Download a File

Download a file from the FTP server.

```bash
nxc ftp 10.10.176.246 -u frank -p D2xc9CgD --get ftp_flag.thm
```

Expected Results:

```bash
FTP         10.10.176.246   21     10.10.176.246    [*] Banner: (vsFTPd 3.0.3)
FTP         10.10.176.246   21     10.10.176.246    [+] frank:D2xc9CgD
FTP         10.10.176.246   21     10.10.176.246    [+] Downloaded: ftp_flag.thm
```

## Upload a File

Upload a file to the FTP server providing you have relevant permissions

```bash
nxc ftp [IP_ADDRESS] -u [USERNAME] -p [PASSWORD] --put [LOCAL_FILE] [REMOTE_FILE]
```

Expected Results:

```bash
FTP         10.10.176.246   21     10.10.176.246    [*] Banner: (vsFTPd 3.0.3)
FTP         10.10.176.246   21     10.10.176.246    [+] frank:D2xc9CgD
FTP         10.10.176.246   21     10.10.176.246    [+] Uploaded: test.txt to test.txt
```

#### Specify port

```bash
nxc ftp 192.168.0.10 -u 'marshall' -p 'badpassword' --port 2121
FTP         192.168.0.10   2121   192.168.0.10    [*] Banner: (vsFTPd 3.0.5)
FTP         192.168.0.10   2121   192.168.0.10    [+] marshall:badpassword
```
