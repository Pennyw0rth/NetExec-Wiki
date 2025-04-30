# 🐧 Installation for Unix

## Installing NetExec with pipx :saxophone:

{% hint style="info" %}
We do recomand to install rust before to make sure everything will work properly

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
{% endhint %}

Using [pipx ](https://github.com/pypa/pipx)to install NetExec is recommended. This allows you to use NetExec and the nxcdb system-wide.

```bash
sudo apt install pipx git
pipx ensurepath
pipx install git+https://github.com/Pennyw0rth/NetExec
```

Open a new shell and you are ready to go:

```bash
NetExec
nxcdb
```

Updating via pipx:

```bash
pipx upgrade netexec        # Will update if there is a new version
pipx reinstall netexec      # Force download the latest commits from github
```

#### Failed building wheel for aardwolf

If pip fails to build aardwolf you need to [install rust](https://www.rust-lang.org/tools/install). Don't forget to reload your shell so rust is added to your PATH!

## Installation for Kali :dragon\_face:

```bash
apt update
apt install netexec
```

## Installation for BlackArch :dagger:

```bash
pacman -Syu netexec
```

## Installation for ParrotSec 🦜

```bash
apt update
apt install netexec
```

## Availability on other Unix distributions :penguin:

[![Packaging status](https://repology.org/badge/vertical-allrepos/netexec.svg)](https://repology.org/project/netexec/versions)

## Installation for development using UV

Install uv (and rust)

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
apt install pipx git
pipx ensurepath
pipx install uv
```

Now that UV is set, up and we can download the NetExec repository and install its dependencies:

```
git clone https://github.com/Pennyw0rth/NetExec
cd NetExec
uv tool install .
uv run netexec
```

## Installation for development using Poetry :postal\_horn:

{% hint style="warning" %}
We do not recommand to install poetry via APT on kali
{% endhint %}

You're going to need to install [Poetry](https://python-poetry.org/docs/#installation) which is what nxc uses to manage dependencies. To install poetry you should use [pipx](https://github.com/pypa/pipx), because our dynamic-versioning plugin will likely crash otherwise.

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
apt install pipx git
pipx ensurepath
pipx install poetry
poetry self add "poetry-dynamic-versioning[plugin]"
poetry dynamic-versioning enable
```

Now that poetry is set, up and we can download the NetExec repository and install its dependencies:

```bash
git clone https://github.com/Pennyw0rth/NetExec
cd NetExec
poetry install
poetry run NetExec
```

## Binaries

We recommend installing via pipx/pip, but if you want to use a pre-compiled binary, go to the [Releases](https://github.com/Pennyw0rth/NetExec/releases) and download the appropriate binary.
