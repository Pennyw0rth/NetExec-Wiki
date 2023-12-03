---
description: >-
  If you want to build the standalone binary yourself, here is a tutorial for
  you
---

# 🛠 Manually building the binary



{% hint style="warning" %}
This process can vary from time to time as dependencies change, resulting in potential errors. If you don't need to compile the binaries yourself for a specific reason it is recommended to use the precompiled binaries from [GitHub](https://github.com/Pennyw0rth/NetExec/releases).
{% endhint %}

## Linux

Clone the repository:

```
git clone https://github.com/Pennyw0rth/NetExec.git
cd NetExec
```

Create a virtual environment for pip, install some packages and build the binary:

```
virtualenv env
source env/bin/activate
pip install pyinstaller
pyinstaller netexec.spec    # This will compile the binary
```

You should now have compiled binaries:

```
./dist/nxc
```

## Windows

You will need to install the C++ build support tools from windows in order to compile the windows binary! Especially the **Desktop development with C++** package from [here](https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=msvc-170#step-4---choose-workloads).

You will also need to have Rust installed on your machine, you can install it from [here](https://www.rust-lang.org/tools/install).

{% hint style="warning" %}
If you encounter compilation errors while installing pip dependencies you are probably missing either the C++ build tools or Rust!
{% endhint %}

Clone the repository:

```
git clone https://github.com/Pennyw0rth/NetExec.git
cd NetExec
```

Install required packages and build the binary:

```
pip install pyinstaller pillow
pyinstaller netexec.spec
```

You should now have compiled binary:

```
./dist/nxc.exe
```
