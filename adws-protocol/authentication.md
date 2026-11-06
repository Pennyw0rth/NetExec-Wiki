# Authentication

ADWS (Active Directory Web Services) runs on TCP port 9389 and provides a SOAP-based interface to Active Directory. It is a stealthier alternative to LDAP for AD enumeration, as ADWS traffic is less commonly monitored.

{% hint style="info" %}
ADWS requires a domain to be specified with `-d` to avoid LDAP referral errors.
{% endhint %}

### Testing Credentials

```bash
nxc adws 192.168.1.100 -u user -p password -d domain.local
```

### Using NTLM Hash

```bash
nxc adws 192.168.1.100 -u user -H A29F7623FD11550DEF0192DE9246F46B -d domain.local
```

### Using Kerberos

```bash
nxc adws 192.168.1.100 -u user -p password -d domain.local -k
```

Expected Results:

```
ADWS        192.168.1.100   9389   DC01             [*] (name:DC01) (domain:domain.local)
ADWS        192.168.1.100   9389   DC01             [+] domain.local\user:password
```
