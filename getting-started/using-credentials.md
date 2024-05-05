---
description: Using crendentials with NetExec
---

# Using Credentials

## Using Credentials

Every protocol supports using credentials in one form or another. For details on using credentials with a specific protocol, see the appropriate wiki section.

Generally speaking, to use credentials, you can run the following commands:

```
netexec <protocol> <target(s)> -u username -p password
```

{% hint style="success" %}
Code execution results in a (**Pwn3d!**) added after the login confirmation. With SMB protocol, most likely your compromised users are in the local administrators group.
{% endhint %}

| Protocol | See Pwn3d! in output                         |
| -------- | -------------------------------------------- |
| FTP      | No check                                     |
| SSH      | root (otherwise specific message)            |
| WINRM    | Code execution at least                      |
| LDAP     | Path to domain admin                         |
| SMB      | Most likely local admin :white\_check\_mark: |
| RDP      | Code execution at least                      |
| VNC      | Code execution at least                      |
| WMI      | Most likely local admin :white\_check\_mark: |

{% hint style="info" %}
When using usernames or passwords that contain special symbols (especially exclaimation points!), wrap them in single quotes to make your shell interpret them as a string.
{% endhint %}

Example:

```
netexec <protocol> <target(s)> -u username -p 'October2022!'
```

{% hint style="info" %}
Due to a [bug](https://bugs.python.org/issue9334) in Python's argument parsing library, credentials beginning with a dash (`-`) will throw an `expected at least one argument` error message. To get around this, specify the credentials by using the 'long' argument format (note the `=` sign):
{% endhint %}

`netexec <protocol> <target(s)> -u='-username' -p='-`October2022`'`

## Using a Credential Set From the Database

By specifying a credential ID (or multiple credential IDs) with the `-id` flag nxc will automatically pull that credential from the back-end database and use it to authenticate (saves a lot of typing):

```
netexec <protocol> <target(s)> -id <cred ID(s)>
```

## Multi-Domain Environment

You can use nxc with mulitple domain environment

```
netexec <protocol> <target(s)> -u FILE -p password
```

Where **FILE** is a file with usernames in this format

```
DOMAIN1\user
DOMAIN2\user
```

## Brute Forcing & Password Spraying

All protocols support brute-forcing and password spraying. For details on brute-forcing/password spraying with a specific protocol, see the appropriate wiki section.

By specifying a file or multiple values nxc will automatically brute-force logins for all targets using the specified protocol:

Examples:

```
netexec <protocol> <target(s)> -u username1 -p password1 password2
```

```
netexec <protocol> <target(s)> -u username1 username2 -p password1
```

```
netexec <protocol> <target(s)> -u ~/file_containing_usernames -p ~/file_containing_passwords
```

```
netexec <protocol> <target(s)> -u ~/file_containing_usernames -H ~/file_containing_ntlm_hashes
```

## Password Spraying Without Bruteforce

Can be usefull for protocols like WinRM and MSSQL. This option avoid the bruteforce when you use files (-u file -p file)

```
netexec <protocol> <target(s)> -u ~/file_containing_usernames -H ~/file_containing_ntlm_hashes --no-bruteforce
```

```
netexec <protocol> <target(s)> -u ~/file_containing_usernames -p ~/file_containing_passwords --no-bruteforce
```

```
user1 -> pass1
user2 -> pass2
```

{% hint style="info" %}
By default nxc will exit after a successful login is found. Using the --continue-on-success flag will continue spraying even after a valid password is found. Usefull for spraying a single password against a large user list.
{% endhint %}

```
netexec <protocol> <target(s)> -u ~/file_containing_usernames -H ~/file_containing_ntlm_hashes --no-bruteforce --continue-on-success
```
