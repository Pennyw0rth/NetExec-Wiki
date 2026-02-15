# Table of contents

* [Welcome](README.md)
* [News](news/README.md)
  * [🕷️ v1.0.0 Release!](news/v1.0.0-release.md)
  * [🔧 v1.1.0 - nxc4u](news/v1.1.0-nxc4u.md)
  * [📡 v1.2.0 - ItsAlwaysDNS](news/v1.2.0-ItsAlwaysDNS.md)
  * [🏎️ v1.3.0 - NeedForSpeed](news/v1.3.0-NeedForSpeed.md)
  * [🧈 v1.4.0 - SmoothOperator](news/v1.4.0-SmoothOperator.md)
* [Logo & Banner](logo-and-banner.md)
* [NetExec Lab](netexec-lab.md)

## Getting Started

* [Installation](getting-started/installation/README.md)
  * [🐧 Installation for Unix](getting-started/installation/installation-on-unix.md)
  * [🪟 Installation for Windows](getting-started/installation/installation-on-windows.md)
  * [🍎 Installation for Mac](getting-started/installation/installation-for-mac.md)
  * [🛠️ Manually building the binary](getting-started/installation/manually-building-the-binary.md)
  * [➡️ Post Installation Setup](getting-started/installation/setting-up-tab-completion.md)
* [Selecting & Using a Protocol](getting-started/selecting-and-using-a-protocol.md)
* [Target Formats](getting-started/target-formats.md)
* [Using Credentials](getting-started/using-credentials.md)
* [Using Kerberos](getting-started/using-kerberos.md)
* [Using Certificates](getting-started/using-certificates.md)
* [Using Modules](getting-started/using-modules.md)
* [DNS options](getting-started/dns-options.md)
* [Database General Usage](getting-started/database-general-usage.md)
* [BloodHound Integration](getting-started/bloodhound-integration.md)
* [Audit Mode](getting-started/audit-mode.md)
* [Ignore OpSec Warnings](getting-started/ignore-opsec-warnings.md)
* [Logging](getting-started/log-your-results.md)

## SMB protocol

* [Generate hosts file](smb-protocol/generate-hosts-file.md)
* [Generate krb5.conf file](smb-protocol/generate-krb5.conf-file.md)
* [Generate TGT](smb-protocol/generate-tgt.md)
* [Scan for Vulnerabilities](smb-protocol/scan-for-vulnerabilities.md)
* [Enumeration](smb-protocol/enumeration/README.md)
  * [Enumerate Hosts](smb-protocol/enumeration/enumerate-hosts.md)
  * [Enumerate Null Sessions](smb-protocol/enumeration/enumerate-null-sessions.md)
  * [Enumerate Guest Logon](smb-protocol/enumeration/enumerate-guest-logon.md)
  * [Enumerate Hosts with SMB Signing Not Required](smb-protocol/enumeration/smb-signing-not-required.md)
  * [🆕 Enumerate Active Windows Sessions](smb-protocol/enumeration/enumerate-active-windows-sessions.md)
  * [🆕 Enumerate Logged-On Users with the Remote Registry Service](smb-protocol/enumeration/enumerate-logged-on-users-winreg.md)
  * [Enumerate Logged-On Users with the Workstation Service](smb-protocol/enumeration/enumerate-logged-on-users-wkssvc.md)
  * [Enumerate Shares and Access](smb-protocol/enumeration/enumerate-shares-and-access.md)
  * [🆕 Enumerate Network Interfaces](smb-protocol/enumeration/enumerate-network-interfaces.md)
  * [Enumerate Disks](smb-protocol/enumeration/enumerate-disks.md)
  * [Enumerate Bitlocker](smb-protocol/enumeration/enumerate-bitlocker.md)
  * [Enumerate Domain Users](smb-protocol/enumeration/enumerate-domain-users.md)
  * [Enumerate Users by Bruteforcing RID](smb-protocol/enumeration/enumerate-users-by-bruteforcing-rid.md)
  * [Enumerate Domain Groups](smb-protocol/enumeration/enumerate-domain-groups.md)
  * [Enumerate Local Groups](smb-protocol/enumeration/enumerate-local-groups.md)
  * [Enumerate Domain Password Policy](smb-protocol/enumeration/enumerate-domain-password-policy-1.md)
  * [Enumerate Anti-Virus & EDR](smb-protocol/enumeration/enumerate-antivirus-edr.md)
  * [Enumerate remote processes](smb-protocol/enumeration/enumerate-remote-processes.md)
  * [🆕 Enumerate changed lockscreen executables](smb-protocol/enumeration/enumerate-lockscreen-backdoors.md)
  * [🆕 Enumerate Primary Site Server and Distribution Point via recon6](smb-protocol/enumeration/enumerate-sccm-primarysiteserver-and-distributionpoint.md)
