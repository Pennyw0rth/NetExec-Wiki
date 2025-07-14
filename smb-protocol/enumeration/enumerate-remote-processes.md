# Enumerate remote processes

One thing that's to know when pentesting is whether or not a specific process is being run on the server you are targeting. This can now be done via the following option:

```bash
nxc smb 192.168.1.0/24 -u user -p 'PASSWORDHERE' --tasklist
```

Note that by default, NXC will print the entire list of processes running on the remote host. If you want to look for a specific process (hello there keepass.exe) you can fill the process name as a parameter:

```bash
nxc smb 192.168.1.0/24 -u user -p 'PASSWORDHERE' --tasklist keepass.exe
```

# Killing remote processes

We have also added an option allowing you to specify either a process name to remotely kill or a specific PID:

```bash
nxc smb 192.168.1.0/24 -u user -p 'PASSWORDHERE' --taskkill PID
nxc smb 192.168.1.0/24 -u user -p 'PASSWORDHERE' --taskkill process_name.exe
```