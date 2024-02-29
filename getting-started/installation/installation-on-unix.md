# 🐧 Installation for Unix

## Installing NetExec with pipx

Using pipx to install NetExec is recommended. This allows you to use NetExec and the nxcdb system-wide.

{% code overflow="wrap" fullWidth="false" %}
```
sudo apt install pipx git
pipx ensurepath
pipx install git+https://github.com/Pennyw0rth/NetExec
```
{% endcode %}

Open a new shell and you are ready to go:

```
NetExec
nxcdb
```

## Installation for development using Poetry

You're going to need to install [Poetry](https://python-poetry.org/docs/#installation) which is what nxc uses to manage dependencies.

```
apt-get install -y libssl-dev libffi-dev python-dev-is-python3 build-essential
git clone https://github.com/Pennyw0rth/NetExec
cd NetExec
poetry install
poetry run NetExec
```

## Installing NetExec with pip

{% hint style="warning" %}
Using pipx over pip is recommended
{% endhint %}

<pre><code><strong>sudo apt install python3 python3-pip
</strong>git clone https://github.com/Pennyw0rth/NetExec
cd NetExec
python3 -m venv .
source bin/activate
pip install .
NetExec
</code></pre>

## Binaries

We recommend installing via pipx/pip, but if you want to use a pre-compiled binary, go to the [Releases](https://github.com/Pennyw0rth/NetExec/releases) and download the appropriate binary.
