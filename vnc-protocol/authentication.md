# Authentication

### VNC Authentication

#### Testing credentials
Some VNC servers do not require a username. In such cases, the username field should be left empty, as illustrated in the results below.
```bash
nxc vnc <ip> -u '' -p 'password'
```

Expected Results:
```bash
nxc vnc <ip> -u '' -p 'password'
VNC         <ip>   5900   <ip>    [*] RFB 3.8
VNC         <ip>   5900   <ip>    [+] password (Pwn3d!)
```

#### Specify port
```bash
nxc vnc <ip> --port <port>
```

#### Unauthenticated access
When the VNC server doesn't require authentication, the following output can be expected.
```bash
nxc vnc <ip>
VNC         <ip>   5900   <ip>    [*] RFB 3.8 (No Auth:True)
```

#### VNC sleep
Increase the VNC socket connection sleep interval to prevent rate limiting.
```bash
nxc vnc <ip> --vnc-sleep 5
```
