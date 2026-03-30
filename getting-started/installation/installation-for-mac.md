# 🍎 Installation for Mac

{% hint style="warning" %}
For Mac, [Homebrew](https://brew.sh/) and Rust are required for installation. If you can't install these, see below for a standalone executable.
{% endhint %}

## Setup Rust with Homebrew

Ensure Homebrew is installed, or install it with the following command

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install Rust with Homebrew

```bash
brew install rust
```

Or install via curl

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

## Installing Netexec with pipx 

```bash
brew install pipx
pipx install git+https://github.com/Pennyw0rth/NetExec
```

## Using NetExec Binary

1. Download the latest Windows binary on the [release ](https://github.com/Pennyw0rth/NetExec/releases) page (netexec-windows-latest)
2. Unzip the folder
3. Run the binary from the command line