---
description: >-
  Instructions for using FTP commands to access and transfer files using
  NetExec.
---

# File Upload & Download

## List Files in a Directory

To retrieve files, the [list](file-listing.md) flag should be used to determine the target file on the FTP server:

```bash
nxc ftp <ip> -u <username> -p <password> --ls <directory>
```

Expected Results:

```bash
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

Upload a file to the FTP server providing you have relevant permissions. The first argument after `--put` will be the location of the file on your local machine to upload. The following argument determines the name of the file when uploaded:

```bash
nxc ftp 10.10.176.246 <ip> -u <username> -p <password> --put <local-file> <filename>
```

Expected Results:

```bash
nxc ftp 10.10.176.246 -u frank -p D2xc9CgD --put test.txt test.txt
FTP         10.10.176.246   21     10.10.176.246    [*] Banner: (vsFTPd 3.0.3)
FTP         10.10.176.246   21     10.10.176.246    [+] frank:D2xc9CgD
FTP         10.10.176.246   21     10.10.176.246    [+] Uploaded: test.txt to test.txt
```
