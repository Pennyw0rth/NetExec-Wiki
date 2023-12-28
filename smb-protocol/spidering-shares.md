---
description: Spidering shares with NetExec
---

# Spidering Shares

## Using Default Option `--spider`

Options for spidering shares of remote systems. Example, Spider the C drive for files with txt in the name (finds both sometxtfile.html and somefile.txt)

Notice the '$' character has to be escaped. (example shown can be used as-is in a kali linux terminal)

```
nxc SMB <IP> -u USER -p PASSWORD --spider C\$ --pattern txt
```

## Using Module "spider\_plus"

The module `spider_plus` allows you to list and dump all files from all readable shares thanks to [@vincd](https://github.com/vincd)

### List all readable files

```
nxc smb 10.10.10.10 -u 'user' -p 'pass' -M spider_plus
```

### Dumping All Files

Using the option `-o DOWNLOAD_FLAG=True` all files will be copied on the host

```
nxc smb 10.10.10.10 -u 'user' -p 'pass' -M spider_plus -o DOWNLOAD_FLAG=True
```
