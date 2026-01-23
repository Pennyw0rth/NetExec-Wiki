# LSA Operations

This document covers Local Security Authority (LSA) operations available in the RPC protocol.

## Overview

LSA operations interact with the Local Security Authority subsystem, which handles security policy, authentication, and SID management on Windows systems.

---

## Basic LSA Query

### --lsa-query

Query basic LSA information including domain name and SID.

**rpcclient equivalent:** `lsaquery`

```bash
nxc rpc 192.168.1.100 -u user -p pass --lsa-query
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  Domain Name: CONTOSO
RPC  192.168.1.100  445  DC01  Domain SID: S-1-5-21-1234567890-1234567890-1234567890
```

---

## Account Enumeration

### --lsa-enum-accounts

Enumerate all SIDs known to the Local Security Authority.

**rpcclient equivalent:** `lsaenumsid`

```bash
nxc rpc 192.168.1.100 -u user -p pass --lsa-enum-accounts
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 15 SID(s)
RPC  192.168.1.100  445  DC01    S-1-5-21-xxx-500
RPC  192.168.1.100  445  DC01    S-1-5-21-xxx-512
RPC  192.168.1.100  445  DC01    S-1-5-32-544
RPC  192.168.1.100  445  DC01    S-1-1-0
```

---

## Privilege Enumeration

### --lsa-enum-privileges

Enumerate all privileges known to the system.

**rpcclient equivalent:** `enumprivs`

```bash
nxc rpc 192.168.1.100 -u user -p pass --lsa-enum-privileges
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 35 privilege(s)
RPC  192.168.1.100  445  DC01    SeCreateTokenPrivilege (0x2)
RPC  192.168.1.100  445  DC01    SeAssignPrimaryTokenPrivilege (0x3)
RPC  192.168.1.100  445  DC01    SeLockMemoryPrivilege (0x4)
RPC  192.168.1.100  445  DC01    SeIncreaseQuotaPrivilege (0x5)
RPC  192.168.1.100  445  DC01    SeDebugPrivilege (0x14)
RPC  192.168.1.100  445  DC01    SeBackupPrivilege (0x11)
RPC  192.168.1.100  445  DC01    SeRestorePrivilege (0x12)
```

**Common Interesting Privileges:**
| Privilege | Description | Security Impact |
|-----------|-------------|-----------------|
| `SeDebugPrivilege` | Debug programs | Can access any process memory |
| `SeBackupPrivilege` | Back up files | Can read any file |
| `SeRestorePrivilege` | Restore files | Can write any file |
| `SeTakeOwnershipPrivilege` | Take ownership | Can take ownership of any object |
| `SeImpersonatePrivilege` | Impersonate client | Token impersonation attacks |
| `SeLoadDriverPrivilege` | Load drivers | Kernel-level access |

---

### --lsa-enum-account-rights SID

Enumerate the rights/privileges assigned to a specific SID.

**rpcclient equivalent:** `lsaenumacctrights`

```bash
# Query rights for a user SID
nxc rpc 192.168.1.100 -u user -p pass --lsa-enum-account-rights S-1-5-21-xxx-500

# Query rights for Administrators group
nxc rpc 192.168.1.100 -u user -p pass --lsa-enum-account-rights S-1-5-32-544

# Query rights for Everyone
nxc rpc 192.168.1.100 -u user -p pass --lsa-enum-account-rights S-1-1-0
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Rights for S-1-5-32-544:
RPC  192.168.1.100  445  DC01    SeBackupPrivilege
RPC  192.168.1.100  445  DC01    SeRestorePrivilege
RPC  192.168.1.100  445  DC01    SeShutdownPrivilege
RPC  192.168.1.100  445  DC01    SeRemoteInteractiveLogonRight
RPC  192.168.1.100  445  DC01    SeNetworkLogonRight
```

---

## SID and Name Lookups

### --lsa-lookup-sids SIDS

Resolve one or more SIDs to their account names.

**rpcclient equivalent:** `lookupsids`

```bash
# Single SID
nxc rpc 192.168.1.100 -u user -p pass --lsa-lookup-sids S-1-5-21-xxx-500

# Multiple SIDs (comma-separated)
nxc rpc 192.168.1.100 -u user -p pass --lsa-lookup-sids "S-1-5-21-xxx-500,S-1-5-21-xxx-512"

# Well-known SIDs
nxc rpc 192.168.1.100 -u user -p pass --lsa-lookup-sids "S-1-1-0,S-1-5-32-544"
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  S-1-5-21-xxx-500 -> CONTOSO\Administrator (User)
RPC  192.168.1.100  445  DC01  S-1-5-21-xxx-512 -> CONTOSO\Domain Admins (Group)
RPC  192.168.1.100  445  DC01  S-1-1-0 -> Everyone (WellKnown)
RPC  192.168.1.100  445  DC01  S-1-5-32-544 -> BUILTIN\Administrators (Alias)
```

