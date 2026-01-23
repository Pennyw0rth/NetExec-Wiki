# User Management

This document covers user management operations available in the RPC protocol.

## Overview

User management operations allow creating, deleting, enabling, disabling, and modifying user accounts via SAMR (Security Account Manager Remote Protocol).

**Note:** Most operations require appropriate privileges on the target system.

---

## Creating Users

### --create-user USER:PASS

Create a new domain user with the specified username and password.

**rpcclient equivalent:** `createdomuser` + `setuserinfo2`

**Requires:** Account Operator or higher privileges

```bash
nxc rpc 192.168.1.100 -u admin -p adminpass --create-user newuser:Password123!
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [*] Creating user (createdomuser newuser)
RPC  192.168.1.100  445  DC01  [+] Created user newuser with RID 0x450
```

**Notes:**
- The user is automatically enabled after creation
- Password must meet domain password policy requirements
- User is created in the domain (not local)

### Password Requirements

Most domains require passwords to meet complexity requirements:
- Minimum 7-8 characters
- Must contain 3 of 4 character types:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)

```bash
# Good password examples
nxc rpc target -u admin -p pass --create-user testuser:Summer2024!
nxc rpc target -u admin -p pass --create-user testuser:P@ssw0rd123
```

---

## Deleting Users

### --delete-user USER

Delete a domain user account.

**rpcclient equivalent:** `deletedomuser`

**Requires:** Account Operator or higher privileges

```bash
nxc rpc 192.168.1.100 -u admin -p adminpass --delete-user testuser
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [*] Deleting user (deletedomuser testuser)
RPC  192.168.1.100  445  DC01  [+] Deleted user testuser
```

**Warning:** This action is irreversible. The user account and all associated permissions will be permanently removed.

---

## Enabling/Disabling Users

### --enable-user USER

Enable a disabled user account.

**rpcclient equivalent:** `setuserinfo2`

**Requires:** Account Operator or higher privileges

```bash
nxc rpc 192.168.1.100 -u admin -p adminpass --enable-user disableduser
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [*] Enabling user account (setuserinfo2 disableduser)
RPC  192.168.1.100  445  DC01  [+] Enabled user disableduser (UAC: 0x202 -> 0x200)
```

If the user is already enabled:
```
RPC  192.168.1.100  445  DC01  [*] User disableduser is already enabled (UAC: 0x200)
```

---

### --disable-user USER

Disable a user account, preventing authentication.

**rpcclient equivalent:** `setuserinfo2`

**Requires:** Account Operator or higher privileges

```bash
nxc rpc 192.168.1.100 -u admin -p adminpass --disable-user targetuser
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [*] Disabling user account (setuserinfo2 targetuser)
RPC  192.168.1.100  445  DC01  [+] Disabled user targetuser (UAC: 0x200 -> 0x202)
```

If the user is already disabled:
```
RPC  192.168.1.100  445  DC01  [*] User targetuser is already disabled (UAC: 0x202)
```

### User Account Control (UAC) Flags

The UAC value shown indicates account status:

| Flag | Value | Description |
|------|-------|-------------|
| `USER_ACCOUNT_DISABLED` | 0x0001 | Account is disabled |
| `USER_NORMAL_ACCOUNT` | 0x0010 | Normal user account |
| `USER_DONT_EXPIRE_PASSWORD` | 0x0200 | Password never expires |
| `USER_PASSWORD_NOT_REQUIRED` | 0x0004 | No password required |

Common UAC values:
- `0x200` (512) - Normal enabled account
- `0x202` (514) - Disabled account
- `0x10200` - Normal account, password never expires

---

## Changing Passwords

### --change-password USER:OLD:NEW

Change a user's password when you know the current password. This is typically used for self-service password changes or when the old password is known.

**rpcclient equivalent:** `chgpasswd`

**Requires:** Knowledge of the current password

```bash
nxc rpc 192.168.1.100 -u user -p pass --change-password targetuser:OldPass123:NewPass456!
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [*] Changing password (chgpasswd targetuser)
RPC  192.168.1.100  445  DC01  [+] Changed password for targetuser
```

