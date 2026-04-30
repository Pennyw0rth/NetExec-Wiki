# Screenshot

## Screenshot and Save Location

You can take a screenshot of a VNC server's desktop after a successful authentication.

```bash
nxc vnc <ip> -u <username> -p <password> --screenshot
```

Expected Results:

```bash
nxc vnc 192.168.56.22 -u samwell.tarly -p Heartsbane --screenshot
VNC         192.168.56.22   5900   192.168.56.22    [*] RFB 3.8
VNC         192.168.56.22   5900   192.168.56.22    [+] :Heartsbane
VNC         192.168.56.22   5900   192.168.56.22    Screenshot saved /home/user/.nxc/screenshots/192.168.56.22_192.168.56.22_2026-04-09_000342.png
```

## Adjusting Screenshot Capture Time

Use `--screentime` to adjust the number of seconds to wait for the desktop image before capturing. 

```bash
nxc vnc <ip> -u <username> -p <password> --screenshot --screentime <seconds>
```
