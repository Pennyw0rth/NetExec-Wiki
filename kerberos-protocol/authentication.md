# Authentication

## Checking Credentials

- **Failed logins** result in `[-]`.
- **Successful logins** result in `[+] Domain\Username:Password`.

Test account existence and credentials using the Kerberos protocol.

### User Existence

Enumerate valid usernames **without credentials** or triggering `badPwdCount` using AS-REQ requests without including pre-authentication data (`PA-DATA`). It only **checks if the principal exists in the KDC database**. *(Stealthy alternative to LDAP/SMB enumeration.)*

The KDC responds with:
* `KDC_ERR_PREAUTH_REQUIRED` → User exists (pre-auth is enabled for this user).
* `KDC_ERR_C_PRINCIPAL_UNKNOWN` → User does not exist.
* `KDC_ERR_CLIENT_REVOKED` → User exists but is disabled.

For a single user:
```bash
nxc kerberos <DC_IP> -u $user
```

For a list of users (like `kerbrute`):
```bash
nxc kerberos <DC_IP> -d <DOMAIN> -u <userlist.txt> [--threads <N>]
```

{% hint style="info" %}
Use the `names.withletters` trick to create `name.a`, `name.b` variants:
```shell
awk '/^[[:space:]]*$/ {next} { gsub(/^[ \t]+|[ \t]+$/,""); for(i=97;i<=122;i++) printf "%s.%c\n", $0, i }' /usr/share/seclists/Usernames/Names/names.txt | tee /tmp/names.txt > /dev/null
```
{% endhint %}

To export all users to a file:
```bash
nxc kerberos <DC_IP> -d <DOMAIN> -u <userlist.txt> [--threads <N>] --users-export output.txt
```

{% hint style="warning" %}
[AS-REP Roasting](https://www.netexec.wiki/ldap-protocol/asreproast) (LDAP with `--asreproast`) only works for users with pre-auth disabled (~5-10% of users in most AD environments). Whereas this method works for all users.
{% endhint %}


### Password Authentication

It will generate the TGT.

```bash
nxc kerberos <DC_IP> -u $user -p $password
```

### Example

Test Kerberos enumeration on the Hercules HTB machine:

{% embed url="https://www.hackthebox.com/machines/hercules" %}
