# Lookup Operations

This document covers SID, name, and domain lookup operations available in the RPC protocol.

## Overview

Lookup operations allow resolving between SIDs (Security Identifiers) and account names, which is essential for understanding permissions, ACLs, and account relationships in Windows environments.

---

## Name Lookups

### --lookup-names NAMES

Look up one or more account names to get their RIDs via SAMR.

**rpcclient equivalent:** `lookupnames`

```bash
# Single name
nxc rpc 192.168.1.100 -u user -p pass --lookup-names Administrator

# Multiple names (comma-separated)
nxc rpc 192.168.1.100 -u user -p pass --lookup-names "Administrator,Guest,krbtgt"
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  Administrator -> S-1-5-21-xxx-500 (User)
RPC  192.168.1.100  445  DC01  Guest -> S-1-5-21-xxx-501 (User)
RPC  192.168.1.100  445  DC01  krbtgt -> S-1-5-21-xxx-502 (User)
```

**Type Values:**
| Type | Value | Description |
|------|-------|-------------|
| User | 1 | User account |
| Group | 2 | Domain group |
| Alias | 4 | Local/alias group |
| WellKnown | 5 | Well-known SID |
| Computer | 9 | Computer account |

---

### --lsa-lookup-names NAMES

Look up names via LSA (Local Security Authority). Can resolve names across trusted domains.

**rpcclient equivalent:** `lookupnames`

```bash
# Single name
nxc rpc 192.168.1.100 -u user -p pass --lsa-lookup-names Administrator

# Multiple names
nxc rpc 192.168.1.100 -u user -p pass --lsa-lookup-names "DOMAIN\\Administrator,Everyone,BUILTIN\\Administrators"
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  Administrator -> CONTOSO\Administrator S-1-5-21-xxx-500 (User)
RPC  192.168.1.100  445  DC01  Everyone -> Everyone S-1-1-0 (WellKnown)
```

---

## SID Lookups

### --sid-lookup SID

Look up a SID to get the account name.

**rpcclient equivalent:** `lookupsids`

```bash
# Domain SID
nxc rpc 192.168.1.100 -u user -p pass --sid-lookup S-1-5-21-1234567890-1234567890-1234567890-500

# Well-known SID
nxc rpc 192.168.1.100 -u user -p pass --sid-lookup S-1-5-32-544

# Everyone SID
nxc rpc 192.168.1.100 -u user -p pass --sid-lookup S-1-1-0
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  S-1-5-21-xxx-500 -> CONTOSO\Administrator (type 1)
```

---

### --lsa-lookup-sids SIDS

Look up one or more SIDs via LSA to get account names.

**rpcclient equivalent:** `lookupsids`

```bash
# Single SID
nxc rpc 192.168.1.100 -u user -p pass --lsa-lookup-sids S-1-5-21-xxx-500

# Multiple SIDs (comma-separated)
nxc rpc 192.168.1.100 -u user -p pass --lsa-lookup-sids "S-1-5-21-xxx-500,S-1-5-21-xxx-512,S-1-1-0"
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  S-1-5-21-xxx-500 -> CONTOSO\Administrator (User)
RPC  192.168.1.100  445  DC01  S-1-5-21-xxx-512 -> CONTOSO\Domain Admins (Group)
RPC  192.168.1.100  445  DC01  S-1-1-0 -> Everyone (WellKnown)
```

---

## SAM Lookups

### --sam-lookup domain|builtin NAMES

Look up names in either the domain or builtin SAM database.

**rpcclient equivalent:** `samlookupnames`

```bash
# Look up in domain database
nxc rpc 192.168.1.100 -u user -p pass --sam-lookup domain "Administrator,Domain Admins"

# Look up in builtin database
nxc rpc 192.168.1.100 -u user -p pass --sam-lookup builtin "Administrators,Users"
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  Administrator S-1-5-21-xxx-500 (User: 1)
RPC  192.168.1.100  445  DC01  Domain Admins S-1-5-21-xxx-512 (Group: 2)
```

---

## Domain Lookups

### --lookup-domain DOMAIN

Look up a domain name to get its SID.

**rpcclient equivalent:** `lookupdomain`

```bash
nxc rpc 192.168.1.100 -u user -p pass --lookup-domain CONTOSO
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  Domain CONTOSO -> SID S-1-5-21-1234567890-1234567890-1234567890
```

