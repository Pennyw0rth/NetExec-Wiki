# Authentication

## Testing credentials

You can use two methods to authenticate to the WMI: `windows` or `local` (default: `windows`). To use local auth, add the following flag `--local-auth`

### **Windows auth**

- With SMB port open

```
#~ nxc wmi 10.10.10.52 -u james -p 'J@m3s_P@ssW0rd!'
```

- With SMB port close, add the flag `-d DOMAIN`

```
#~ nxc wmi 10.10.10.52 -u james -p 'J@m3s_P@ssW0rd!' -d HTB
```

Expected Results:

```
WMI       10.10.10.52     1433   MANTIS           [+] HTB\james:J@m3s_P@ssW0rd! 
```

### **Local auth**

```
#~ nxc wmi 10.10.10.52 -u admin -p 'admin' --local-auth
```
