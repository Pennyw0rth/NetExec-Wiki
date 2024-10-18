# 🐧 Installation for Unix

## Installing NetExec with pipx :saxophone:

Using [pipx ](https://github.com/pypa/pipx)to install NetExec is recommended. This allows you to use NetExec and the nxcdb system-wide.

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

Updating via pipx:

```
pipx upgrade netexec        # Will update if there is a new version
pipx reinstall netexec      # Force download the latest commits from github
```

## Installation for Kali :dragon\_face:

```
apt update
apt install netexec
```

## Installation for BlackArch :dagger:

```
pacman -Syu netexec
```

## Installation for ParrotSec 🦜

```
apt update
apt install netexec
```

## Availability on other Unix distributions :penguin:

[![Packaging status](https://repology.org/badge/vertical-allrepos/netexec.svg)](https://repology.org/project/netexec/versions)

## Installation for development using Poetry :postal\_horn:

You're going to need to install [Poetry](https://python-poetry.org/docs/#installation) which is what nxc uses to manage dependencies. To install poetry you should use [pipx](https://github.com/pypa/pipx), because our dynamic-versioning plugin will likely crash otherwise.

```
apt install pipx git
pipx ensurepath
pipx install poetry
poetry self add "poetry-dynamic-versioning[plugin]"
poetry dynamic-versioning enable
```

Now that poetry is set, up and we can download the NetExec repository and install its dependencies:

```
git clone https://github.com/Pennyw0rth/NetExec
cd NetExec
poetry install
poetry run NetExec
```

## Installing NetExec with pip :no\_entry:

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
