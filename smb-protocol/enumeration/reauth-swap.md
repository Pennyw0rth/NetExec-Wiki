# 🆕 Check SMB Signing Bypass (Re-Auth Swap)

Even when a host **enforces** SMB signing, a relayed authentication can still be abused if the server lets an existing SMB session be re-authenticated as a *different* user (a cross-user "re-auth swap"). That swap is the primitive an attacker uses to keep a privileged, relayed session alive under a signing key they control, defeating enforced signing.

This module probes a host for that behavior. It needs a **second account** that differs from the one you log in with (any domain account works, its privileges do not matter). Microsoft hardened this server-side (CVE-2026-69676): patched hosts allow same-user re-auth only and refuse the swap with `ACCESS_DENIED`. The fix is feature-flagged and not derivable from the build number, so the module tests it live.

Technique details: [Defeating enforced SMB signing](https://blackfield.ch/blog/defeating-enforced-smb-signing/)

{% hint style="warning" %}
Each target triggers one real NTLM logon as `PROBE_USER`. A **correct** password or hash never increments `badPwdCount`, whether the host is patched (`ACCESS_DENIED`) or vulnerable (`SUCCESS`). A **wrong** `PROBE_PASS`/`PROBE_NTHASH`, or a `PROBE_USER` that does not exist in the domain, returns `LOGON_FAILURE` and raises `badPwdCount` once per host. Validate `PROBE_USER` on a single host before running it wide.
{% endhint %}

### Usage

Provide a second account (`PROBE_USER` + `PROBE_PASS`) that differs from the login account:

```bash
nxc smb <ip> -u user -p pass -M reauth_swap -o PROBE_USER=second_user PROBE_PASS=second_pass
```

You can pass an NT hash instead of a password:

```bash
nxc smb <ip> -u user -p pass -M reauth_swap -o PROBE_USER=second_user PROBE_NTHASH=<nthash>
```

Expected Results:

On a vulnerable host, enforced signing can be bypassed:

```bash
SMB         192.168.1.10    445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:corp.local) (signing:True) (SMBv1:False)
SMB         192.168.1.10    445    DC01             [+] corp.local\user:password
REAUTH_SWAP 192.168.1.10    445    DC01             VULNERABLE - enforced SMB signing bypassable
REAUTH_SWAP 192.168.1.10    445    DC01             Next step: https://blackfield.ch/blog/defeating-enforced-smb-signing/
```

On a patched host, the swap is refused (same-user re-auth only):

```bash
REAUTH_SWAP 192.168.1.10    445    DC01             not vulnerable - cross-user re-auth swap refused (ACCESS_DENIED), same-user re-auth only
```