* [Password Spraying](smb-protocol/password-spraying.md)
* [Authentication](smb-protocol/authentication/README.md)
  * [Checking Credentials (Domain)](smb-protocol/authentication/checking-credentials-domain.md)
  * [Checking Credentials (Local)](smb-protocol/authentication/checking-credentials-local.md)
  * [🆕 Delegation](smb-protocol/authentication/delegation.md)
* [Command Execution](smb-protocol/command-execution/README.md)
  * [Executing Remote Commands](smb-protocol/command-execution/execute-remote-command/README.md)
    * [Process Injection (pi module)](smb-protocol/command-execution/execute-remote-command/process-injection-pi-module.md)
  * [Getting Shells 101](smb-protocol/command-execution/getting-shells-101.md)
* [Spidering Shares](smb-protocol/spidering-shares.md)
* [Get and Put Files](smb-protocol/get-and-put-files.md)
* [Obtaining Credentials](smb-protocol/obtaining-credentials/README.md)
  * [Dump SAM](smb-protocol/obtaining-credentials/dump-sam.md)
  * [Dump LSA](smb-protocol/obtaining-credentials/dump-lsa.md)
  * [Dump NTDS.dit](smb-protocol/obtaining-credentials/dump-ntds.dit.md)
  * [Dump LSASS](smb-protocol/obtaining-credentials/dump-lsass.md)
  * [Dump DPAPI](smb-protocol/obtaining-credentials/dump-dpapi.md)
  * [🆕 Dump with BackupOperator Priv](smb-protocol/obtaining-credentials/dump-backupop.md)
  * [🆕 Dump SCCM](smb-protocol/obtaining-credentials/dump-sccm.md)
  * [🆕 Dump Token Broker Cache](smb-protocol/obtaining-credentials/dump-token-broker-cache.md)
  * [Dump WIFI password](smb-protocol/obtaining-credentials/dump-wifi-password.md)
  * [Dump KeePass](smb-protocol/obtaining-credentials/dump-keepass.md)
  * [Dump Veeam](smb-protocol/obtaining-credentials/dump-veeam.md)
  * [Dump WinSCP](smb-protocol/obtaining-credentials/dump-winscp.md)
  * [🆕 Dump PuTTY](smb-protocol/obtaining-credentials/dump-putty.md)
  * [🆕 Dump VNC](smb-protocol/obtaining-credentials/dump-vnc.md)
  * [🆕 Dump mRemoteNG](smb-protocol/obtaining-credentials/dump-mremoteng.md)
  * [🆕 Dump Notepad](smb-protocol/obtaining-credentials/dump-notepad.md)
  * [🆕 Dump Notepad++](smb-protocol/obtaining-credentials/dump-notepad++.md)
  * [🆕 Dump Remote Desktop Credential Manager](smb-protocol/obtaining-credentials/dump-rdcman.md)
  * [🆕 Dump Event Log Creds(4688)](smb-protocol/obtaining-credentials/eventlog-creds.md)
  * [🆕 Dump Yandex Credentials](smb-protocol/obtaining-credentials/dump-yandex-creds.md)
* [Defeating LAPS](smb-protocol/defeating-laps.md)
* [Checking for Spooler & WebDav](smb-protocol/spooler-webdav-running.md)
* [Steal Microsoft Teams Cookies](smb-protocol/steal-microsoft-teams-cookies.md)
* [Impersonate logged-on Users](smb-protocol/impersonate-logged-on-users.md)
* [Change User Password](smb-protocol/change-user-password.md)
* [Dump User Local Security Questions](smb-protocol/dump-user-local-security-questions.md)

## LDAP protocol

