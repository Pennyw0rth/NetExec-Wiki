# Linux Privilege Escalation Check (NetExec Module)

The `linux_privesc_check` module helps identify common privilege escalation paths on Linux hosts.  
It does **not exploit** vulnerabilities directly — it highlights possible escalation methods for further manual testing.  

---

## Module Options

- **NO_SUDO**: Skip `sudo -l` checks  
- **NO_GTF**: Skip GTFOBins lookups (no internet required)  
- **SHOW_ALL_SUID**: Show *all* SUID binaries (not just GTFOBins-exploitable ones)  
- **SHOW_ALL_CAPS**: Show *all* binaries with Linux capabilities  

---

## Attack Examples

### 1. Run Full Enumeration (default)
```bash
nxc ssh 192.168.56.101 -u alice -p alice123 -M linux_privesc_check
```

### 1.1 Expected Ouput
```bash
[linux_privesc_check] Running Linux privilege escalation checks...
[Kernel] Linux victim 5.15.0-86-generic #96-Ubuntu SMP x86_64 GNU/Linux
[User Info] uid=1000(alice) gid=1000(alice) groups=1000(alice)
[Sudo] Checking sudo -l...
    (ALL : ALL) NOPASSWD: /usr/bin/vim -> https://gtfobins.github.io/gtfobins/vim/#sudo
[SUID] Checking for exploitable SUID binaries...
Exploit SUID: /usr/bin/find -> https://gtfobins.github.io/gtfobins/find/#suid
[Capabilities] Checking for binaries with capabilities...
Capability: /usr/bin/python3.8 = cap_setuid+ep -> https://gtfobins.github.io/gtfobins/python/#capabilities
```

### 2. Skip Sudo (no sudo -l)
```bash
nxc ssh 192.168.56.101 -u alice -p alice123 -M linux_privesc_check -o NO_SUDO=true
```

### 2.1 Expected Output
```bash
[linux_privesc_check] Skipping sudo -l enumeration (NO_SUDO)
[SUID] Checking for exploitable SUID binaries...
...
```

### 3. Skip GTFOBins Lookup
```bash
nxc ssh 192.168.56.101 -u alice -p alice123 -M linux_privesc_check -o NO_GTF=true
```

### 3.1 Expected Output
```bash
[linux_privesc_check] Skipping GTFOBins lookups (NO_GTF)
[SUID] Checking for exploitable SUID binaries...
Exploit SUID: /usr/bin/passwd
[Capabilities] Checking for binaries with capabilities...
Capability: /usr/bin/tar = cap_dac_read_search+ep
```

### 4. Show all SUID Binaries
```bash
nxc ssh 192.168.56.101 -u alice -p alice123 -M linux_privesc_check -o SHOW_ALL_SUID=true
```

### 4.1 Expected Output
```bash
[SUID] Checking for exploitable SUID binaries...
Exploit SUID: /usr/bin/passwd
Exploit SUID: /usr/bin/chsh
Exploit SUID: /usr/bin/su
...
```

### 5. Show all Capabilites
```bash
nxc ssh 192.168.56.101 -u alice -p alice123 -M linux_privesc_check -o SHOW_ALL_CAPS=true
```

### 5.1 Expected Output
```bash
[Capabilities] Checking for binaries with capabilities...
Capability: /usr/bin/ping = cap_net_raw+ep
Capability: /usr/bin/python3.8 = cap_setuid+ep
...
```