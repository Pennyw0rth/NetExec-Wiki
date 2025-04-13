# 🪟 Installation for Windows

## Using Python and pipx

{% hint style="success" %}
If Python is available it is recommended to install NetExec with pipx
{% endhint %}

{% hint style="warning" %}
For Windows, git and Rust are required for installation. If you can't install either of these, see below for a standalone executable.
{% endhint %}

Set up git, Rust and C++:\
[https://git-scm.com/download/win](https://git-scm.com/download/win)\
[https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install)\
[https://visualstudio.microsoft.com/de/visual-cpp-build-tools/](https://visualstudio.microsoft.com/de/visual-cpp-build-tools/)

Install pipx and install NetExec directly from the repository:

```bash
pip install pipx
python -m pipx ensurepath
python -m pipx install git+https://github.com/Pennyw0rth/NetExec
```

Restart your command line and you should be able to execute NetExec:

```bash
NetExec
```

## Using NetExec Binary

1. Download the latest Windows binary on the [release ](https://github.com/Pennyw0rth/NetExec/releases)page (netexec-windows-latest)
2. Unzip the folder
3. Run the binary from the command line

## From Python ZippApp

{% hint style="warning" %}
Not all functionalities have been tested
{% endhint %}

1. You can also use the [standalone](https://www.python.org/downloads/windows/) version of Python, then add the path of the folder containing the python.exe file to the **PATH** env variable of your user.
2. Download the ZippApp for your specific OS & Python version [here](https://github.com/Pennyw0rth/NetExec/actions/runs/6374124950)
3. Then just run the binary `python.exe .\nxc`

{% embed url="https://www.python.org/downloads/windows/" %}

If you got this error

```bash
FileNotFoundError: [Errno 2] No such file or directory: 'C:\Users\Admin.shiv\nxc_51b7721208fc3d0af7e301aa9a56e1da0a38e9ec5bc08bfe8cc9ba14853ac5d1.tmp\site-packages\nxc\data\powersploit\CodeExecution\Invoke-ReflectivePEInjection_Resources\DemoDLL_RemoteProcess\DemoDLL_RemoteProcess\DemoDLL_RemoteProcess.vcxproj.filters
```

Add the following registry key:

```Bash
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f
```
