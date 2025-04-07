---
description: >-
  Instructions for using FTP commands to access and transfer files using
  NetExec.
---

# 🆕 File Upload & Download

## List Files in a Directory

List files in a specific directory using FTP.

```
nxc ftp [IP_ADDRESS] -u [USERNAME] -p [PASSWORD] --ls [DIRECTORY]
```

Example:

```
nxc ftp 10.10.176.246 -u frank -p D2xc9CgD --ls
FTP         10.10.176.246   21     10.10.176.246    [*] Banner: (vsFTPd 3.0.3)
FTP         10.10.176.246   21     10.10.176.246    [+] frank:D2xc9CgD
FTP         10.10.176.246   21     10.10.176.246    [*] Directory Listing
FTP         10.10.176.246   21     10.10.176.246    drwx------   10 1001     1001         4096 Sep 15  2021 Maildir
FTP         10.10.176.246   21     10.10.176.246    -rw-rw-r--    1 1001     1001         4006 Sep 15  2021 README.txt
FTP         10.10.176.246   21     10.10.176.246    -rw-rw-r--    1 1001     1001           39 Sep 15  2021 ftp_flag.thm
```

## Download a File

Download a file from the FTP server.

```
nxc ftp [IP_ADDRESS] -u [USERNAME] -p [PASSWORD] --get [FILE]
```

Example:

```
nxc ftp 10.10.176.246 -u frank -p D2xc9CgD --get ftp_flag.thm
FTP         10.10.176.246   21     10.10.176.246    [*] Banner: (vsFTPd 3.0.3)
FTP         10.10.176.246   21     10.10.176.246    [+] frank:D2xc9CgD
FTP         10.10.176.246   21     10.10.176.246    [+] Downloaded: ftp_flag.thm
```

## Upload a File

Upload a file to the FTP server providing you have relevant permissions

```
nxc ftp [IP_ADDRESS] -u [USERNAME] -p [PASSWORD] --put [LOCAL_FILE] [REMOTE_FILE]
```

Example:

```
 nxc ftp 10.10.176.246 -u frank -p D2xc9CgD --put test.txt test.txt
FTP         10.10.176.246   21     10.10.176.246    [*] Banner: (vsFTPd 3.0.3)
FTP         10.10.176.246   21     10.10.176.246    [+] frank:D2xc9CgD
FTP         10.10.176.246   21     10.10.176.246    [-] Failed to upload file. Response: (550 Permission denied.)
```
