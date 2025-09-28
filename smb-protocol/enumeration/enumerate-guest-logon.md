# Enumerate Guest Logon

Using a random username and password you can check if the target accepts guest logon. If so, it means that either the domain guest account or the local guest account of the server you're targetting is enabled.

{% hint style="info" %}
Since 2025 you can now automatically check if guest login is enabled without supplying any credentials. This method is not yet by default, make sure NetExec is up to date then edit the file \~/.nxc/nxc.conf and change the line check\_guest\_account to true. Next just fire nxc without any credentials : nxc smb 10.10.10.178 if the guest is enabled you will see: Guest: True
{% endhint %}

<figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
For checking manually, make sure the password is empty
{% endhint %}

```bash
nxc smb 10.10.10.178 -u 'a' -p '' 
nxc smb 10.10.10.178 -u 'a' -p '' --shares
```

Note that if the domain guest account is available you will be able to use to launch attacks such as Coerces.

{% embed url="https://blog.whiteflag.io/blog/guest-vs-null-session-on-windows/" %}

### Example

Nest machine is a good example of **guest logon** with NetExec

{% embed url="https://www.hackthebox.com/machines/nest" %}
