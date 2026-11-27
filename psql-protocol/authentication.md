# Authentication

## Testing Credentials

```bash
nxc psql 10.10.1.10 -u postgres -p postgres
PSQL        10.10.1.10    5432   10.10.1.10     [*] PostgreSQL (version < 18) (TLS-supported:False)
PSQL        10.10.1.10    5432   10.10.1.10     [+] postgres:postgres (Pwn3d!) PostgreSQL 16.15 (Debian 16.15-1.pgdg13+2)
```

## Specify Port

```bash
nxc psql 10.10.1.10 -u postgres -p postgres --port 54322
PSQL        10.10.1.10    54322   10.10.1.10     [*] PostgreSQL (version < 18) (TLS-supported:True)
PSQL        10.10.1.10    54322   10.10.1.10     [+] postgres:postgres (Pwn3d!) PostgreSQL 16.15 (Debian 16.15-1.pgdg13+2)
```

## Specify Database

```bash
nxc psql 10.10.1.10 -u app_admin -p app_password --database app_db
PSQL        10.10.1.10    5432   10.10.1.10     [*] PostgreSQL (version < 18) (TLS-supported:False)
PSQL        10.10.1.10    5432   10.10.1.10     [+] app_admin:app_password (Pwn3d!) PostgreSQL 16.15 (Debian 16.15-1.pgdg13+2)
```