* [Authentication](ldap-protocol/authentication.md)
* [Enumerate Domain Users](ldap-protocol/enumerate-users.md)
* [Enumerate Domain Groups](ldap-protocol/enumerate-group-members.md)
* [🆕 Query LDAP](ldap-protocol/query-ldap.md)
* [ASREPRoast](ldap-protocol/asreproast.md)
* [Find Domain SID](ldap-protocol/find-domain-sid.md)
* [Kerberoasting](ldap-protocol/kerberoasting.md)
* [🆕 Find Misconfigured Delegation](ldap-protocol/find-misconfigured-delegation.md)
* [Unconstrained Delegation](ldap-protocol/unconstrained-delegation.md)
* [Admin Count](ldap-protocol/admin-count.md)
* [Machine Account Quota](ldap-protocol/machine-account-quota.md)
* [Get User Descriptions](ldap-protocol/get-user-descriptions.md)
* [Dump gMSA](ldap-protocol/dump-gmsa.md)
* [Exploit ESC8 (ADCS)](ldap-protocol/exploit-esc8-adcs.md)
* [Extract Subnet](ldap-protocol/extract-subnet.md)
* [Check LDAP Signing](ldap-protocol/check-ldap-signing.md)
* [Read DACL Rights](ldap-protocol/read-dacl-right.md)
* [Extract gMSA Secrets](ldap-protocol/extract-gmsa-secrets.md)
* [Bloodhound Ingestor](ldap-protocol/bloodhound-ingestor.md)
* [🆕 List DC IP / Enum Trust](ldap-protocol/dc-list.md)
* [🆕 Abuse Domain Trust: Raisechild](ldap-protocol/raisechild.md)
* [Enumerate Domain Trusts](ldap-protocol/enumerate-trusts.md)
* [🆕 Enumerate SCCM](ldap-protocol/enumerate-sccm.md)
* [🆕 Enumerate Entra ID](ldap-protocol/enumerate-entra-id.md)

***

* [🆕 Dump PSO](dump-pso.md)

## WINRM protocol

* [Password Spraying](winrm-protocol/password-spraying.md)
* [Authentication](winrm-protocol/authentication.md)
* [Command Execution](winrm-protocol/command-execution.md)
* [Defeating LAPS](winrm-protocol/defeating-laps.md)
* [Obtaining Credentials](winrm-protocol/obtaining-credentials/README.md)
  * [Dump SAM](winrm-protocol/obtaining-credentials/dump-sam.md)
  * [Dump LSA](winrm-protocol/obtaining-credentials/dump-lsa.md)
  * [🆕 Dump DPAPI](winrm-protocol/obtaining-credentials/dump-dpapi.md)

## MSSQL protocol

* [Password Spraying](mssql-protocol/mssql-passwordspray.md)
* [Authentication](mssql-protocol/authentication.md)
* [MSSQL PrivEsc](mssql-protocol/mssql-privesc.md)
* [MSSQL Command Execution](mssql-protocol/mssql-command.md)
* [MSSQL Upload & Download](mssql-protocol/mssql-upload-download.md)
* [Execute via xp\_cmdshell](mssql-protocol/windows-command.md)
* [🆕 Enumerate Users by Bruteforcing RID](mssql-protocol/enumerate-users-by-bruteforcing-rid.md)
* [MSSQL Linked Servers](mssql-protocol/mssql-linked-servers.md)

## SSH protocol

* [Password Spraying](ssh-protocol/password-spraying.md)
* [Authentication](ssh-protocol/authentication.md)
* [Command Execution](ssh-protocol/command-execution.md)
* [Get and Put Files](ssh-protocol/get-and-put-files.md)

## FTP protocol

* [Password Spraying](ftp-protocol/password-spraying.md)
* [🆕 File Listing, etc](ftp-protocol/file-listing-etc.md)
* [🆕 File Upload & Download](ftp-protocol/get-and-put-files.md)

## RDP Protocol

* [Password Spraying](rdp-protocol/password-spraying.md)
* [Screenshot (connected)](rdp-protocol/screenshot-connected.md)
* [Screenshot Without NLA (not connected)](rdp-protocol/screenshot-without-nla-not-connected.md)
* [🆕 Command Execution](rdp-protocol/command-execution.md)

## WMI Protocol

* [Password Spraying](wmi-protocol/password-spraying.md)
* [Authentication](wmi-protocol/authentication.md)
* [Command Execution](wmi-protocol/command-execution.md)

## NFS Protocol

* [🆕 Enumeration](nfs-protocol/Enumeration.md)
* [Download and Upload Files](nfs-protocol/Download-and-Upload-Files.md)
* [🆕 Escape to root file system](nfs-protocol/escape-to-root-file-system.md)

## VNC Protocol

* [Authentication](vnc-protocol/authentication.md)