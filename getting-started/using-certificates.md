---
description: Using Certificates authentication with NetExec
---

# Using Certificates

## PKINIT (default)

By default, nxc authenticates with the certificate through **PKINIT**: it asks the KDC for a TGT with the certificate, then uses the resulting ticket. It works on every protocol, but requires the KDC to support PKINIT: the Domain Controller must hold a certificate with the **KDC Authentication** EKU (`1.3.6.1.5.2.3.5`), issued by a CA present in the NTAuth store.

```bash
nxc smb 192.168.0.1 --pfx-cert user.pfx -u user 
```

```bash
nxc smb 192.168.0.1 --pfx-cert user.pfx --pfx-pass password -u user 
```

```bash
nxc smb 192.168.0.1 --pfx-base64 user.pfx -u user 
```

```bash
nxc smb 192.168.0.1 --pem-cert user.pem --pem-key key.pem -u user 
```

{% hint style="info" %}
When authenticate with a certificate, nxc will generate a ccache file inside nxc home directory, you can also use this ccache to authenticate with kerberos for other tools
{% endhint %}

## Schannel (LDAP only)

When the Domain Controller has no such certificate, PKINIT is unavailable and the authentication fails with `KDC_ERR_PADATA_TYPE_NOSUPP`. With `--schannel`, the certificate is presented directly in the TLS handshake and the bind is done with a SASL `EXTERNAL` bind: Kerberos is never involved, so it still works in that case.

```bash
nxc ldap 192.168.56.3 --pfx-cert ./administrateur.pfx --schannel
```

```bash
nxc ldap 192.168.56.3 --pfx-cert ./administrateur.pfx --schannel --port 636
```

```bash
nxc ldap 192.168.56.3 --pem-cert user.pem --pem-key key.pem --schannel
```

<figure><img src="../.gitbook/assets/schannel.png" alt=""><figcaption><p>PKINIT fails on a DC without KDC certificate, while Schannel authenticates over LDAP and LDAPS</p></figcaption></figure>

{% hint style="info" %}
The account is resolved by the Domain Controller from the certificate mapping, so no username is needed: nxc retrieves the mapped account with an LDAP `whoami` and displays it (`AZOX.CORP\Administrateur from certificate`). Any `-u` value is ignored.
{% endhint %}

{% hint style="warning" %}
`--schannel` only works with the **ldap** protocol, and requires one of `--pfx-cert`, `--pfx-base64` or `--pem-cert` / `--pem-key`. Since no Kerberos ticket, password or hash is obtained, features that need a secret (SMB access, modules reading SYSVOL, etc.) are not available.
{% endhint %}
