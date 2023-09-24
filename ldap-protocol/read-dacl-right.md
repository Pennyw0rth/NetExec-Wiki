# Read DACL right

LDAP module that permits to read and export the DACLs of one or mulitple objects !

* Read all the ACEs of the Administrator

```
poetry run NetExec ldap lab-dc.lab.local -k --kdcHost lab-dc.lab.local -M daclread -o TARGET=Administrator ACTION=read
SMB         lab-dc.lab.local 445    LAB-DC           [*] Windows 10.0 Build 17763 x64 (name:LAB-DC) (domain:lab.local) (signing:False) (SMBv1:False)
LDAP        lab-dc.lab.local 389    LAB-DC           [+] lab.local\
DACLREAD    lab-dc.lab.local 389    LAB-DC           Target principal found in LDAP (CN=Administrator,CN=Users,DC=lab,DC=local)
[*]  ACE[0] info                
[*]    ACE Type                  : ACCESS_ALLOWED_OBJECT_ACE
[*]    ACE flags                 : None
[*]    Access mask               : ReadProperty
[*]    Flags                     : ACE_OBJECT_TYPE_PRESENT, ACE_INHERITED_OBJECT_TYPE_PRESENT
[*]    Object type (GUID)        : User-Account-Restrictions (4c164200-20c0-11d0-a768-00aa006e0529)
[*]    Inherited type (GUID)     : inetOrgPerson (4828cc14-1437-45bc-9b07-ad6f015e5f28)
[*]    Trustee (SID)             : BUILTIN\Pre-Windows 2000 Compatible Access (S-1-5-32-554)
[*]  ACE[1] info                
[*]    ACE Type                  : ACCESS_ALLOWED_OBJECT_ACE
[*]    ACE flags                 : None
[*]    Access mask               : ReadProperty
[*]    Flags                     : ACE_OBJECT_TYPE_PRESENT, ACE_INHERITED_OBJECT_TYPE_PRESENT
[*]    Object type (GUID)        : User-Account-Restrictions (4c164200-20c0-11d0-a768-00aa006e0529)
[*]    Inherited type (GUID)     : User (bf967aba-0de6-11d0-a285-00aa003049e2)
[*]    Trustee (SID)             : BUILTIN\Pre-Windows 2000 Compatible Access (S-1-5-32-554)
[*]  ACE[2] info                
[*]    ACE Type                  : ACCESS_ALLOWED_OBJECT_ACE
[*]    ACE flags                 : None
[*]    Access mask               : ReadProperty
[*]    Flags                     : ACE_OBJECT_TYPE_PRESENT, ACE_INHERITED_OBJECT_TYPE_PRESENT
[*]    Object type (GUID)        : User-Logon (5f202010-79a5-11d0-9020-00c04fc2d4cf)
[*]    Inherited type (GUID)     : inetOrgPerson (4828cc14-1437-45bc-9b07-ad6f015e5f28)
[*]    Trustee (SID)             : BUILTIN\Pre-Windows 2000 Compatible Access (S-1-5-32-554)
[SNIP]
```

* Read all the rights the BlWasp user has on the Administrator

```
poetry run NetExec ldap lab-dc.lab.local -k --kdcHost lab-dc.lab.local -M daclread -o TARGET=Administrator ACTION=read PRINCIPAL=BlWasp
SMB         lab-dc.lab.local 445    LAB-DC           [*] Windows 10.0 Build 17763 x64 (name:LAB-DC) (domain:lab.local) (signing:False) (SMBv1:False)
LDAP        lab-dc.lab.local 389    LAB-DC           [+] lab.local\
DACLREAD    lab-dc.lab.local 389    LAB-DC           Found principal SID to filter on: S-1-5-21-2570265163-3918697770-3667495639-1103
DACLREAD    lab-dc.lab.local 389    LAB-DC           Target principal found in LDAP (CN=Administrator,CN=Users,DC=lab,DC=local)
[*]  ACE[10] info                
[*]    ACE Type                  : ACCESS_ALLOWED_OBJECT_ACE
[*]    ACE flags                 : None
[*]    Access mask               : ControlAccess
[*]    Flags                     : ACE_OBJECT_TYPE_PRESENT
[*]    Object type (GUID)        : User-Force-Change-Password (00299570-246d-11d0-a768-00aa006e0529)
[*]    Trustee (SID)             : blwasp (S-1-5-21-2570265163-3918697770-3667495639-1103)
```

* Read all the principals that have DCSync rights on the domain

