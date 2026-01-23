# RPC Enumeration

This document covers all enumeration capabilities of the RPC protocol.

## Server Information

### --server-info

Query server information including name, version, and type.

**rpcclient equivalent:** `srvinfo`

```bash
nxc rpc 192.168.1.100 -u user -p pass --server-info
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [*] Windows 10 / Server 2019 Build 17763
RPC  192.168.1.100  445  DC01  [+] domain\user:pass
RPC  192.168.1.100  445  DC01  Server Name: DC01
RPC  192.168.1.100  445  DC01  Server Comment: 
RPC  192.168.1.100  445  DC01  Server Version: 10.0
RPC  192.168.1.100  445  DC01  Server Type: 0x84102b
```

---

## Domain Enumeration

### --enum-domains

Enumerate all domains available on the server.

**rpcclient equivalent:** `enumdomains`

```bash
nxc rpc 192.168.1.100 -u user -p pass --enum-domains
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 2 domain(s)
RPC  192.168.1.100  445  DC01    CONTOSO
RPC  192.168.1.100  445  DC01    Builtin
```

---

### --enum-trusts

Enumerate trusted domains. Critical for identifying lateral movement paths in multi-domain environments.

**rpcclient equivalent:** `enumtrust`

```bash
nxc rpc 192.168.1.100 -u user -p pass --enum-trusts
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 2 trusted domain(s)
RPC  192.168.1.100  445  DC01  Domain: child.contoso.local (CHILD)
RPC  192.168.1.100  445  DC01    SID: S-1-5-21-1234567890-1234567890-1234567890
RPC  192.168.1.100  445  DC01    Direction: Bidirectional | Type: Uplevel
RPC  192.168.1.100  445  DC01    Attributes: WITHIN_FOREST (0x20)
```

**Trust Direction Values:**
- `Disabled` (0) - Trust is disabled
- `Inbound` (1) - One-way trust, other domain trusts this domain
- `Outbound` (2) - One-way trust, this domain trusts the other
- `Bidirectional` (3) - Two-way trust

**Trust Attributes:**
- `NON_TRANSITIVE` - Trust cannot be used transitively
- `UPLEVEL_ONLY` - Only Windows 2000+ can use this trust
- `QUARANTINED` - Domain is quarantined
- `FOREST_TRANSITIVE` - Trust is forest-wide
- `WITHIN_FOREST` - Trust is within the same forest
- `TREAT_AS_EXTERNAL` - Treat as external trust

---

### --domain-info

Query detailed domain information including user/group counts.

**rpcclient equivalent:** `querydominfo`

```bash
nxc rpc 192.168.1.100 -u user -p pass --domain-info
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  Domain: CONTOSO
RPC  192.168.1.100  445  DC01  Total Users: 150
RPC  192.168.1.100  445  DC01  Total Groups: 25
RPC  192.168.1.100  445  DC01  Total Aliases: 10
RPC  192.168.1.100  445  DC01  Sequence: 1234567
RPC  192.168.1.100  445  DC01  Force Logoff: -1
RPC  192.168.1.100  445  DC01  Domain Server State: 1
RPC  192.168.1.100  445  DC01  Server Role: 3
```

---

### --pass-pol

Query domain password policy including minimum length, history, and lockout settings.

**rpcclient equivalent:** `getdompwinfo`

```bash
nxc rpc 192.168.1.100 -u user -p pass --pass-pol
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  Min password length: 7
RPC  192.168.1.100  445  DC01  Password history length: 24
RPC  192.168.1.100  445  DC01  Password properties: 0x00000001
RPC  192.168.1.100  445  DC01  Lockout threshold: 5
RPC  192.168.1.100  445  DC01  Lockout duration: -18000000000
RPC  192.168.1.100  445  DC01  Lockout window: -18000000000
```

---

## User Enumeration

### --users

Enumerate all domain users with their RIDs.

**rpcclient equivalent:** `enumdomusers`

```bash
nxc rpc 192.168.1.100 -u user -p pass --users
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 150 user(s)
RPC  192.168.1.100  445  DC01  user:[Administrator] rid:[0x1f4]
RPC  192.168.1.100  445  DC01  user:[Guest] rid:[0x1f5]
RPC  192.168.1.100  445  DC01  user:[krbtgt] rid:[0x1f6]
RPC  192.168.1.100  445  DC01  user:[john.doe] rid:[0x450]
```

---

### --querydispinfo

Query user display information including descriptions and full names.

**rpcclient equivalent:** `querydispinfo`

```bash
nxc rpc 192.168.1.100 -u user -p pass --querydispinfo
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 150 user(s)
RPC  192.168.1.100  445  DC01  index: 1 RID: 0x1f4 acb: 0x210 name: Administrator desc: Built-in admin
RPC  192.168.1.100  445  DC01  index: 2 RID: 0x450 acb: 0x210 name: john.doe desc: IT Department
```

