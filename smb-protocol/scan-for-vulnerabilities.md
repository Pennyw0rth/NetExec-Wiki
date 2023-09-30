---
description: Check if a DC is vulnerable
---

# Scan for Vulnerabilities

When you start your internal pentest, these are the first modules you should try:

### ZeroLogon

`NetExec smb <ip> -u '' -p '' -M zerologon`

### PetitPotam

`NetExec smb <ip> -u '' -p '' -M petitpotam`

### noPAC

`NetExec smb <ip> -u 'user' -p 'pass' -M nopac`

{% hint style="warning" %}
You need a credential for this one
{% endhint %}

Or, try them all at once! Just list each one: `-M zerologon -M petitpotam`

Check out what other modules are available via `nxc <protocol> -L`
