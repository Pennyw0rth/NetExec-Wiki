---
description: >-
  If you want to build the standalone binary yourself, here is a tutorial for
  you
---

# 🛠️ Manually building the binary



{% hint style="warning" %}
This process can vary from time to time as dependencies change, resulting in potential errors. If you don't need to compile the binaries yourself for a specific reason it is recommended to use the precompiled binaries from [GitHub](https://github.com/Pennyw0rth/NetExec/releases).
{% endhint %}

## Linux

Clone the repository:

```
git clone https://github.com/Pennyw0rth/NetExec.git
cd NetExec
```

Create a virtual environment for pip, install pyinstaller and build the binary:

```
virtualenv env
source env/bin/activate
pip install pyinstaller .
pyinstaller netexec.spec    # This will compile the binary
```

You should now have compiled binaries:

```
./dist/nxc
```

## Windows

{% hint style="warning" %}
For Windows Rust is required to build the python dependencies.
{% endhint %}

Go to the Rust installation page and follow the installation instructions:\
[https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install)

With Rust installed clone the repository:

```
git clone https://github.com/Pennyw0rth/NetExec.git
cd NetExec
```

Set up a virtual environment, install required packages and build the binary:

```
python -m venv env
source env/Scripts/activate
pip install pyinstaller pillow .
pyinstaller netexec.spec
```

You should now have compiled binary:

```
./dist/nxc.exe
```
