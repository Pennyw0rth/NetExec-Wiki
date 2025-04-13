# Database General Usage

## Database General Usage

nxc automatically stores all used/dumped credentials (along with other information) in its database which is setup on first run.

Each protocol has its own database which makes things much more sane and allows for some awesome possibilities. Additionally, there are workspaces (like Metasploit), to separate different engagements/pentests.

For details and usage of a specific protocol's database see the appropriate wiki section.

All workspaces and their relative databases are stored in `~/.nxc/workspaces`

## Interacting with the Database

nxc ships with a secondary command line script `nxcdb` which abstracts interacting with the back-end database. Typing the command `nxcdb` will drop you into a command shell:

```bash
#~ nxcdb
nxcdb (default) >
```

## Listing Help

At anytime, just type "help" for a list of commands:

```bash
nxcdb (default)(smb) > help

Documented commands (type help <topic>):
========================================
clear_database  creds  dpapi  exit  export  groups  help  hosts  shares  wcc

Undocumented commands:
======================
back  import
```

## Workspaces

The default workspace name is called 'default' (as represented within the prompt), once a workspace is selected everything that you do in nxc will be stored in that workspace.

To create a workspace:

```bash
nxcdb (default) > workspace create test
[*] Creating workspace 'test'
<-- CUT -->
nxcdb (test) >
```

To switch workspace:

```bash
nxcdb (test) > workspace default
nxcdb (default) >
```

To list workspaces:

```bash
nxcdb (test) > workspace list
[*] Enumerating Workspaces
default
==> test
```

## Accessing a Protocol's Database

To access a protocol's database simply run `proto <protocol>`, for example:

```bash
nxcdb (test) > proto smb
nxcdb (test)(smb) >
```

As you can see by the prompt, we are now in the workspace called 'test' and using the SMB protocol's database. Every protocol database has its own set of commands, you can run `help` to view available commands.

Please refer to the appropriate wiki section for details and usage of a specific protocol's database.

To switch protocol database:

```bash
nxcdb (test)(smb) > back
nxcdb (test) > proto http
nxcdb (test)(http) >
```

## :new: Exporting From the Database

You can export information from the database in a few different ways

```bash
nxcdb (test)(smb) > export shares detailed file.csv
```

For all of the up to date options, type `help export`

```bash
nxcdb (default)(smb) > help export

export [creds|hosts|local_admins|shares|signing|keys] [simple|detailed|*] [filename]
Exports information to a specified file

* hosts has an additional third option from simple and detailed: signing - this simply writes a list of ips of
hosts where signing is enabled
* keys' third option is either "all" or an id of a key to export
    export keys [all|id] [filename]
```
