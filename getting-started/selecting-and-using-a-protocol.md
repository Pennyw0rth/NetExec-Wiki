---
description: Selecting & Using a Protocol on NetExec
---

# Selecting & Using a Protocol

## Available Protocols

<pre><code><strong>smb
</strong><strong>ssh
</strong><strong>ldap
</strong><strong>ftp
</strong><strong>wmi
</strong><strong>winrm
</strong><strong>rdp
</strong><strong>vnc
</strong><strong>mssql
</strong><strong>nfs
</strong></code></pre>

Note that not all protocols support the same functionality, be sure to check each protocol's options

## Using Protocol Options

To view a protocols options, run: `nxc <protocol> --help`

Then use those options: `nxc <protocol> <protocol options>`

## Viewing Available Protocols

Running `nxc --help` will list general options and protocols that are available (Notice the 'protocols' section below):

```
#~ nxc --help
usage: nxc [-h] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL] [--no-progress] [--verbose] [--debug] [--version] {smb,ssh,ldap,ftp,wmi,winrm,rdp,vnc,mssql} ...

    <-- Banner -->   

options:
  -h, --help            show this help message and exit
  -t THREADS            set how many concurrent threads to use (default: 100)
  --timeout TIMEOUT     max timeout in seconds of each thread (default: None)
  --jitter INTERVAL     sets a random delay between each connection (default: None)
  --no-progress         Not displaying progress bar during scan
  --verbose             enable verbose output
  --debug               enable debug level information
  --version             Display nxc version

protocols:
  available protocols

  {smb,ssh,ldap,ftp,wmi,winrm,rdp,vnc,mssql}
    smb                 own stuff using SMB
    ssh                 own stuff using SSH
    ldap                own stuff using LDAP
    ftp                 own stuff using FTP
    wmi                 own stuff using WMI
    winrm               own stuff using WINRM
    rdp                 own stuff using RDP
    vnc                 own stuff using VNC
    mssql               own stuff using MSSQL
    nfs                 own stuff using NFS
```
