# Authentication

## Anonymous Login

```bash
nxc ftp 192.168.0.10 -u '' -p ''
FTP         192.168.0.10   21     192.168.0.10    [*] Banner: (vsFTPd 3.0.5)
FTP         192.168.0.10   21     192.168.0.10    [+] : - Anonymous Login!
```

## Testing Credentials

```bash
nxc ftp 192.168.0.10 -u 'marshall' -p 'badpassword'
FTP         192.168.0.10   21     192.168.0.10    [*] Banner: (vsFTPd 3.0.5)
FTP         192.168.0.10   21     192.168.0.10    [+] marshall:badpassword
```

## Specify Port

```bash
nxc ftp 192.168.0.10 -u 'marshall' -p 'badpassword' --port 2121
FTP         192.168.0.10   2121   192.168.0.10    [*] Banner: (vsFTPd 3.0.5)
FTP         192.168.0.10   2121   192.168.0.10    [+] marshall:badpassword
```
