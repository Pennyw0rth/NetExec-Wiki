---
description: List and download files in the Recycle Bin
---

# Recycle Bin Module

{% hint style="warning" %}
This module requires administrator privileges.
{% endhint %}

This module lists deleted files in the Recycle Bin for every user. It shows the original location of the deleted file as well as the date when it was deleted.

List files in the Recycle Bin on the remote target:

```bash
nxc smb 192.168.1.10 -u USER -p PASSWORD -M recycle_bin
```

<figure><img src="../.gitbook/assets/Recycle_bin_listing-files.png" alt=""><figcaption><p>Listing Recycle Bin files</p></figcaption></figure>

List and download all files in the Recycle Bin on the remote target:

```bash
nxc smb 192.168.1.10 -u USER -p PASSWORD -M recycle_bin -o DOWNLOAD=true
```

List and download only specific files using a filter on the original name (file name) value:

{% hint style="info" %}
The below command only downloads files that contain the word "pass" in their name.
{% endhint %}

```bash
nxc smb 192.168.1.10 -u USER -p PASSWORD -M recycle_bin -o DOWNLOAD=true FILTER=pass
```

<figure><img src="../.gitbook/assets/Recycle_bin_filter-on-filename.png" alt=""><figcaption><p>Download files with names that contain the word "pass"</p></figcaption></figure>

## Module Options

```bash
DOWNLOAD    Download the files in the Recycle Bin (default: False)
            Example: -o DOWNLOAD=True
FILTER      Filter what files you want to download (default: all) based on their original location, supports regular expressions
            Example: -o FILTER=pass
```