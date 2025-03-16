# 🆕 Change User Password


The Module `change-password` can change a target user's password or NT hash, thanks to the contribution from [@FaganAfandiyev](https://x.com/kriyosthearcane).

Change the password of TargetUser to NewPassword

```
$ nxc smb <ip> -u user -p pass -M change-password -o USER=TargetUser NEWPASS=NewPassword
```
![Change Password](../.gitbook/assets/changepasswd.png)


Change the NT hash of TargetUser to 10C035D527CA60BE3ADF51996E7CD7E1

```
$ nxc smb <ip> -u user -p pass -M change-password -o USER=TargetUser NEWHASH=10C035D527CA60BE3ADF51996E7CD7E1
```
![Change Hash](../.gitbook/assets/changehash.png)
