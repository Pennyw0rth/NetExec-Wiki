# ➡ Setting up Tab Completion

## Using argcomplete

Currently, we use [argcomplete](https://github.com/kislyuk/argcomplete) to automatically do tab completion through argparse.

Once you've installed nxc globally, do the following:

{% hint style="info" %}
Installing with pipx is recommended for global install
{% endhint %}

{% code overflow="wrap" fullWidth="false" %}
```
apt install python3-argcomplete
activate-global-python-argcomplete
```
{% endcode %}

Open a new shell and you are ready to go:

```
NetExec
netexec
nxc
```

If you don't want global python argcomplete, you can manually register individual commands:

{% code overflow="wrap" fullWidth="false" %}
```
eval "$(register-python-argcomplete nxc)"
```
{% endcode %}

{% hint style="info" %}
Note that this eval should be added to your `.bashrc` or `.zshrc` to activate on source
{% endhint %}
