# MSSQL upload/download

### Download / Upload MSSQL file

```
nxc mssql 10.10.10.52 -u admin -p 'm$$ql_S@_P@ssW0rd!' --put-file  --put-file /tmp/users C:\\Windows\\Temp\\whoami.txt
```

Expected Results:

```
$ poetry run NetExec mssql 192.168.212.134 -u administrator -p October2022 --put-file /tmp/users C:\\Windows\\Temp\\whoami.txt
MSSQL       192.168.212.134 1433   DC01             [*] Windows 10.0 Build 20348 (name:DC01) (domain:poudlard.wizard)
MSSQL       192.168.212.134 1433   DC01             [+] poudlard.wizard\administrator:October2022 (Pwn3d!)
MSSQL       192.168.212.134 1433   DC01             [*] Copy /tmp/users to C:\Windows\Temp\whoami.txt
MSSQL       192.168.212.134 1433   DC01             [*] Size is 23 bytes
MSSQL       192.168.212.134 1433   DC01             [+] File has been uploaded on the remote machine
```

```
nxc mssql 10.10.10.52 -u admin -p 'm$$ql_S@_P@ssW0rd!' --get-file C:\\Windows\\Temp\\whoami.txt /tmp/file
```

Expected Results:

```
$ poetry run NetExec mssql 192.168.212.134 -u administrator -p October2022 --get-file C:\\Windows\\Temp\\whoami.txt /tmp/users-t
MSSQL       192.168.212.134 1433   DC01             [*] Windows 10.0 Build 20348 (name:DC01) (domain:poudlard.wizard)
MSSQL       192.168.212.134 1433   DC01             [+] poudlard.wizard\administrator:October2022 (Pwn3d!)
MSSQL       192.168.212.134 1433   DC01             [*] Copy C:\Windows\Temp\whoami.txt to /tmp/users-t
MSSQL       192.168.212.134 1433   DC01             [+] File C:\Windows\Temp\whoami.txt was transferred to /tmp/users-t
```
