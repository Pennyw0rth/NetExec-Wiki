# 🆕 Enumerate SCCM

System Center Configuration Manager (SCCM) or also called MECM nowadays is a managament infrastructure for inventor/endpoint management. As it contains a lot of different server or applications enumerating and mapping them isn't easy.&#x20;

This module implements the LDAP enumeration part of the [Misconfiguration-Manager](https://github.com/subat0mik/Misconfiguration-Manager) ([RECON-1](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/attack-techniques/RECON/RECON-1/recon-1_description.md)) to assist with initial discovery of SCCM entities in the AD environment. It will find SCCM Site-Servers, SCCM Sites, SCCM Management Points and Users, Computers or Groups related to SCCM.

```bash
nxc ldap 192.168.33.10 -u alice -p whiteRabbit -M sccm -o REC_RESOLVE=TRUE
```

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption><p>Enumerate SCCM environments in Active Directory using LDAP and the SCCM module</p></figcaption></figure>

{% content-ref url="../smb-protocol/obtaining-credentials/dump-sccm.md" %}
[dump-sccm.md](../smb-protocol/obtaining-credentials/dump-sccm.md)
{% endcontent-ref %}

{% embed url="https://github.com/subat0mik/Misconfiguration-Manager" %}

{% embed url="https://github.com/garrettfoster13/sccmhunter" %}
