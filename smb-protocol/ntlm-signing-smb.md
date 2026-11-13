---
description: Checking NTLM Signing Enforcement (SMB)
---

# 🆕 Checking NTLM Signing Enforcement (SMB)

This module checks whether a target **enforces NTLM signing** (`KB5135557` / `ServerRequireNtlmSign`) over **SMB**.

It authenticates twice with the same credentials, once **negotiating NTLM signing** and once **not negotiating it**:

* Unsigned rejected + signed accepted = **NTLM signing is enforced**
* Both accepted = **NTLM signing is not enforced**

```bash
nxc smb 192.168.1.0/24 -u user -p pass -M ntlmsign
```

{% hint style="info" %}
This module requires **valid, non-guest credentials** over **NTLM**. See [Limitations](#limitations).
{% endhint %}

#### References

{% embed url="https://support.microsoft.com/en-us/servicing/os/windows/docs/2026/11/kb5135557-ntlm-signing-security-improvements" %}

## How it works

For each target the module opens two separate SMB sessions:

1. **Signed**: the NTLM Type 1 message sets the signing flag
2. **Unsigned**: the NTLM Type 1 message does not set the signing flag

The result of both logins is compared to determine whether the server rejects unsigned NTLM authentication.

{% hint style="warning" %}
Two authentication attempts are made per target, so expect two logon events per host in the target's logs.
{% endhint %}

## Example output

The screenshot below shows the registry query before and after enabling enforcement, each followed by a scan with the module.

<figure><img src="../.gitbook/assets/On vs Off SMB.png" alt=""><figcaption><p>ntlmsign against a DC with ServerRequireNtlmSign off vs on</p></figcaption></figure>

## Limitations

The check only makes sense for **NTLM authentication with a real account**. The module exits early with a failure message in the following cases.

### Kerberos

Kerberos authentication (`-k` / `--use-kcache`) does not use NTLM, so there is nothing to check.

<!-- IMAGE HERE: Kerberos exception message -->

### Null authentication

Null sessions and the `guest` account are **exempt** from `ServerRequireNtlmSign`, so a result obtained with them would be meaningless. Re-run with a non-guest account.

<!-- IMAGE HERE: Null auth exception message -->

{% hint style="info" %}
SMB1 is not supported. If the server only negotiates SMB1 the check fails.
{% endhint %}