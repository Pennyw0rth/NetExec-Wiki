# Enumerate host with SMB signing not required

Maps the network of live hosts and saves a list of only the hosts that **don't** require SMB signing.\
List format is one IP per line

```
#~ nxc smb 192.168.1.0/24 --gen-relay-list relaylistOutputFilename.txt
```

Expected Results:

```
SMB         192.168.1.101    445    DC2012A          [*] Windows Server 2012 R2 Standard 9600 x64 (name:DC2012A) (domain:OCEAN) (signing:True) (SMBv1:True)
SMB         192.168.1.102    445    DC2012B          [*] Windows Server 2012 R2 Standard 9600 x64 (name:DC2012B) (domain:EARTH) (signing:True) (SMBv1:True)
SMB         192.168.1.111    445    SERVER1          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:SERVER1) (domain:PACIFIC) (signing:False) (SMBv1:True)
SMB         192.168.1.117    445    WIN10DESK1       [*] WIN10DESK1 x64 (name:WIN10DESK1) (domain:OCEAN) (signing:False) (SMBv1:True)
...SNIP...

#~ cat relaylistOutputFilename.txt
192.168.1.111
192.168.1.117
```

{% embed url="https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html" %}

### Alternative with nmap

You can also list only the hosts that **don't** require SMB signing using nmap

```
nmap --script smb-security-mode.nse,smb2-security-mode.nse -p445 127.0.0.1
```
