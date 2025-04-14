# ➡ Setting up Tab Completion

## Using argcomplete

Currently, we use [argcomplete](https://github.com/kislyuk/argcomplete) to automatically do tab completion through argparse.

Once you've installed nxc globally, do the following:

{% hint style="info" %}
Installing with pipx is recommended for global install
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
