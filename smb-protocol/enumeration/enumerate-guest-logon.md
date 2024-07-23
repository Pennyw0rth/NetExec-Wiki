# Enumerate Guest Logon

Using a random username and password you can check if the target accepts guest logon. If so, it means that either the domain guest account or the local guest account of the server you're targetting is enabled.

{% hint style="danger" %}
Make sure the password is empty
{% endhint %}

```
nxc smb 10.10.10.178 -u 'a' -p '' 
nxc smb 10.10.10.178 -u 'a' -p '' --shares
```

Note that if the domain guest account is available you will be able to use to launch attacks such as Coerces.

{% embed url="https://blog.whiteflag.io/blog/guest-vs-null-session-on-windows/" %}

### Example

Nest machine is a good example of **guest logon** with NetExec

{% embed url="https://www.hackthebox.eu/home/machines/profile/225" %}