---

## Well-Known SIDs Reference

### Universal Well-Known SIDs

| SID | Name | Description |
|-----|------|-------------|
| S-1-0-0 | Null SID | No security principal |
| S-1-1-0 | Everyone | All users |
| S-1-2-0 | Local | Local logon |
| S-1-3-0 | Creator Owner | Placeholder for object creator |
| S-1-3-1 | Creator Group | Placeholder for creator's group |

### NT Authority SIDs (S-1-5-x)

| SID | Name | Description |
|-----|------|-------------|
| S-1-5-1 | Dialup | Dial-up connection users |
| S-1-5-2 | Network | Network logon users |
| S-1-5-3 | Batch | Batch job users |
| S-1-5-4 | Interactive | Interactive logon users |
| S-1-5-6 | Service | Service accounts |
| S-1-5-7 | Anonymous | Anonymous logon |
| S-1-5-9 | Enterprise Domain Controllers | All DCs in forest |
| S-1-5-10 | Principal Self | Placeholder for self |
| S-1-5-11 | Authenticated Users | All authenticated users |
| S-1-5-13 | Terminal Server Users | Terminal Services users |
| S-1-5-18 | Local System | SYSTEM account |
| S-1-5-19 | Local Service | LOCAL SERVICE account |
| S-1-5-20 | Network Service | NETWORK SERVICE account |

### Builtin Domain SIDs (S-1-5-32-x)

| SID | RID | Name |
|-----|-----|------|
| S-1-5-32-544 | 544 | Administrators |
| S-1-5-32-545 | 545 | Users |
| S-1-5-32-546 | 546 | Guests |
| S-1-5-32-547 | 547 | Power Users |
| S-1-5-32-548 | 548 | Account Operators |
| S-1-5-32-549 | 549 | Server Operators |
| S-1-5-32-550 | 550 | Print Operators |
| S-1-5-32-551 | 551 | Backup Operators |
| S-1-5-32-552 | 552 | Replicators |
| S-1-5-32-554 | 554 | Pre-Windows 2000 Compatible Access |
| S-1-5-32-555 | 555 | Remote Desktop Users |
| S-1-5-32-556 | 556 | Network Configuration Operators |

### Domain-Specific SIDs (S-1-5-21-domain-x)

| RID | Name |
|-----|------|
| 500 | Administrator |
| 501 | Guest |
| 502 | krbtgt |
| 512 | Domain Admins |
| 513 | Domain Users |
| 514 | Domain Guests |
| 515 | Domain Computers |
| 516 | Domain Controllers |
| 517 | Cert Publishers |
| 518 | Schema Admins |
| 519 | Enterprise Admins |
| 520 | Group Policy Creator Owners |
| 521 | Read-only Domain Controllers |
| 522 | Cloneable Domain Controllers |
| 525 | Protected Users |
| 526 | Key Admins |
| 527 | Enterprise Key Admins |

---

## Practical Use Cases

### Analyzing ACL Entries

When you encounter a SID in an ACL, resolve it to understand who has access:

```bash
# Found in ACL: S-1-5-21-xxx-1105
nxc rpc target -u user -p pass --sid-lookup S-1-5-21-xxx-1105
# Output: svc_backup (User)
```

### Cross-Domain Trust Analysis

```bash
# Get domain SID
nxc rpc target -u user -p pass --lookup-domain CHILD

# Look up accounts in trusted domain
nxc rpc target -u user -p pass --lsa-lookup-sids S-1-5-21-CHILD_DOMAIN_SID-512
```

### Finding Account RIDs for RID Brute

```bash
# Look up known accounts to get domain SID pattern
nxc rpc target -u user -p pass --lookup-names Administrator
# Output: S-1-5-21-1234567890-1234567890-1234567890-500

# Now brute force other RIDs
nxc rpc target -u user -p pass --rid-brute 2000
```

### Mapping Service Accounts

```bash
# Look up service accounts found in SPNs
nxc rpc target -u user -p pass --lookup-names "svc_sql,svc_backup,svc_http"
```

### Verify Account Existence

```bash
# Check if an account exists before attempting password spray
nxc rpc target -u user -p pass --lookup-names "potential_user"
```
