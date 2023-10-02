# 🐧 Installation for Unix

## Installing from Source & with Poetry

You're going to need to install [Poetry](https://python-poetry.org/docs/#installation) which is what nxc uses to manage dependencies.

```
apt-get install -y libssl-dev libffi-dev python-dev-is-python3 build-essential
git clone -b mainhttps://github.com/Pennyw0rth/NetExec
cd NetExec
poetry install
poetry run NetExec
```

## Python Package

{% hint style="warning" %}
Using pipx over pip is recommanded
{% endhint %}

<pre><code><strong>python3 -m pip install pipx
</strong>git clone -b main https://github.com/Pennyw0rth/NetExec
cd NetExec
pipx install .
</code></pre>

## Binaries

We recommend installing via pip/pipx, but if you want to use a pre-compiled binary, go to the [Releases](https://github.com/Pennyw0rth/NetExec/releases) and download the appropriate binary.
