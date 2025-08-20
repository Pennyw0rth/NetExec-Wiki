# 🆕 Command Execution

{% hint style="info" %}
This functionality is still in beta testing and was added in 2025
{% endhint %}

```
netexec rdp ip -u user -p password -x whoami
```

You can also add the flag `--cmd-delay` and `--clipboard-delay` to increase the time if the target is very slow:          &#x20;

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The use of -x option will disconnect the target user if connected (like a lock), not logoff therefore no work is lost and no application is closed.
{% endhint %}



