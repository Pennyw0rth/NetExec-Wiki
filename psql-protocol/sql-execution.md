---
description: Execute SQL command using NetExec
---

# SQL command

### Execute SQL commands

```bash
nxc psql 10.10.1.10 -u postgres -p postgres --query 'SELECT datname FROM pg_database;'
```

Expected Results:

```bash
PSQL        10.10.1.10    5432   10.10.1.10     [*] PostgreSQL (version < 18) (TLS-supported:False)
PSQL        10.10.1.10    5432   10.10.1.10     [+] postgres:postgres (Pwn3d!) PostgreSQL 16.15 (Debian 16.15-1.pgdg13+2)
PSQL        10.10.1.10    5432   10.10.1.10     --------------------
PSQL        10.10.1.10    5432   10.10.1.10     datname:template1
PSQL        10.10.1.10    5432   10.10.1.10     --------------------
PSQL        10.10.1.10    5432   10.10.1.10     datname:template0
PSQL        10.10.1.10    5432   10.10.1.10     --------------------
PSQL        10.10.1.10    5432   10.10.1.10     datname:postgres
```
