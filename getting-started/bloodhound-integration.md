---
description: Sending credential to Bloodhound
---

# BloodHound integration

NetExec will set user as 'owned' on BloodHound when an account is found ! Very usefull when lsassy finds 20 credentials in one dump :)

First you need to configure your config file in you home folder: `~/.nxc/nxc.conf` and add the following lines:

```
[BloodHound]
bh_enabled = True
bh_uri = 127.0.0.1
bh_port = 7687
bh_user = user
bh_pass = pass
```

Then, every time nxc will find a valid credential, it will be added to bloodhound :tada:

To ingest the data directly follow this page

{% content-ref url="../ldap-protocol/bloodhound-ingestor.md" %}
[bloodhound-ingestor.md](../ldap-protocol/bloodhound-ingestor.md)
{% endcontent-ref %}
