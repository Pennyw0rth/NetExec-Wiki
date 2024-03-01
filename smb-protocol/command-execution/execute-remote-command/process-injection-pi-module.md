# Process Injection (pi module)

{% hint style="warning" %} You need at least local admin privilege on the remote target {% endhint %}

The "pi" module accesses the process of a user with an active session on a Windows system using the Process Injection method to execute commands with the privileges of the target user (requires SYSTEM privileges).

It allows impersonating authorized domain users in Active Directory.

It works more stable for Server 2016/Win10 and above.

```
#~ NetExec <IP> -u username -p password -M pi -o PID=<target_process_pid> EXEC=<command>
```

For more information on the creation of the `pi` module, see the developer's blog post here: [https://medium.com/@mehmetcantopal/development-and-implementation-of-the-pi-smb-module-for-netexec-crackmapexec-83eac92ded8f](https://medium.com/@mehmetcantopal/development-and-implementation-of-the-pi-smb-module-for-netexec-crackmapexec-83eac92ded8f)
