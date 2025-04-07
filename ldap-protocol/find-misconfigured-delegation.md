# 🆕 Find Misconfigured Delegation

NetExec allows you to retrieve the list of all misconfigured delegations

```bash
nxc ldap 192.168.56.11 -u eddard.stark -p FightP3aceAndHonor! --find-delegation

# Example Output

SMB    192.168.56.11   445   WINTERFELL   [*] Windows 10 / Server 2019 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
LDAP   192.168.56.11   389   WINTERFELL   [+] north.sevenkingdoms.local\eddard.stark:FightP3aceAndHonor! (Pwn3d!)
LDAP   192.168.56.11   389   WINTERFELL   AccountName  AccountType DelegationType                     DelegationRightsTo
LDAP   192.168.56.11   389   WINTERFELL   ------------ ----------- ---------------------------------- ----------------------------------------------------------------
LDAP   192.168.56.11   389   WINTERFELL   sansa.stark  Person      Unconstrained                      N/A
LDAP   192.168.56.11   389   WINTERFELL   jon.snow     Person      Constrained w/ Protocol Transition CIFS/winterfell, CIFS/winterfell.north.sevenkingdoms.local
LDAP   192.168.56.11   389   WINTERFELL   jon.snow     Person      Resource-Based Constrained         RBCD-COMPUTER$
LDAP   192.168.56.11   389   WINTERFELL   CASTELBLACK$ Computer    Constrained                        HTTP/winterfell, HTTP/winterfell.north.sevenkingdoms.local
LDAP   192.168.56.11   389   WINTERFELL   пользователь Person      Resource-Based Constrained         WINTERFELL$
```
