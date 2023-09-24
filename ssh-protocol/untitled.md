# Authentication

#### Testing credentials

```
#~ nxc ssh 192.168.1.0/24 -u user -p password
```

Expected Results:

```
SSH         127.0.0.1       22     127.0.0.1        [*] SSH-2.0-OpenSSH_8.2p1 Debian-4
SSH         127.0.0.1       22     127.0.0.1        [+] user:password
```

#### Specify Ports

```
#~ nxc http 192.168.1.0/24 --port 2222
```
