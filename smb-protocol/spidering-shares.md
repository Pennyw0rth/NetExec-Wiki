---
description: Spidering shares with NetExec
---

# Spidering Shares

## Using Default Option `--spider`

### Spider files and folders in share

The default option retrieves the name and path of all files and folders within a share.

Notice the '$' character has to be escaped. (example shown can be used as-is in a kali linux terminal)

```
nxc smb <ip> -u user -p password --spider c\$ 
```

### Spider all readabe shares

Use the option `--spider-all` to spider all readable shares

```
nxc smb <ip> -u user -p password --spider-all 

```

### Search for specific file and folder names 

Use the `--pattern` option to spider the C drive for files and folders with txt in the name

```
nxc SMB <IP> -u USER -p PASSWORD --spider C\$ --pattern txt
```

Also supports `--regex` for more specific searches. 

This query grabs files with only the .txt extenstion

```
nxc SMB <IP> -u USER -p PASSWORD --spider C\$  --regex ".*\.txt$"
```

### Search through content

The `--content` option seraches through text within readable files to match a specific pattern or regex query.

```
nxc SMB <IP> -u USER -p PASSWORD --spider C\$ content --pattern Creds
```

### Only display files or folders

The `-only-files` option can be used to only filter for files 

```
nxc SMB <IP> -u USER -p PASSWORD --spider C\$ --only-files
```
The `-only-folders` option can be used to only filter for folders

```
nxc SMB <IP> -u USER -p PASSWORD --spider C\$ --only-folders
```

### Search through a specific folder depth

Use the `--depth` option  to only search through a specific number of nested folders

```
nxc SMB <IP> -u USER -p PASSWORD --spider C\$ --depth 1
```

### Exclude Folders

Can  exclude certain folders within shares using the `exclude-folders` option

```
nxc SMB <IP> -u USER -p PASSWORD --spider C\$ --exclude-folders Documents Downloads
```


## Using Module "spider\_plus"

The module `spider_plus` allows you to list and dump all files from all readable shares thanks to [@vincd](https://github.com/vincd)

### List all readable files

```
nxc smb <ip> -u USER -p PASSWORD -M spider_plus
```

### Dumping All Files

Using the option `-o DOWNLOAD_FLAG=True` all files will be copied on the host

```
nxc smb <ip> -u USER -p PASSWORD -M spider_plus -o DOWNLOAD_FLAG=True
```
