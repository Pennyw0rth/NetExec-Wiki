# 🆕 Enumerating NFS

All flags work anonymously right now.

### Enumerate NFS Servers

Detect remote NFS server and versions.

```
NetExec nfs <ip> 

# Example Output                                                          
NFS         <ip>  <nfs_port>  <ip>   [*] Target supported NFS versions: (3, 4)

```

### Enumerate NFS Shares


Using the flag `--shares` for enumerating NFS shares. Output shows target `UID, Permissions, Storage Usage, Access List`.

```
NetExec nfs <ip> --shares

# Example Output
NFS         <ip>  <nfs_port>  <ip>   [*] Target supported NFS versions: (3, 4)
NFS         <ip>  <nfs_port>  <ip>   [*] Enumerating NFS Shares
NFS         <ip>  <nfs_port>  <ip>   UID        Perms    Storage Usage    Share                          Access List    
NFS         <ip>  <nfs_port>  <ip>   ---        -----    -------------    -----                          -----------    
NFS         <ip>  <nfs_port>  <ip>   2000       rw-      9.2GB/19.5GB    /home/user/Desktop/test        *              
NFS         <ip>  <nfs_port>  <ip>   1000       rw-      9.2GB/19.5GB    /home/user/Desktop/NFSShare    192.168.0.0/24
```

### Enumerate the File on NFS Shares

Enumerating all files and folders recursively with `--enum-shares`. Output shows target `UID, Permissions, File Size, File Path, Access List`.

```
NetExec nfs <ip> --enum-shares

# Example Output
NFS         <ip>  <nfs_port>  <ip>   [*] Target supported NFS versions: (3, 4)
NFS         <ip>  <nfs_port>  <ip>   [*] Enumerating NFS Shares Directories
NFS         <ip>  <nfs_port>  <ip>   [+] /home/user/Desktop/test
NFS         <ip>  <nfs_port>  <ip>   UID        Perms    File Size      File Path                                     Access List    
NFS         <ip>  <nfs_port>  <ip>   ---        -----    ---------      ---------                                     -----------    
NFS         <ip>  <nfs_port>  <ip>   1000       r--      21.0B          /home/user/Desktop/test/test.txt              *              
NFS         <ip>  <nfs_port>  <ip>   0          r--      9.0B           /home/user/Desktop/test/test2.txt             *              
NFS         <ip>  <nfs_port>  <ip>   [+] /home/user/Desktop/NFSShare
NFS         <ip>  <nfs_port>  <ip>   UID        Perms    File Size      File Path                                     Access List    
NFS         <ip>  <nfs_port>  <ip>   ---        -----    ---------      ---------                                     -----------    
NFS         <ip>  <nfs_port>  <ip>   1000       rw-      6.0B           /home/user/Desktop/NFSShare/test.txt          192.168.38.0/24
NFS         <ip>  <nfs_port>  <ip>   1000       rw-      7.0B           /home/user/Desktop/NFSShare/NFS2/test2.txt    192.168.38.0/24,
NFS         <ip>  <nfs_port>  <ip>   1000       rwx      27.0B          /home/user/Desktop/NFSShare/test3.txt         192.168.38.0/24

```