---
description: Installation of NetExec on Unix system
---

# 🐧 Installation for Unix

## Installing from Source & with Poetry

You're going to need to install [Poetry](https://python-poetry.org/docs/#installation) which is what nxc uses to manage dependencies.

```
#~ apt-get install -y libssl-dev libffi-dev python-dev-is-python3 build-essential
#~ git clone https://github.com/Pennyw0rth/NetExec
#~ cd NetExec
#~ poetry install
#~ poetry run NetExec
```

## Python Package

{% hint style="warning" %}
Using pipx over pip is recommanded
{% endhint %}

<pre><code><strong>#~ python3 -m pip install pipx
</strong>#~ git clone https://github.com/Pennyw0rth/NetExec
#~ cd NetExec
#~ pipx install .
</code></pre>

## Binaries

You should be using the binaries in 99% of the cases as it requires no installation (outside of Python 3 itself).

Go to the actions tab (at the top of the repo), click on the latest build and download the appropriate binary according to your OS.

{% hint style="warning" %}
Binaries are compiled for python 3.8 / 3.9 / 3.10 / 3.11
{% endhint %}

{% hint style="info" %}
Note: you need to be logged into Github in order to download the binaries from the **Actions** feature
{% endhint %}