**Notes:**
- Requires the current (old) password
- The new password must meet domain password policy requirements
- Subject to minimum password age policy

---

### --reset-password USER:NEWPASS

Admin password reset - set a new password without knowing the old password.

**rpcclient equivalent:** `setuserinfo2` (level 25)

**Requires:** Account Operator or Domain Admin privileges

```bash
nxc rpc 192.168.1.100 -u admin -p adminpass --reset-password targetuser:NewPass456!
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  [*] Resetting password for targetuser
RPC  192.168.1.100  445  DC01  [+] Reset password for targetuser
```

**Notes:**
- Does NOT require knowledge of the current password
- Requires administrative privileges on the domain
- The new password must meet domain password policy requirements
- Bypasses minimum password age policy

**When to use which:**

| Scenario | Use |
|----------|-----|
| User changing own password | `--change-password` |
| Admin resetting forgotten password | `--reset-password` |
| Know the old password | `--change-password` |
| Don't know the old password | `--reset-password` |

---

## Querying Users

### --user RID_OR_NAME

Query detailed information about a specific user by RID or username.

**rpcclient equivalent:** `queryuser`

```bash
# Query by username
nxc rpc 192.168.1.100 -u user -p pass --user Administrator

# Query by RID (decimal)
nxc rpc 192.168.1.100 -u user -p pass --user 500

# Query by RID (hex)
nxc rpc 192.168.1.100 -u user -p pass --user 0x1f4
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  User Name: Administrator
RPC  192.168.1.100  445  DC01  Full Name: 
RPC  192.168.1.100  445  DC01  Home Directory: 
RPC  192.168.1.100  445  DC01  Home Drive: 
RPC  192.168.1.100  445  DC01  Logon Script: 
RPC  192.168.1.100  445  DC01  Profile Path: 
RPC  192.168.1.100  445  DC01  Description: Built-in account for administering the computer/domain
RPC  192.168.1.100  445  DC01  Workstations: 
RPC  192.168.1.100  445  DC01  Comment: 
RPC  192.168.1.100  445  DC01  Remote Dial: 
RPC  192.168.1.100  445  DC01  Logon Time: 2024-01-15 10:30:00
RPC  192.168.1.100  445  DC01  Logoff Time: Never
RPC  192.168.1.100  445  DC01  Kickoff Time: Never
RPC  192.168.1.100  445  DC01  Password Last Set: 2024-01-01 00:00:00
RPC  192.168.1.100  445  DC01  Password Can Change: 2024-01-02 00:00:00
RPC  192.168.1.100  445  DC01  Password Must Change: Never
RPC  192.168.1.100  445  DC01  User RID: 0x1f4
RPC  192.168.1.100  445  DC01  Primary Group RID: 0x201
RPC  192.168.1.100  445  DC01  Account Flags: 0x210
```

---

### --user-pass-pol RID

Query password policy information for a specific user.

**rpcclient equivalent:** `getusrdompwinfo`

```bash
nxc rpc 192.168.1.100 -u user -p pass --user-pass-pol 500
```

**Example Output:**
```
RPC  192.168.1.100  445  DC01  Password Info for RID 500:
RPC  192.168.1.100  445  DC01    Min Password Length: 7
RPC  192.168.1.100  445  DC01    Password Properties: 0x1
```

---

## Practical Use Cases

### Persistence - Create Backdoor Account

```bash
# Create a new user
nxc rpc target -u admin -p pass --create-user backdoor:ComplexP@ss123!

# Verify the user can authenticate
nxc rpc target -u backdoor -p 'ComplexP@ss123!'
```

### Disable Accounts During Incident Response

```bash
# Disable compromised account
nxc rpc target -u admin -p pass --disable-user compromised_user

# Verify account is disabled
nxc rpc target -u admin -p pass --user compromised_user
```

### Password Reset