**Common Well-Known SIDs:**
| SID | Name |
|-----|------|
| `S-1-0-0` | Null SID |
| `S-1-1-0` | Everyone |
| `S-1-5-7` | Anonymous |
| `S-1-5-11` | Authenticated Users |
| `S-1-5-18` | Local System |
| `S-1-5-19` | Local Service |
| `S-1-5-20` | Network Service |
| `S-1-5-32-544` | Administrators |
| `S-1-5-32-545` | Users |

---

### --lsa-lookup-names NAMES

Resolve account names to their SIDs via LSA.

**rpcclient equivalent:** `lookupnames`

```bash
# Single name
nxc rpc 192.168.1.100 -u user -p pass --lsa-lookup-names Administrator

# Multiple names (comma-separated)
nxc rpc 192.168.1.100 -u user -p pass --lsa-lookup-names "Administrator,Domain Admins,Guest"
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  Administrator -> S-1-5-21-xxx-500 (User)
RPC  192.168.1.100  445  DC01  Domain Admins -> S-1-5-21-xxx-512 (Group)
RPC  192.168.1.100  445  DC01  Guest -> S-1-5-21-xxx-501 (User)
```

---

## Account Creation

### --lsa-create-account SID

Create an LSA account object for a SID. This allows assigning privileges to the account.

**rpcclient equivalent:** `lsacreateaccount`

**Requires:** Administrative privileges

```bash
nxc rpc 192.168.1.100 -u admin -p pass --lsa-create-account S-1-5-21-xxx-1001
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Created LSA account for S-1-5-21-xxx-1001
```

---

## Security Descriptor Query

### --lsa-query-security

Query the security descriptor of the LSA policy object. Shows the DACL (Discretionary Access Control List) with all ACEs (Access Control Entries).

**rpcclient equivalent:** `lsaquerysecobj`

```bash
nxc rpc 192.168.1.100 -u user -p pass --lsa-query-security
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  revision: 1
RPC  192.168.1.100  445  DC01  type: 0x8004: SEC_DESC_DACL_PRESENT SEC_DESC_SELF_RELATIVE
RPC  192.168.1.100  445  DC01  DACL
RPC  192.168.1.100  445  DC01      ACL     Num ACEs:   9   revision:   2
RPC  192.168.1.100  445  DC01      ---
RPC  192.168.1.100  445  DC01      ACE
RPC  192.168.1.100  445  DC01          type: ACCESS DENIED (1) flags: 0x00
RPC  192.168.1.100  445  DC01          Specific bits: 0x800
RPC  192.168.1.100  445  DC01          Permissions: 0x800:
RPC  192.168.1.100  445  DC01          SID: S-1-5-7
RPC  192.168.1.100  445  DC01      ---
RPC  192.168.1.100  445  DC01      ACE
RPC  192.168.1.100  445  DC01          type: ACCESS ALLOWED (0) flags: 0x00
RPC  192.168.1.100  445  DC01          Specific bits: 0x1fff
RPC  192.168.1.100  445  DC01          Permissions: 0xf1fff: WRITE_OWNER_ACCESS WRITE_DAC_ACCESS READ_CONTROL_ACCESS DELETE_ACCESS
RPC  192.168.1.100  445  DC01          SID: S-1-5-32-544
```

**ACE Types:**
- `ACCESS ALLOWED (0)` - Grants access
- `ACCESS DENIED (1)` - Denies access
- `SYSTEM AUDIT (2)` - Audit access

**Common Permission Flags:**
- `DELETE_ACCESS` (0x10000) - Delete the object
- `READ_CONTROL_ACCESS` (0x20000) - Read security descriptor
- `WRITE_DAC_ACCESS` (0x40000) - Modify DACL
- `WRITE_OWNER_ACCESS` (0x80000) - Change owner

---

## Use Cases

### Privilege Escalation Reconnaissance

```bash
# Check what privileges are available
nxc rpc target -u user -p pass --lsa-enum-privileges

# Check privileges for your user's SID
nxc rpc target -u user -p pass --lsa-enum-account-rights S-1-5-21-xxx-YOUR_RID

# Check privileges for groups you're a member of
nxc rpc target -u user -p pass --lsa-enum-account-rights S-1-5-32-545
```

### Trust Enumeration for Lateral Movement

```bash
# Enumerate trusts
nxc rpc target -u user -p pass --enum-trusts

# Look up SIDs from other domains
nxc rpc target -u user -p pass --lsa-lookup-sids S-1-5-21-OTHER_DOMAIN_SID-512
```

### Security Audit

```bash
# Query LSA security to check who has access
nxc rpc target -u user -p pass --lsa-query-security

# Enumerate all accounts with assigned rights
nxc rpc target -u user -p pass --lsa-enum-accounts
```
