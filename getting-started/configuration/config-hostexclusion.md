---
description: Configuring host exclusion in NetExec
---

# 🆕 Host Exclusion

{% hint style="warning" %}
NetExec will solely exclude the target from scan operations but not from indirect connections, e.g., when collecting Bloodhound data. To completely prevent data transmission to a host, consider blocking the host in your local firewall.
{% endhint %}

## Overview

NetExec provides host exclusion functionality to prevent scanning specific hosts, IP ranges, or networks. This feature is useful for:

* Avoiding scanning of honeypots or monitoring systems
* Preventing accidental scanning of out-of-scope targets
* Excluding your own machine from network-wide scans

## Configuration

Host exclusion is configured in the NetExec configuration file located at `~/.nxc/nxc.conf` under the `[nxc]` section.

### Configuration Options

```ini
[nxc]
exclude_hosts = []
skip_self = False
```

## Exclude Specific Hosts

The `exclude_hosts` option allows you to define a list of hosts that should be permanently excluded from all NetExec scans.

### Single IP Address

```ini
exclude_hosts = ["192.168.1.100"]
```

### Multiple IP Addresses

```ini
exclude_hosts = ["192.168.1.100", "10.0.0.50", "172.16.0.254"]
```

### IP Ranges

```ini
exclude_hosts = ["192.168.1.100-110", "10.0.0.50-60"]
```

### CIDR Notation

```ini
exclude_hosts = ["192.168.1.0/24", "10.0.0.0/16"]
```

### Mixed Formats

You can combine different formats in a single configuration:

```ini
exclude_hosts = ["192.168.1.100", "10.0.0.50-60", "172.16.0.0/24", "8.8.8.8"]
```

## Skip Self

The `skip_self` option automatically excludes all local IP addresses of the machine running NetExec.

### Enable Skip Self

```ini
skip_self = True
```

When enabled, NetExec will:

1. Detect all network interfaces on the local machine
2. Identify all assigned IP addresses
3. Automatically exclude these IPs from scanning

## Complete Example

Here's a complete example configuration for a penetration test scenario:

```ini
[nxc]
# Exclude multiple hosts and/or ranges
exclude_hosts = [
    "192.168.1.1",           # Main router
    "192.168.1.10-20",       # Server range
    "10.0.0.0/24",           # Management network
    "172.16.50.100",         # Monitoring system
    "192.168.100.0/24"       # Out-of-scope network
]

# Don't scan the machine running NetExec
skip_self = True
```

## Verification

To verify your exclusion configuration is working, run a scan and observe the excluded hosts in verbose mode:

```bash
nxc smb 192.168.1.0/24 --verbose
```

Excluded hosts will be logged in verbose output.
