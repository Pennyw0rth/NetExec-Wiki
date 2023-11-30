---
description: Instructions for using FTP commands to access and transfer files using NetExec.

# FTP File Access and Transfer

## List Files in a Directory

List files in a specific directory using FTP.

```
netexec ftp [IP_ADDRESS] -u [USERNAME] -p [PASSWORD] --ls [DIRECTORY]
```

Example:
```
netexec ftp 10.10.176.246 -u frank -p D2xc9CgD --ls
```

## Download a File

Download a file from the FTP server.

```
netexec ftp [IP_ADDRESS] -u [USERNAME] -p [PASSWORD] --get [FILE]
```

Example:
```
netexec ftp 10.10.176.246 -u frank -p D2xc9CgD --get ftp_flag.thm
```

## Upload a File

Upload a file to the FTP server.

```
netexec ftp [IP_ADDRESS] -u [USERNAME] -p [PASSWORD] --put [LOCAL_FILE] [REMOTE_FILE]
```

Example:
```
netexec ftp 10.10.176.246 -u frank -p D2xc9CgD --put localFile.txt remoteFile.txt
```