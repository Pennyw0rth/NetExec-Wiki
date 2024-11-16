# Find Misconfigured Delegation

NetExec allows you to retrieve the list of all misconfigured delegations

```
nxc ldap 192.168.0.104 -u harry -p pass --find-delegation

# Example Output

nxc ldap 192.168.56.11 -u eddard.stark -p FightP3aceAndHonor! --find-delegation
SMB    192.168.56.11    445    WINTERFELL
LDAP   192.168.56.11    389    WINTERFELL
LDAP   192.168.56.11    389    WINTERFELL    [+] Windows 10 / Server 2019 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
LDAP   192.168.56.11    389    WINTERFELL    AccountName          AccountType          DelegationType                     DelegationRightsTo
LDAP   192.168.56.11    389    WINTERFELL    ----------------------------------------------------------------------------------------------------------------
LDAP   192.168.56.11    389    WINTERFELL    sansa.stark          Person               Unconstrained                      N/A
LDAP   192.168.56.11    389    WINTERFELL    jon.snow             Person               Constrained w/ Protocol Transition CIFS/winterfell, CIFS/winterfell.north.sevenkingdoms.local
LDAP   192.168.56.11    389    WINTERFELL    jon.snow             Person               Resource-Based Constrained         RBCD-COMPUTER$
LDAP   192.168.56.11    389    WINTERFELL    CASTLEBLACK$         Computer             Constrained                        HTTP/winterfell, HTTP/winterfell.north.sevenkingdoms.local
LDAP   192.168.56.11    389    WINTERFELL    пользователь$        Person               Resource-Based Constrained         WINTERFELL$
```


