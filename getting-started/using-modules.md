---
description: Using Module with NetExec
---

# Using Modules

## Using Modules

### Viewing available modules for a Protocol

Run `nxc <protocol> -L` to view available modules for the specified protocol.

For example to view all modules for the SMB protocol:

```
#~ nxc smb -L
```

### Using a module

Run `nxc <protocol> <target(s)> -M <module name>`.

For example to run the SMB Mimikatz module:

```
#~ NetExec smb <target(s)> -u Administrator -p 'October2022' -M lsassy
```

### Viewing module options

Run `nxc <protocol> -M <module name> --options` to view a modules supported options, e.g:

```
#~ nxc smb -M lsassy --options
```

### Using module options

Module options are specified with the `-o` flag. All options are specified in the form of KEY=value (msfvenom style)

Example:

```
#~ nxc <protocol> <target(s)> -u Administrator -p 'P@ssw0rd' -M lsassy -o COMMAND=xxxxxxxxug'
```

### Chaining multiple modules