```
poetry run NetExec ldap lab-dc.lab.local -k --kdcHost lab-dc.lab.local -M daclread -o TARGET_DN="DC=lab,DC=LOCAL" ACTION=read RIGHTS=DCSync
SMB         lab-dc.lab.local 445    LAB-DC           [*] Windows 10.0 Build 17763 x64 (name:LAB-DC) (domain:lab.local) (signing:False) (SMBv1:False)
LDAP        lab-dc.lab.local 389    LAB-DC           [+] lab.local\
DACLREAD    lab-dc.lab.local 389    LAB-DC           Target principal found in LDAP (DC=lab,DC=local)
[*]  ACE[13] info                
[*]    ACE Type                  : ACCESS_ALLOWED_OBJECT_ACE
[*]    ACE flags                 : None
[*]    Access mask               : ControlAccess
[*]    Flags                     : ACE_OBJECT_TYPE_PRESENT
[*]    Object type (GUID)        : DS-Replication-Get-Changes-All (1131f6ad-9c07-11d1-f79f-00c04fc2dcd2)
[*]    Trustee (SID)             : Domain Controllers (S-1-5-21-2570265163-3918697770-3667495639-516)
[*]  ACE[14] info                
[*]    ACE Type                  : ACCESS_ALLOWED_OBJECT_ACE
[*]    ACE flags                 : None
[*]    Access mask               : ControlAccess
[*]    Flags                     : ACE_OBJECT_TYPE_PRESENT
[*]    Object type (GUID)        : DS-Replication-Get-Changes-All (1131f6ad-9c07-11d1-f79f-00c04fc2dcd2)
[*]    Trustee (SID)             : blwasp (S-1-5-21-2570265163-3918697770-3667495639-1103)
[*]  ACE[27] info                
[*]    ACE Type                  : ACCESS_ALLOWED_OBJECT_ACE
[*]    ACE flags                 : None
[*]    Access mask               : ControlAccess
[*]    Flags                     : ACE_OBJECT_TYPE_PRESENT
[*]    Object type (GUID)        : DS-Replication-Get-Changes-All (1131f6ad-9c07-11d1-f79f-00c04fc2dcd2)
[*]    Trustee (SID)             : Administrators (S-1-5-32-544)
```

* Maybe a Denied ACE is present ?

```
poetry run NetExec ldap lab-dc.lab.local -k --kdcHost lab-dc.lab.local -M daclread -o TARGET=Administrator ACTION=read ACE_TYPE=denied
SMB         lab-dc.lab.local 445    LAB-DC           [*] Windows 10.0 Build 17763 x64 (name:LAB-DC) (domain:lab.local) (signing:False) (SMBv1:False)
LDAP        lab-dc.lab.local 389    LAB-DC           [+] lab.local\
DACLREAD    lab-dc.lab.local 389    LAB-DC           Target principal found in LDAP (CN=Administrator,CN=Users,DC=lab,DC=local)
[*]  ACE[25] info                
[*]    ACE Type                  : ACCESS_DENIED_ACE
[*]    ACE flags                 : None
[*]    Access mask               : FullControl (0xf01ff)
[*]    Trustee (SID)             : blwasp (S-1-5-21-2570265163-3918697770-3667495639-1103)
```

* Backup the DACLs of multiple targets

```
poetry run NetExec ldap lab-dc.lab.local -k --kdcHost lab-dc.lab.local -M daclread -o TARGET=../../targets.txt ACTION=backup
SMB         lab-dc.lab.local 445    LAB-DC           [*] Windows 10.0 Build 17763 x64 (name:LAB-DC) (domain:lab.local) (signing:False) (SMBv1:False)
LDAP        lab-dc.lab.local 389    LAB-DC           [+] lab.local\
DACLREAD    lab-dc.lab.local 389    LAB-DC           Target principal found in LDAP (blwasp)
DACLREAD    lab-dc.lab.local 389    LAB-DC           DACL backed up to dacledit-20220730-131655-blwasp.bak
DACLREAD    lab-dc.lab.local 389    LAB-DC           Target principal found in LDAP (Administrator)
DACLREAD    lab-dc.lab.local 389    LAB-DC           DACL backed up to dacledit-20220730-131655-Administrator.bak
DACLREAD    lab-dc.lab.local 389    LAB-DC           [-] Target SID not found in LDAP (blabla)
DACLREAD    lab-dc.lab.local 389    LAB-DC           Target principal found in LDAP (Domain Admins)
DACLREAD    lab-dc.lab.local 389    LAB-DC           DACL backed up to dacledit-20220730-131655-Domain Admins.bak
```

All the Security Descriptors have been exported, but it looks like a target doesn't exist, she will be ignored.