```bash
# If you know the current password
nxc rpc target -u user -p oldpass --change-password user:oldpass:newpass
```

### Enumerate Then Target

```bash
# First enumerate users
nxc rpc target -u user -p pass --users

# Then query specific interesting users
nxc rpc target -u user -p pass --user Administrator
nxc rpc target -u user -p pass --user krbtgt
nxc rpc target -u user -p pass --user svc_backup
```

---

## Setting User Information

### --set-user-info USER CLASS VALUE

Modify various user account attributes using SAMR SetUserInformation2.

**rpcclient equivalent:** `setuserinfo2`

**Requires:** Account Operator or higher privileges (depending on attribute)

#### Available Classes

| Class | Description | Value Format | Example |
|-------|-------------|--------------|---------|
| `fullname` | Full display name | String | `"John Doe"` |
| `description` | Account description | String | `"Service Account"` |
| `comment` | Admin comment (alias for description) | String | `"Test user"` |
| `homedir` | Home directory path | UNC path | `"\\\\server\\home\\user"` |
| `homedrive` | Home drive letter | Drive letter | `"H:"` |
| `script` | Logon script path | Relative path | `"logon.bat"` |
| `profile` | Profile path | UNC path | `"\\\\server\\profiles\\user"` |
| `workstations` | Allowed workstations | Comma-separated | `"WS01,WS02,WS03"` |
| `control` | User account control flags | Integer (dec/hex) | `0x200` |
| `expires` | Account expiration | FILETIME integer | `0` (never) |
| `primary-group` | Primary group RID | Integer RID | `513` |
| `parameters` | Terminal Services parameters | String | `"CtxCfgPresent"` |
| `name` | Rename user | `newuser` or `newuser:newfullname` | `"newname:New Full Name"` |
| `logonhours` | Allowed logon hours | `all`, `none`, or 42-char hex | `all` |
| `preferences` | Locale preferences | `countrycode:codepage` | `1:437` |

---

#### Basic String Attributes

```bash
# Set full name
nxc rpc target -u admin -p pass --set-user-info jdoe fullname "John Doe"

# Set description
nxc rpc target -u admin -p pass --set-user-info jdoe description "IT Department"

# Set home directory
nxc rpc target -u admin -p pass --set-user-info jdoe homedir "\\\\fileserver\\home\\jdoe"

# Set home drive
nxc rpc target -u admin -p pass --set-user-info jdoe homedrive "H:"

# Set logon script
nxc rpc target -u admin -p pass --set-user-info jdoe script "logon.bat"

# Set profile path
nxc rpc target -u admin -p pass --set-user-info jdoe profile "\\\\fileserver\\profiles\\jdoe"

# Set allowed workstations
nxc rpc target -u admin -p pass --set-user-info jdoe workstations "PC01,PC02,PC03"
```

---

#### Rename User (name)

Rename a user account and optionally set a new full name.

```bash
# Rename user only
nxc rpc target -u admin -p pass --set-user-info olduser name newuser

# Rename user and set full name
nxc rpc target -u admin -p pass --set-user-info olduser name "newuser:New Full Name"
```

---

#### User Account Control (control)

Set UAC flags directly. Value can be decimal or hex (with 0x prefix).

```bash
# Set to normal enabled account
nxc rpc target -u admin -p pass --set-user-info jdoe control 0x200

# Set password never expires
nxc rpc target -u admin -p pass --set-user-info jdoe control 0x10200

# Disable account
nxc rpc target -u admin -p pass --set-user-info jdoe control 0x202
```

**Common UAC Values:**

| Value | Hex | Description |
|-------|-----|-------------|
| 512 | 0x200 | Normal account |
| 514 | 0x202 | Disabled account |
| 66048 | 0x10200 | Password never expires |
| 66050 | 0x10202 | Disabled + password never expires |
| 4194816 | 0x400200 | Don't require preauth |

---

#### Primary Group (primary-group)

Set the primary group RID for a user.

