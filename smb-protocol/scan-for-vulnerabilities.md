---
description: Check if the DC is vulnerable
---

# Scan for vulnerabilities

When you start your internal pentest, this is the first modules you should try:

### Zerologon

`NetExec smb <ip> -u '' -p '' -M zerologo`

### PetitPotam

`NetExec smb <ip> -u '' -p '' -M petitpotam`

### noPAC

`NetExec smb <ip> -u 'user' -p 'pass' -M nopac`

{% hint style="warning" %}
You need a credential for this one
{% endhint %}
