# Authentication

## Testing credentials

You can use two methods to authenticate to MSSQL: `windows` or `local` (default: `windows`). To use local auth, add the following flag `--local-auth`

### **Windows auth**

1. With SMB port open

```bash
nxc mssql 10.10.10.52 -u james -p 'J@m3s_P@ssW0rd!'
```

1. With SMB port close, add the flag `-d DOMAIN`

```bash
nxc mssql 10.10.10.52 -u james -p 'J@m3s_P@ssW0rd!' -d HTB
```

Expected Results:

```bash
MSSQL       10.10.10.52     1433   MANTIS           [+] HTB\james:J@m3s_P@ssW0rd! 
```

### **Local auth**

```bash
nxc mssql 10.10.10.52 -u admin -p 'm$$ql_S@_P@ssW0rd!' --local-auth
```

Expected Results:

```bash
MSSQL       10.10.10.52     1433   None             [+] admin:m$$ql_S@_P@ssW0rd! (Pwn3d!)
```

### Specify Ports

```bash
nxc mssql 10.10.10.52 -u admin -p 'm$$ql_S@_P@ssW0rd!' --port 1434
```

### Execute as other user

```bash
nxc mssql 10.10.10.52 -u user -p 'Password123!' --impersonate 'sysadmin'
```
