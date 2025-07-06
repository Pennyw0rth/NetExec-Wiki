---
description: Configuring host exclusion in NetExec
---

# Host Exclusion

## Overview

NetExec provides host exclusion functionality to prevent scanning specific hosts, IP ranges, or networks. This feature is useful for:
- Excluding critical infrastructure during penetration tests
- Avoiding scanning of honeypots or monitoring systems
- Preventing accidental scanning of out-of-scope targets
- Excluding your own machine from network-wide scans

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

This is particularly useful when:
- Running broad network scans that might include your own subnet
- Preventing self-scanning which could cause issues or false positives
- Ensuring your scanning machine doesn't appear in results

## Complete Example

Here's a complete example configuration for a penetration test scenario:

```ini
[nxc]
# Exclude critical infrastructure
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

To verify your exclusion configuration is working:

1. Check the configuration file:
```bash
cat ~/.nxc/nxc.conf | grep -A 2 exclude_hosts
cat ~/.nxc/nxc.conf | grep skip_self
```

2. Run a scan and observe the excluded hosts in verbose mode:
```bash
nxc smb 192.168.1.0/24 -v
```

Excluded hosts will be logged in verbose output.

## Best Practices

1. **Document Exclusions**: Keep a record of why specific hosts are excluded
2. **Regular Review**: Periodically review your exclusion list to ensure it's up to date
3. **Test Configuration**: Always test your configuration with a limited scan before running large-scale operations
4. **Use CIDR for Subnets**: When excluding entire subnets, use CIDR notation for clarity
5. **Combine with Target Lists**: Use exclusions in combination with target files for precise scoping

## Troubleshooting

### Hosts Still Being Scanned
- Ensure the configuration file is saved in the correct location
- Check for syntax errors in the IP addresses or ranges
- Verify the configuration file permissions are readable

### Skip Self Not Working
- Ensure `skip_self = True`
- Check that NetExec can detect network interfaces properly
- Run with verbose mode to see detected local IPs

### Performance Considerations
- Large exclusion lists may slightly impact initial scan setup time
- CIDR notation is processed more efficiently than individual IPs
- Consider using target lists instead of exclusions for very specific scans