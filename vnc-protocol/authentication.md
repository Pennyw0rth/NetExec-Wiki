# Authentication

## Testing credentials

VNC servers do not require a username. As such, the username field is omitted and not sent.

```bash
nxc vnc <ip> -u '' -p <password>
```

Expected Results:

```bash
nxc vnc 192.168.56.22 -u '' -p 'badpassword'
VNC         192.168.56.22   5900   192.168.56.22    [*] RFB 3.8
VNC         192.168.56.22   5900   192.168.56.22    [+] badpassword (Pwn3d!)
```

## Unauthenticated access

When the VNC server doesn't require authentication, the following output can be expected.

```bash
nxc vnc 192.168.56.22
VNC         192.168.56.22   5900   192.168.56.22    [*] RFB 3.8 (No Auth:True)
```

## Specify port

```bash
nxc vnc 192.168.56.22 --port 5901
VNC         192.168.56.22   5901   192.168.56.22    [*] RFB 3.8 (No Auth:True)
```

## VNC sleep

Increase the VNC socket connection sleep interval to prevent rate limiting.

```bash
nxc vnc <ip> --vnc-sleep <seconds>
```
