---
description: Configuring DNS
---

# 🆕 DNS options

There are several options that can be set to configure the DNS server that is used.\
Besides forcing NetExec to use ipv6 there is an option to set the dns server manually, set a dns timeout or to configure using tcp for dns resolution:

```
netexec <protocol> <target(s)> -u username -p password --dns-server <dns-server ip>
netexec <protocol> <target(s)> -u username -p password --dns-timeout <seconds>
netexec <protocol> <target(s)> -u username -p password --dns-tcp    # Use TCP for DNS
netexec <protocol> <target(s)> -u username -p password -6           # Enforce ipv6

```
