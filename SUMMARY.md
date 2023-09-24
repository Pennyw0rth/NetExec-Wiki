# Table of contents

* [Introduction](README.md)
* [Changelog](changelog.md)

## Getting Started

* [Installation](getting-started/installation/README.md)
  * [🐧 Installation for Unix](getting-started/installation/installation-on-unix.md)
  * [🪟 Installation for Windows](getting-started/installation/installation-on-windows.md)
* [Selecting & Using a Protocol](getting-started/selecting-and-using-a-protocol.md)
* [Target Formats](getting-started/target-formats.md)
* [Using Credentials](getting-started/using-credentials.md)
* [Using Kerberos](getting-started/using-kerberos.md)
* [Using Modules](getting-started/using-modules.md)
* [Database General Usage](getting-started/database-general-usage.md)
* [BloodHound integration](getting-started/bloodhound-integration.md)
* [Audit Mode](getting-started/audit-mode.md)
* [Log your results](getting-started/log-your-results.md)

## SMB protocol

* [Scan for vulnerabilities](smb-protocol/scan-for-vulnerabilities.md)
* [Enumeration](smb-protocol/enumeration/README.md)
  * [Enumerate hosts](smb-protocol/enumeration/untitled.md)
  * [Enumerate null sessions](smb-protocol/enumeration/enumerate-null-sessions.md)
  * [Enumerate anonymous logon](smb-protocol/enumeration/enumerate-anonymous-logon.md)
  * [Enumerate active sessions](smb-protocol/enumeration/enumerate-active-sessions.md)
  * [Enumerate shares and access](smb-protocol/enumeration/enumerate-shares-and-access.md)
  * [Enumerate disks](smb-protocol/enumeration/enumerate-disks.md)
  * [Enumerate logged on users](smb-protocol/enumeration/enumerate-logged-on-users.md)
  * [Enumerate domain users](smb-protocol/enumeration/enumerate-domain-users.md)
  * [Enumerate users by bruteforcing RID](smb-protocol/enumeration/enumerate-users-by-bruteforcing-rid.md)
  * [Enumerate domain groups](smb-protocol/enumeration/enumerate-domain-groups.md)
  * [Enumerate local groups](smb-protocol/enumeration/enumerate-local-groups.md)
  * [Enumerate domain password policy](smb-protocol/enumeration/enumerate-domain-password-policy-1.md)
  * [Enumerate host with SMB signing not required](smb-protocol/enumeration/smb-signing-not-required.md)
  * [🆕 Enumerate Antivirus/EDR](smb-protocol/enumeration/enumerate-antivirus-edr.md)
* [Password spraying](smb-protocol/password-spraying.md)
* [Authentication](smb-protocol/authentication/README.md)
  * [Checking Credentials (Domain)](smb-protocol/authentication/checking-credentials-domain.md)
  * [Checking credentials (Local)](smb-protocol/authentication/checking-credentials-local.md)
* [Command execution](smb-protocol/command-execution/README.md)
  * [Execute remote command](smb-protocol/command-execution/execute-remote-command.md)
  * [Getting Shells 101](smb-protocol/command-execution/getting-shells-101.md)
* [Spidering Shares](smb-protocol/spidering-shares.md)
* [Get and Put files](smb-protocol/get-and-put-files.md)
* [Obtaining Credentials](smb-protocol/obtaining-credentials/README.md)
  * [Dump SAM](smb-protocol/obtaining-credentials/dump-sam.md)
  * [Dump LSA](smb-protocol/obtaining-credentials/dump-lsa.md)
  * [Dump NTDS.dit](smb-protocol/obtaining-credentials/dump-ntds.dit.md)
  * [Dump LSASS](smb-protocol/obtaining-credentials/dump-lsass.md)
  * [Dump WIFI password](smb-protocol/obtaining-credentials/dump-wifi-password.md)
  * [Dump KeePass](smb-protocol/obtaining-credentials/dump-keepass.md)
  * [Dump DPAPI](smb-protocol/obtaining-credentials/dump-dpapi.md)
* [Defeating LAPS](smb-protocol/defeating-laps.md)
* [Spooler, WebDav running ?](smb-protocol/spooler-webdav-running.md)
* [Steal Microsoft Teams cookies](smb-protocol/steal-microsoft-teams-cookies.md)

## LDAP protocol

* [Authentication](ldap-protocol/authentication.md)
* [ASREPRoast](ldap-protocol/asreproast.md)
* [Find domain SID](ldap-protocol/find-domain-sid.md)
* [Kerberoasting](ldap-protocol/kerberoasting.md)
* [Unconstrained delegation](ldap-protocol/unconstrained-delegation.md)
* [Admin Count](ldap-protocol/admin-count.md)
* [Machine Account Quota](ldap-protocol/machine-account-quota.md)
* [Get user descriptions](ldap-protocol/get-user-descriptions.md)
* [Dump gMSA](ldap-protocol/dump-gmsa.md)
* [Exploit ESC8 (adcs)](ldap-protocol/exploit-esc8-adcs.md)
* [Extract subnet](ldap-protocol/extract-subnet.md)
* [Check LDAP signing](ldap-protocol/check-ldap-signing.md)
* [Read DACL right](ldap-protocol/read-dacl-right.md)
* [Extract gMSA secrets](ldap-protocol/extract-gmsa-secrets.md)
* [Bloodhound Ingestor](ldap-protocol/bloodhound-ingestor.md)
* [List DC IP](ldap-protocol/list-dc-ip.md)
* [Enumerate trusts](ldap-protocol/enumerate-trusts.md)

## WINRM protocol

* [Password spraying](winrm-protocol/password-spraying.md)
* [Authentication](winrm-protocol/authentication.md)
* [Command execution](winrm-protocol/command-execution.md)
* [Defeating LAPS](winrm-protocol/defeating-laps.md)

## MSSQL protocol

* [Password spraying](mssql-protocol/untitled.md)
* [Authentication](mssql-protocol/authentication.md)
* [MSSQL Privesc](mssql-protocol/mssql-privesc.md)
* [MSSQL command](mssql-protocol/mssql-command.md)
* [MSSQL upload/download](mssql-protocol/mssql-upload-download.md)
* [Windows command](mssql-protocol/windows-command.md)

## SSH protocol

* [Password spraying](ssh-protocol/password-spraying.md)
* [Authentication](ssh-protocol/untitled.md)
* [Command execution](ssh-protocol/command-execution.md)

## FTP protocol

* [Password spraying](ftp-protocol/password-spraying.md)

## RDP Protocol

* [Password spraying](rdp-protocol/password-spraying.md)
* [Screenshot (connected)](rdp-protocol/screenshot-connected.md)
* [Screenshot without NLA (not connected)](rdp-protocol/screenshot-without-nla-not-connected.md)

## WMI Protocol

* [Password spraying](wmi-protocol/password-spraying.md)
* [Authentication](wmi-protocol/authentication.md)
* [Command execution](wmi-protocol/command-execution.md)
