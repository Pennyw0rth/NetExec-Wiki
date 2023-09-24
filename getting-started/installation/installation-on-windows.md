---
description: Installation of NetExec on Windows
---

# 🪟 Installation for Windows

## Using nxc binary

1. Download the latest windows binary on the release page
2. unzip the folder
3. run the binary

## From Python standalone version

{% hint style="warning" %}
Not all functionalities have been tested
{% endhint %}

1. You can also use the [standalone](https://www.python.org/downloads/windows/) version of **Python3.8**, then add the path of the folder containing the python.exe file to the **PATH** env variable of your user.
2. Then just run the binary `python3.8.exe .\nxc`

{% embed url="https://www.python.org/downloads/windows/" %}

If you got this error

`FileNotFoundError: [Errno 2] No such file or directory: 'C:\Users\Admin.shiv\nxc_51b7721208fc3d0af7e301aa9a56e1da0a38e9ec5bc08bfe8cc9ba14853ac5d1.tmp\site-packages\nxc\data\powersploit\CodeExecution\Invoke-ReflectivePEInjection_Resources\DemoDLL_RemoteProcess\DemoDLL_RemoteProcess\DemoDLL_RemoteProcess.vcxproj.filters`

Add the following registry key:

`REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f`

## <(")

But maybe there is also a binary for Windows, just look a the github to find the answer :)
