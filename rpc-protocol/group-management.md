# Group Management

This document covers group management operations available in the RPC protocol.

## Overview

Group management operations allow creating, deleting, and modifying group membership via SAMR (Security Account Manager Remote Protocol).

**Note:** Most operations require appropriate privileges on the target system.

---

## Creating Groups

### --create-group GROUP

Create a new domain group.

**rpcclient equivalent:** `createdomgroup`

**Requires:** Account Operator or higher privileges

```bash
nxc rpc 192.168.1.100 -u admin -p adminpass --create-group "IT Support"
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [*] Creating group (createdomgroup IT Support)
RPC  192.168.1.100  445  DC01  [+] Created group IT Support with RID 0x450
```

---

## Deleting Groups

### --delete-group GROUP

Delete a domain group.

**rpcclient equivalent:** `deletedomgroup`

**Requires:** Account Operator or higher privileges

```bash
nxc rpc 192.168.1.100 -u admin -p adminpass --delete-group "Old Team"
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [*] Deleting group (deletedomgroup Old Team)
RPC  192.168.1.100  445  DC01  [+] Deleted group Old Team
```

**Warning:** This action is irreversible. The group and all its membership associations will be permanently removed.

---

## Managing Group Membership

### --add-to-group USER:GROUP

Add a user to a domain group.

**Requires:** Account Operator or higher privileges

```bash
# Add user to a group
nxc rpc 192.168.1.100 -u admin -p adminpass --add-to-group "john.doe:IT Support"

# Add to Domain Admins (high privilege operation)
nxc rpc 192.168.1.100 -u admin -p adminpass --add-to-group "backdoor:Domain Admins"
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [*] Adding john.doe to group IT Support
RPC  192.168.1.100  445  DC01  [+] Added john.doe to IT Support
```

---

### --remove-from-group USER:GROUP

Remove a user from a domain group.

**Requires:** Account Operator or higher privileges

```bash
nxc rpc 192.168.1.100 -u admin -p adminpass --remove-from-group "john.doe:IT Support"
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [*] Removing john.doe from group IT Support
RPC  192.168.1.100  445  DC01  [+] Removed john.doe from IT Support
```

---

## Querying Groups

### --groups

Enumerate all domain groups.

**rpcclient equivalent:** `enumdomgroups`

```bash
nxc rpc 192.168.1.100 -u user -p pass --groups
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 15 group(s)
RPC  192.168.1.100  445  DC01  group:[Domain Admins] rid:[0x200]
RPC  192.168.1.100  445  DC01  group:[Domain Users] rid:[0x201]
RPC  192.168.1.100  445  DC01  group:[Domain Guests] rid:[0x202]
RPC  192.168.1.100  445  DC01  group:[Domain Computers] rid:[0x203]
RPC  192.168.1.100  445  DC01  group:[Domain Controllers] rid:[0x204]
RPC  192.168.1.100  445  DC01  group:[Schema Admins] rid:[0x206]
RPC  192.168.1.100  445  DC01  group:[Enterprise Admins] rid:[0x207]
RPC  192.168.1.100  445  DC01  group:[IT Support] rid:[0x450]
```

---

### --local-groups

Enumerate local/alias groups (Builtin groups).

**rpcclient equivalent:** `enumalsgroups builtin`

```bash
nxc rpc 192.168.1.100 -u user -p pass --local-groups
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [+] Found 20 alias group(s)
RPC  192.168.1.100  445  DC01  group:[Administrators] rid:[0x220]
RPC  192.168.1.100  445  DC01  group:[Users] rid:[0x221]
RPC  192.168.1.100  445  DC01  group:[Guests] rid:[0x222]
RPC  192.168.1.100  445  DC01  group:[Print Operators] rid:[0x226]
RPC  192.168.1.100  445  DC01  group:[Backup Operators] rid:[0x227]
RPC  192.168.1.100  445  DC01  group:[Replicator] rid:[0x228]
RPC  192.168.1.100  445  DC01  group:[Remote Desktop Users] rid:[0x22b]
RPC  192.168.1.100  445  DC01  group:[Network Configuration Operators] rid:[0x22c]
```

---

### --group RID_OR_NAME

Query detailed information about a specific group.

**rpcclient equivalent:** `querygroup`

```bash
# Query by name
nxc rpc 192.168.1.100 -u user -p pass --group "Domain Admins"

# Query by RID (decimal)
nxc rpc 192.168.1.100 -u user -p pass --group 512

# Query by RID (hex)
nxc rpc 192.168.1.100 -u user -p pass --group 0x200
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  Group Name: Domain Admins
RPC  192.168.1.100  445  DC01  Description: Designated administrators of the domain
RPC  192.168.1.100  445  DC01  Group Attributes: 7
RPC  192.168.1.100  445  DC01  Num Members: 3
```

---

## Important Groups

### High-Privilege Domain Groups

| Group | RID | Description |
|-------|-----|-------------|
| Domain Admins | 512 (0x200) | Full control over the domain |
| Enterprise Admins | 519 (0x207) | Full control over the forest |
| Schema Admins | 518 (0x206) | Can modify AD schema |
| Domain Controllers | 516 (0x204) | All domain controllers |
| Administrators | 544 (0x220) | Local administrators (Builtin) |

### Interesting Groups for Privilege Escalation

| Group | Description | Why Interesting |
|-------|-------------|-----------------|
| Backup Operators | Can backup/restore files | SeBackupPrivilege, SeRestorePrivilege |
| Server Operators | Manage servers | Can restart services, access servers |
| Account Operators | Manage accounts | Can create users/groups |
| Print Operators | Manage printers | SeLoadDriverPrivilege |
| Remote Desktop Users | RDP access | Remote access capability |
| Remote Management Users | WinRM access | PowerShell remoting |
| DNSAdmins | DNS administration | DLL injection for privilege escalation |

---

## Practical Use Cases

### Privilege Escalation - Add to Domain Admins

```bash
# Create a backdoor user
nxc rpc target -u admin -p pass --create-user backdoor:P@ssw0rd123!

# Add to Domain Admins
nxc rpc target -u admin -p pass --add-to-group "backdoor:Domain Admins"

# Verify
nxc rpc target -u backdoor -p 'P@ssw0rd123!' --users
```

### Persistence - Create Hidden Admin Group

```bash
# Create a innocuous-looking group
nxc rpc target -u admin -p pass --create-group "Printer Users"

# Add your user to it (then later add group to local Admins via GPO/other means)
nxc rpc target -u admin -p pass --add-to-group "backdoor:Printer Users"
```

### Incident Response - Remove Compromised User from Groups

```bash
# Remove from sensitive groups
nxc rpc target -u admin -p pass --remove-from-group "compromised:Domain Admins"
nxc rpc target -u admin -p pass --remove-from-group "compromised:Enterprise Admins"

# Then disable the account
nxc rpc target -u admin -p pass --disable-user compromised
```

### Enumeration Workflow

```bash
# 1. List all groups
nxc rpc target -u user -p pass --groups

# 2. Query interesting groups for member count
nxc rpc target -u user -p pass --group "Domain Admins"
nxc rpc target -u user -p pass --group "Enterprise Admins"
nxc rpc target -u user -p pass --group "Backup Operators"

# 3. List local groups
nxc rpc target -u user -p pass --local-groups
```