```bash
# Set primary group to Domain Users (RID 513)
nxc rpc target -u admin -p pass --set-user-info jdoe primary-group 513

# Set primary group to Domain Admins (RID 512)
nxc rpc target -u admin -p pass --set-user-info jdoe primary-group 512
```

**Note:** The user must already be a member of the group before setting it as primary.

---

#### Account Expiration (expires)

Set when the account expires. Uses FILETIME format (100-nanosecond intervals since January 1, 1601).

```bash
# Never expire (0)
nxc rpc target -u admin -p pass --set-user-info jdoe expires 0

# Set specific expiration (requires FILETIME calculation)
nxc rpc target -u admin -p pass --set-user-info jdoe expires 132516576000000000
```

---

#### Logon Hours (logonhours)

Control when a user is allowed to log on. Uses a 21-byte bitmap (168 bits for 168 hours in a week).

```bash
# Allow logon at all times
nxc rpc target -u admin -p pass --set-user-info jdoe logonhours all

# Deny logon at all times
nxc rpc target -u admin -p pass --set-user-info jdoe logonhours none

# Custom hours (42 hex characters = 21 bytes)
# Each bit represents one hour, starting Sunday midnight
nxc rpc target -u admin -p pass --set-user-info jdoe logonhours "ffffffffffff0000ffffffffffff0000ffffffffffff"
```

**Logon Hours Bitmap:**
- 21 bytes = 168 bits (24 hours × 7 days)
- Bit 0 = Sunday 00:00-01:00
- Bit 1 = Sunday 01:00-02:00
- ... and so on
- `0xFF` = all hours allowed for those 8 hours
- `0x00` = no hours allowed for those 8 hours

---

#### Locale Preferences (preferences)

Set country code and code page for the user.

```bash
# US English with OEM code page
nxc rpc target -u admin -p pass --set-user-info jdoe preferences 1:437

# US English with Windows code page
nxc rpc target -u admin -p pass --set-user-info jdoe preferences 1:1252
```

**Common Values:**

| Country | Code | Description |
|---------|------|-------------|
| 1 | US | United States |
| 44 | UK | United Kingdom |
| 49 | DE | Germany |
| 33 | FR | France |

| Code Page | Description |
|-----------|-------------|
| 437 | OEM US |
| 850 | OEM Multilingual |
| 1252 | Windows Western European |
| 65001 | UTF-8 |

---

#### Terminal Services Parameters (parameters)

Set Terminal Services/RDP configuration parameters.

```bash
# Set TS parameters
nxc rpc target -u admin -p pass --set-user-info jdoe parameters "CtxCfgPresent"
```

---

### Example Output

```
RPC  192.168.1.100  445  DC01  [*] Setting fullname for jdoe
RPC  192.168.1.100  445  DC01  [+] Set fullname='John Doe' for jdoe
```

---

### Practical Use Cases

#### Configure New User Profile

```bash
# Create user
nxc rpc target -u admin -p pass --create-user jdoe:Welcome123!

# Set profile attributes
nxc rpc target -u admin -p pass --set-user-info jdoe fullname "John Doe"
nxc rpc target -u admin -p pass --set-user-info jdoe description "Sales Department"
nxc rpc target -u admin -p pass --set-user-info jdoe homedir "\\\\fs01\\home\\jdoe"
nxc rpc target -u admin -p pass --set-user-info jdoe homedrive "H:"
nxc rpc target -u admin -p pass --set-user-info jdoe script "sales_logon.bat"
```

#### Restrict User Logon Hours

```bash
# Only allow logon during business hours (Mon-Fri 8am-6pm)
# This requires calculating the appropriate bitmap
nxc rpc target -u admin -p pass --set-user-info jdoe logonhours "0000fc0700fc0700fc0700fc0700fc070000000000"
```

#### Temporary Account Setup

```bash
# Create account that expires
nxc rpc target -u admin -p pass --create-user temp:TempPass123!
nxc rpc target -u admin -p pass --set-user-info temp description "Temporary contractor - expires 2024-12-31"
# Set expiration date (requires FILETIME conversion)
```
