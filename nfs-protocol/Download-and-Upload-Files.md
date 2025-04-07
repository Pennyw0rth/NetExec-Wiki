# Download and Upload Files

{% hint style="info" %}
For both `--get-file` and `--put-file` you need to specify the export share with `--share` if you do not want to use the root fs escape method (see [escape to root file system](escape-to-root-file-system.md)).
{% endhint %}

Example usage:

```
# Share name is "/home/user/Desktop/NFSShare"
nxc nfs <ip> --share /home/user/Desktop/NFSShare/ --get-file as.txt as.txt

# Example Output                                                          
NFS         <ip>  <nfs_port>  <ip>   [*] Supported NFS versions: (3, 4) (root escape:True)
NFS         <ip>  <nfs_port>  <ip>   [*] Downloading as.txt to as.txt
NFS         <ip>  <nfs_port>  <ip>   File successfully downloaded from as.txt to as.txt

nxc nfs <ip> --share /home/user/Desktop/NFSShare/ --put-file aa.txt aa.txt

# Example Output                                                          
NFS         <ip>  <nfs_port>  <ip>   [*] Supported NFS versions: (3, 4) (root escape:True)
NFS         <ip>  <nfs_port>  <ip>   [*] Uploading from aa.txt to aa.txt
NFS         <ip>  <nfs_port>  <ip>   [*] Trying to create aa.txtaa.txt
NFS         <ip>  <nfs_port>  <ip>   [+] aa.txt successfully created
NFS         <ip>  <nfs_port>  <ip>   [+] Data from aa.txt successfully written to aa.txt with permissions 777
NFS         <ip>  <nfs_port>  <ip>   File aa.txt successfully uploaded to aa.txt
```

### Download File

Example usage:

```
nxc nfs <ip> --get-file /home/user/Desktop/test/test.txt test.txt

# Example Output                                                          
NFS         <ip>  <nfs_port>  <ip>   [*] Supported NFS versions: (3, 4) (root escape:True)
NFS         <ip>  <nfs_port>  <ip>   [*] Downloading /home/user/Desktop/test/roottest.txt to roottest.txt
NFS         <ip>  <nfs_port>  <ip>   File successfully downloaded to test.txt from /home/user/Desktop/test/test.txt

```

### Upload File

Uploaded files are created with chmod **777** permissions. If folders in the specified path do not exist yet, they will be created as well. Example usage:

```
nxc nfs <ip> --put-file test2.txt /home/user/Desktop/

# Example Output                                                          
NFS         <ip>  <nfs_port>  <ip>   [*] Supported NFS versions: (3, 4) (root escape:True)
NFS         <ip>  <nfs_port>  <ip>   [*] Uploading from test2.txt to /home/user/Desktop/NFSShare/
NFS         <ip>  <nfs_port>  <ip>   [*] Trying to create /home/user/Desktop/NFSShare/test2.txt
NFS         <ip>  <nfs_port>  <ip>   [+] test2.txt successfully created
NFS         <ip>  <nfs_port>  <ip>   [*] Trying to write data from test2.txt to /home/user/Desktop/NFSShare/
NFS         <ip>  <nfs_port>  <ip>   [+] Data from test2.txt successfully written to /home/user/Desktop/NFSShare/
NFS         <ip>  <nfs_port>  <ip>   File test2.txt successfully uploaded to /home/user/Desktop/NFSShare/

```

**If the local file already exists on the remote server, NetExec asks whether you want to overwrite it.**

```
nxc nfs <ip> --put-file test2.txt /home/user/Desktop/

# Example Output  
NFS         <ip>  <nfs_port>  <ip>   [*] Supported NFS versions: (3, 4) (root escape:True)
NFS         <ip>  <nfs_port>  <ip>   [*] Uploading from test2.txt to /home/user/Desktop/NFSShare/
[!] test2.txt already exists on /home/user/Desktop/NFSShare/. Do you want to overwrite it? [Y/n] Y
NFS         <ip>  <nfs_port>  <ip>   [*] test2.txt already exists on /home/user/Desktop/NFSShare/. Trying to overwrite it...
NFS         <ip>  <nfs_port>  <ip>   [*] Trying to write data from test2.txt to /home/user/Desktop/NFSShare/
NFS         <ip>  <nfs_port>  <ip>   [+] Data from test2.txt successfully written to /home/user/Desktop/NFSShare/
NFS         <ip>  <nfs_port>  <ip>   File test2.txt successfully uploaded to /home/user/Desktop/NFSShare/
```
