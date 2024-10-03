# 🆕 Download and Upload Files from NFS Server

### Download File

Get a remote file(s) using NetExec. Example usage:

```
NetExec nfs <ip> --get-file /home/user/Desktop/test/test.txt test.txt

# Example Output                                                          
NFS         <ip>  <nfs_port>  <ip>   [*] Target supported NFS versions: (3, 4)
NFS         <ip>  <nfs_port>  <ip>   [*] Downloading /home/user/Desktop/test/roottest.txt to roottest.txt
NFS         <ip>  <nfs_port>  <ip>   File successfully downloaded to test.txt from /home/user/Desktop/test/test.txt

```

### Upload File

Get a remote file(s) using NetExec. Upload remote NFS file with chmod **777** permissions to the specified **folder**.
Example usage:

```
NetExec nfs <ip> --put-file test2.txt /home/user/Desktop/

# Example Output                                                          
NFS         <ip>  <nfs_port>  <ip>   [*] Target supported NFS versions: (3, 4)
NFS         <ip>  <nfs_port>  <ip>   [*] Uploading from test2.txt to /home/user/Desktop/NFSShare/
NFS         <ip>  <nfs_port>  <ip>   [*] Trying to create /home/user/Desktop/NFSShare/test2.txt
NFS         <ip>  <nfs_port>  <ip>   [+] test2.txt successfully created
NFS         <ip>  <nfs_port>  <ip>   [*] Trying to write data from test2.txt to /home/user/Desktop/NFSShare/
NFS         <ip>  <nfs_port>  <ip>   [+] Data from test2.txt successfully written to /home/user/Desktop/NFSShare/
NFS         <ip>  <nfs_port>  <ip>   File test2.txt successfully uploaded to /home/user/Desktop/NFSShare/

```

**If the local file already exists on the remote server, NetExec asks whether you want to overwrite it.**

```
NetExec nfs <ip> --put-file test2.txt /home/user/Desktop/

# Example Output  
NFS         <ip>  <nfs_port>  <ip>   [*] Target supported NFS versions: (3, 4)
NFS         <ip>  <nfs_port>  <ip>   [*] Uploading from test2.txt to /home/user/Desktop/NFSShare/
[!] test2.txt is already exist on /home/user/Desktop/NFSShare/. Do you want to overwrite it? [Y/n] Y
NFS         <ip>  <nfs_port>  <ip>   [*] test2.txt is already exist on /home/user/Desktop/NFSShare/. Trying to overwrite it...
NFS         <ip>  <nfs_port>  <ip>   [*] Trying to write data from test2.txt to /home/user/Desktop/NFSShare/
NFS         <ip>  <nfs_port>  <ip>   [+] Data from test2.txt successfully written to /home/user/Desktop/NFSShare/
NFS         <ip>  <nfs_port>  <ip>   File test2.txt successfully uploaded to /home/user/Desktop/NFSShare/
```