---

### --rid-brute [MAX_RID]

Brute force RIDs to enumerate users and groups. Works with anonymous access on misconfigured systems.

**Default:** 4000

```bash
# Anonymous RID cycling
nxc rpc 192.168.1.100 -u '' -p '' --rid-brute

# Custom max RID
nxc rpc 192.168.1.100 -u user -p pass --rid-brute 10000
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  S-1-5-21-xxx-500 -> Administrator (User)
RPC  192.168.1.100  445  DC01  S-1-5-21-xxx-501 -> Guest (User)
RPC  192.168.1.100  445  DC01  S-1-5-21-xxx-512 -> Domain Admins (Group)
RPC  192.168.1.100  445  DC01  S-1-5-21-xxx-513 -> Domain Users (Group)
RPC  192.168.1.100  445  DC01  [+] Found 25 principal(s)
```

---

## Group Enumeration

### --groups

Enumerate domain groups.

**rpcclient equivalent:** `enumdomgroups`

```bash
nxc rpc 192.168.1.100 -u user -p pass --groups
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 15 group(s)
RPC  192.168.1.100  445  DC01  group:[Domain Admins] rid:[0x200]
RPC  192.168.1.100  445  DC01  group:[Domain Users] rid:[0x201]
RPC  192.168.1.100  445  DC01  group:[Domain Computers] rid:[0x203]
```

---

### --local-groups

Enumerate local/alias groups (Builtin groups like Administrators, Users, etc.).

**rpcclient equivalent:** `enumalsgroups builtin`

```bash
nxc rpc 192.168.1.100 -u user -p pass --local-groups
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 20 alias group(s)
RPC  192.168.1.100  445  DC01  group:[Administrators] rid:[0x220]
RPC  192.168.1.100  445  DC01  group:[Users] rid:[0x221]
RPC  192.168.1.100  445  DC01  group:[Remote Desktop Users] rid:[0x22b]
```

---

## Share Enumeration

### --shares

Enumerate all shares on the server.

**rpcclient equivalent:** `netshareenumall`

```bash
nxc rpc 192.168.1.100 -u user -p pass --shares
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 5 share(s)
RPC  192.168.1.100  445  DC01  netname: ADMIN$ | type: Disk | remark: Remote Admin
RPC  192.168.1.100  445  DC01  netname: C$ | type: Disk | remark: Default share
RPC  192.168.1.100  445  DC01  netname: IPC$ | type: IPC | remark: Remote IPC
RPC  192.168.1.100  445  DC01  netname: NETLOGON | type: Disk | remark: Logon server share
RPC  192.168.1.100  445  DC01  netname: SYSVOL | type: Disk | remark: Logon server share
```

---

### --share SHARE

Get detailed information about a specific share. Supports share names with spaces using quotes.

**rpcclient equivalent:** `netsharegetinfo`

```bash
# Simple share name
nxc rpc 192.168.1.100 -u user -p pass --share SYSVOL

# Share name with spaces
nxc rpc 192.168.1.100 -u user -p pass --share 'Password Audit'
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  netname: SYSVOL
RPC  192.168.1.100  445  DC01  type: Disk (0x0)
RPC  192.168.1.100  445  DC01  remark: Logon server share
RPC  192.168.1.100  445  DC01  permissions: 0
RPC  192.168.1.100  445  DC01  max_uses: -1
RPC  192.168.1.100  445  DC01  current_uses: 5
RPC  192.168.1.100  445  DC01  path: C:\Windows\SYSVOL\sysvol
```

---

## Session and Connection Enumeration

### --sessions

Enumerate active sessions on the server.

**rpcclient equivalent:** `netsessenum`

```bash
nxc rpc 192.168.1.100 -u user -p pass --sessions
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 3 session(s)
RPC  192.168.1.100  445  DC01  cname: \\192.168.1.50 | username: john.doe | time: 3600
RPC  192.168.1.100  445  DC01  cname: \\192.168.1.51 | username: admin | time: 7200
```

---

### --connections

Enumerate connections to shares.

**rpcclient equivalent:** `netconnenum`

```bash
nxc rpc 192.168.1.100 -u user -p pass --connections
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  share: IPC$ | user: john.doe | client: 192.168.1.50 | opens: 2 | time: 3600s
RPC  192.168.1.100  445  DC01  share: SYSVOL | user: admin | client: 192.168.1.51 | opens: 1 | time: 120s
RPC  192.168.1.100  445  DC01  [+] Found 2 connection(s)
```

---

## Combining Flags

Multiple enumeration flags can be combined:

```bash
# Enumerate users, groups, and shares in one command
nxc rpc 192.168.1.100 -u user -p pass --users --groups --shares

# Full enumeration
nxc rpc 192.168.1.100 -u user -p pass --server-info --domain-info --users --groups --shares --pass-pol
```
