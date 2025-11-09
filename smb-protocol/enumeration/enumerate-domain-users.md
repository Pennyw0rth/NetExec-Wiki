# Enumerate Domain Users

## SMB Enumeration (Authenticated)

Enumerate domain users on the remote target using authenticated SMB:

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --users
```

Export domain users on the remote target:

```bash
nxc smb <ip> -u UserNAme -p 'PASSWORDHERE' --users-export output.txt
```

## Kerberos User Enumeration (Unauthenticated) {#kerberos-user-enumeration}

Enumerate valid Active Directory usernames **without credentials** using Kerberos `AS-REQ` requests (no pre-authentication).

This method:
- Does **not** increment `badPwdCount` (stealthy)
- Works for **all users** (not just those with pre-auth disabled)
- Uses Kerberos port 88 (not SMB port 445)
- Similar to `kerbrute` functionality

{% hint style="warning" %}
**Note:** While the command uses `nxc smb`, this actually performs Kerberos enumeration on port 88. The output may show "SMB" and "445" but this is a display artifact of NetExec's architecture.
{% endhint %}

### How it Works

The tool sends AS-REQ requests without pre-authentication data (`PA-DATA`), checking if the principal exists in the KDC database.

The KDC responds with:
* `KDC_ERR_PREAUTH_REQUIRED` → User exists (pre-auth enabled)
* `KDC_ERR_C_PRINCIPAL_UNKNOWN` → User does not exist
* `KDC_ERR_CLIENT_REVOKED` → User exists but is disabled

### Single User Verification

```bash
nxc smb <DC_IP> -d <DOMAIN> -u <username> -k
```

### Batch Enumeration

```bash
nxc smb <DC_IP> -d <DOMAIN> -u <userlist.txt> -k

Export valid users to a file:
```bash
nxc smb <DC_IP> -d <DOMAIN> -u <userlist.txt> -k --users-export output.txt
```

{% hint style="info" %}
Use the `names.withletters` trick to create `name.a`, `name.b` variants:
```shell
awk '/^[[:space:]]*$/ {next} { gsub(/^[ \t]+|[ \t]+$/,""); for(i=97;i<=122;i++) printf "%s.%c\n", $0, i }' /usr/share/seclists/Usernames/Names/names.txt | tee /tmp/names.txt > /dev/null
```
{% endhint %}

{% hint style="info" %}
**Performance Note:** Due to NetExec's architecture (global semaphore in `connection.py`), enumeration happens sequentially even with `--threads`. This is slower than dedicated tools like `kerbrute` but provides unified tooling.
{% endhint %}

### Comparison with AS-REP Roasting

[AS-REP Roasting](https://www.netexec.wiki/ldap-protocol/asreproast) (LDAP with `--asreproast`) only works for users with pre-auth disabled (~5-10% of users in most AD environments), whereas Kerberos user enumeration works for **all users**.
