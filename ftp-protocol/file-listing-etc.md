# 🆕 File Listing, etc

## Listing Files

Do directory listings on valid authentication by using the `--ls` option:

```bash
nxc ftp 192.168.0.10 -u 'marshall' -p 'badpassword' --ls
FTP         192.168.0.10   21     192.168.0.10    [*] Banner: (vsFTPd 3.0.5)
FTP         192.168.0.10   21     192.168.0.10    [+] marshall:badpassword
FTP         192.168.0.10   21     192.168.0.10    [*] Directory Listing
FTP         192.168.0.10   21     192.168.0.10    drwxr-xr-x    2 1000     1000         4096 Sep 30 17:29 Desktop
FTP         192.168.0.10   21     192.168.0.10    drwxr-xr-x    2 1000     1000         4096 Aug 28  2022 Documents
FTP         192.168.0.10   21     192.168.0.10    drwxr-xr-x    2 1000     1000         4096 Jul 13 23:42 Downloads
FTP         192.168.0.10   21     192.168.0.10    drwxr-xr-x    2 1000     1000         4096 Aug 28  2022 Music
FTP         192.168.0.10   21     192.168.0.10    drwxr-xr-x    2 1000     1000         4096 Aug 28  2022 Pictures
FTP         192.168.0.10   21     192.168.0.10    drwxr-xr-x    2 1000     1000         4096 Aug 28  2022 Public
FTP         192.168.0.10   21     192.168.0.10    drwxr-xr-x    2 1000     1000         4096 Aug 28  2022 Templates
FTP         192.168.0.10   21     192.168.0.10    drwxr-xr-x    2 1000     1000         4096 Aug 28  2022 Videos
FTP         192.168.0.10   21     192.168.0.10    drwx------    4 1000     1000         4096 Aug 28  2022 snap
```

