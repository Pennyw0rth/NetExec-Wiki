# Enumerate anonymous logon

Using a random username and password you can check if the target accepts annonymous/guest logon

{% hint style="warning" %}
I'm not sure about the diff between an anonymous logon and a guest logon, if you have the answer feel free to reach me out on twitter so I can update this page
{% endhint %}

{% hint style="danger" %}
Make sure the password is empty
{% endhint %}

```
nxc smb 10.10.10.178 -u 'a' -p ''
```

You can also check this behavior with **smbclient** or **rpcclient**

```
smbclient -N -L \\10.10.10.178
rpcclient -N -L 10.10.10.178
```

{% embed url="https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj852200(v=ws.11)" %}

### Example

Nest machine is a good example of **anonymous logon** with NetExec

{% embed url="https://www.hackthebox.eu/home/machines/profile/225" %}
