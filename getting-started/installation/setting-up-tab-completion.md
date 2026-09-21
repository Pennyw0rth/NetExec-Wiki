# ➡️ Post Installation Setup

## Setting up Tab Completion

Currently, we use [argcomplete](https://github.com/kislyuk/argcomplete) to automatically do tab completion through argparse.

Once you've installed nxc globally, do the following:

{% hint style="info" %}
Installing with pipx is recommended for global availability
{% endhint %}

```bash
sudo apt install python3-argcomplete

# For Bash
register-python-argcomplete nxc >> ~/.bashrc

# For Zsh
register-python-argcomplete nxc >> ~/.zshrc
```

Open a new shell and you are ready to go:

```bash
NetExec
netexec
nxc
```

## Configuring NetExec's Homefolder

NetExec will create a folder to which the `nxc.conf` configuration file and all other data created/extracted during day-to-day use are written. The default folder that will be created is `~/.nxc`. If you would like to change the destination folder set the environment variable `NXC_PATH` to the target folder.

## Configuring NetExec's Bloodhound Ingestor

Netexec's default Bloodhound ingestor is CE. If you want Netexec to ingest data for legacy:

1. Open `nxc.conf`
2. Set `bh_enabled = True`
3. Set `bhce_enabled = False`
4. Save and you're ready to roll

Bash one liners:

1. For enabling legacy, disabling CE:
```sed -Ei 's/^[[:space:]]*bh_enabled[[:space:]]*=.*/bh_enabled = True/; s/^[[:space:]]*bhce_enabled[[:space:]]*=.*/bhce_enabled = False/' ~/.nxc/nxc.conf```

2. For enabling CE, disabling legacy:
```sed -Ei 's/^[[:space:]]*bh_enabled[[:space:]]*=.*/bh_enabled = False/; s/^[[:space:]]*bhce_enabled[[:space:]]*=.*/bhce_enabled = True/' ~/.nxc/nxc.conf```