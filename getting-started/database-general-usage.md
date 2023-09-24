# Database General Usage

## Database General Usage

nxc automatically stores all used/dumped credentials (along with other information) in it's database which is setup on first run.

As of nxc v4 each protocol has it's own database which makes things much more sane and allows for some awesome possibilities. Additionally, v4 introduces workspaces (similar to Metasploit).

For details and usage of a specific protocol's database see the appropriate wiki section.

All workspaces and their relative databases are stored in `~/.nxc/workspaces`

## Interacting with the Database

nxc ships with a secondary command line script `nxcdb` which abstracts interacting with the back-end database. Typing the command `nxcdb` will drop you into a command shell:

```
#~ nxcdb
nxcdb (default) >
```

## Workspaces

The default workspace name is called 'default' (as represented within the prompt), once a workspace is selected everything that you do in nxc will be stored in that workspace.

To create a workspace:

```
nxcdb (default) > workspace create test
[*] Creating workspace 'test'
[*] Initializing SMB protocol database
[*] Initializing MSSQL protocol database
nxcdb (test) >
```

To switch workspace:

```
nxcdb (test) > workspace default
nxcdb (default) >
```

## Accessing a Protocol's Database

To access a protocol's database simply run `proto <protocol>`, for example:

```
nxcdb (test) > proto smb
nxcdb (test)(smb) >
```

As you can see by the prompt, we are now in the workspace called 'test' and using the SMB protocol's database. Every protocol database has its own set of commands, you can run `help` to view available commands.

Please refer to the appropriate wiki section for details and usage of a specific protocol's database.

To switch protocol database:

```
nxcdb (test)(smb) > back
nxcdb (test) > proto http
nxcdb (test)(http) >
```

## :new: Export the database

You can export the datadase in a CSV format

```
nxcdb (test)(smb) > export shares detailed file.csv
```
