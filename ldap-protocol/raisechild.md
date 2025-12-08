
# 🆕 raisechild

Abuses an **intra-forest transitive trust** (child ↔ parent) to forge a **Golden Ticket** containing an **extra SID** from the other domain (e.g. *Enterprise Admins*).
This allows authenticating to the **target domain** with elevated privileges.

Works **child → parent** *and* **parent → child**.

---

## What it does

1. Detects the corresponding intra-forest trust (`trustedDomain` + inbound/bidirectional).
2. Retrieves the local domain SID (child or parent depending on where the module is executed).
3. Forges a TGT and injects an **extra SID** from the *other* domain (parent or child).
4. Saves the ticket as `<USER>.ccache`.

> Windows Server 2025 disables RC4 by default — AES support in this module allows forging tickets anyway.

---

## Important Requirements

### The targeted user **must exist in BOTH domains**

Since modern Windows checks the user in the PAC, the username must be valid in both the source and target domain.

### `USER_ID` **must match the RID of the user in the domain where raisechild is run**

Example: running the module **from the child domain** with user `test123`:

| Domain | User    | RID      |
| ------ | ------- | -------- |
| Child  | test123 | **1111** |
| Parent | test123 | **1001** |

You must specify:

```
-o USER=test123 -o USER_ID=1111
```

If running **from the parent**, you must instead specify:

```
-o USER=test123 -o USER_ID=1001
```

The RID must always correspond to the domain whose **krbtgt key is used to forge the ticket**.

---

## Module Options

| Option    | Description                                      | Default                 |
| --------- | ------------------------------------------------ | ----------------------- |
| `USER`    | User to impersonate (must exist in both domains) | Administrator           |
| `USER_ID` | RID of USER in the **current domain**            | 500                     |
| `RID`     | Extra SID RID injected from the **other domain** | 519 (Enterprise Admins) |
| `ETYPE`   | rc4 / aes128 / aes256                            | rc4                     |

---

## Usage Examples

Forge a basic Golden Ticket:

```bash
nxc ldap <ip> -u <user> -p <pass> -M raisechild
```

Using a specific account:

```bash
nxc ldap <ip> -u <user> -p <pass> -M raisechild -o USER=test123 USER_ID=1111
```

Using AES256:

```bash
nxc ldap <ip> -u <user> -p <pass> -M raisechild -o ETYPE=aes256
```

Change the injected extra SID:

```bash
nxc ldap <ip> -u <user> -p <pass> -M raisechild -o RID=512
```

---

## Using the forged ticket

```
export KRB5CCNAME=Administrator.ccache
```

Then authenticate to the **target domain**:

```bash
nxc ldap <parent_or_child_dc> -k --use-kcache
```

---