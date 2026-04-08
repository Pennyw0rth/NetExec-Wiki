# Authentication

### VNC Authentication

#### Testing credentials

Some VNC servers do not require a username. In such cases, the username field should be left empty, as illustrated in the results below.
```bash
nxc vnc 192.168.56.22 -u '' -p 'password'
```

Expected Results:
```bash
nxc vnc 192.168.56.22 -u '' -p 'password'
VNC         192.168.56.22   5900   192.168.56.22    [*] RFB 3.8
VNC         192.168.56.22   5900   192.168.56.22    [+] password
```

If the server supports username authentication, you can provide one:
```bash
nxc vnc 192.168.56.22 -u samwell.tarly -p Heartsbane
VNC         192.168.56.22   5900   192.168.56.22    [*] RFB 3.8
VNC         192.168.56.22   5900   192.168.56.22    [+] Heartsbane
```

#### Specify port

```bash
nxc vnc 192.168.56.22 --port 5901
```

#### Unauthenticated access

When the VNC server doesn't require authentication, the following output can be expected.
```bash
nxc vnc 192.168.56.22
VNC         192.168.56.22   5900   192.168.56.22    [*] RFB 3.8 (No Auth:True)
```

#### VNC sleep

Increase the VNC socket connection sleep interval to prevent rate limiting.
```bash
nxc vnc 192.168.56.22 --vnc-sleep 5
```
