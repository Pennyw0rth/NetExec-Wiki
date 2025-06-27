---
description: >-
    DNS module allows to manage DNS records in an Active-Directory integrated DNS over the LDAP protocol.
---

# DNS

The `dns` module allows for the management of DNS records in an Active Directory-integrated DNS environment directly over the LDAP protocol. It can perform actions like adding, modifying, querying, and deleting DNS records by manipulating their corresponding objects in Active Directory.

{% hint style="warning" %}
By default, the module operates on the `DomainDnsZones` partition. However, it also supports targeting older DNS partitions via the `OPTIONS=legacy` parameter. This is useful for environments with legacy DNS configurations, typically from pre-Windows 2000 systems, where DNS data was stored in the `CN=MicrosoftDNS,CN=System` container within the domain partition.
 {% endhint %}

## Module Options

This is the help menu for the module, displayed with the `-o HELP` option.

```
Usage: -M dns -o <options>

ACTIONS (specify with -o ACTION=<action> or A=<action>):

  add:          Adds a new A record. Requires RECORD and DATA.
    Example: -M dns -o ACTION=add RECORD=new-pc.winterfell.local DATA=10.4.10.100
  modify:       Modifies an existing A record. Requires RECORD and DATA.
    Example: -M dns -o ACTION=modify RECORD=new-pc.winterfell.local DATA=10.4.10.101
  query:        Queries an existing record. Requires RECORD.
    Example: -M dns -o A=query R=new-pc.winterfell.local
  remove:       Removes a record by tombstoning it. Requires RECORD and optionally DATA.
    Example: -M dns -o ACTION=remove RECORD=new-pc.winterfell.local DATA=10.4.10.101
  ldapdelete:   Deletes a record object directly from LDAP. Requires RECORD.
    Example: -M dns -o A=ldapdelete R=new-pc.winterfell.local
  resurrect:    Resurrects a tombstoned record object. Requires RECORD.
    Example: -M dns -o ACTION=resurrect RECORD=tombstoned-pc.winterfell.local
  list:         Lists all DNS zones. (Default action if no options are given)
    Example: -M dns
  list-dn:      Lists all DNS zones with their Distinguished Names.
    Example: -M dns -o ACTION=list-dn


OTHER OPTIONS:
  RECORD / R:       The FQDN of the record to target (e.g., 'new-host.domain.com').
  DATA / D:         The data for the record. For A records, this is the IP address.
  OPTIONS / O:      DNS partition to use ('forest' or 'legacy'). Default is DomainDnsZones.
  ZONE / Z:         Zone to search in, if different from the current domain.
  ALLOWMULTIPLE / M: Allow multiple A records for the same name (e.g., 'true').
  HELP / H:         Show this help message.
```

## Usage Examples

{% tabs %}
{% tab title="list" %}
Lists the available DNS zones. This is the default action if no `ACTION` is specified.

**Command:**
```bash
netexec ldap <DC_IP> -u <user> -p <pass> -M dns
```

**Output:**
```
LDAP        192.168.1.10:389      DC01      [+] winterfell.local\User:Password123!
DNS         192.168.1.10:389      DC01      Found 2 domain DNS zones:
DNS         192.168.1.10:389      DC01          _msdcs.winterfell.local
DNS         192.168.1.10:389      DC01          winterfell.local
```
{% endtab %}

{% tab title="add" %}
Adds a new `A` record.

{% hint style="info" %}
*   **`RECORD` (required):** FQDN of the computer to add.
*   **`DATA` (required):** IP address of the computer to add.
{% endhint %}

**Command:**
```bash
netexec ldap <DC_IP> -u <user> -p <pass> -M dns -o ACTION=add RECORD=new-pc.winterfell.local DATA=10.10.10.100
```

**Output:**
```
LDAP        192.168.1.10:389      DC01      [+] winterfell.local\User:Password123!
DNS         192.168.1.10:389      DC01      Adding new record
DNS         192.168.1.10:389      DC01      LDAP operation completed successfully
```
{% endtab %}

{% tab title="query" %}
Queries an existing DNS record.

{% hint style="info" %}
*   **`RECORD` (required):** FQDN of the record to query.
{% endhint %}

**Command:**
```bash
netexec ldap <DC_IP> -u <user> -p <pass> -M dns -o A=query R=new-pc.winterfell.local
```

**Output:**
```
LDAP        192.168.1.10:389      DC01      [+] winterfell.local\User:Password123!
DNS         192.168.1.10:389      DC01      Found record new-pc
DNS         192.168.1.10:389      DC01      DC=new-pc,DC=winterfell.local,CN=MicrosoftDNS,DC=DomainDnsZones,DC=winterfell,DC=local
DNS         192.168.1.10:389      DC01      Record entry:
DNS         192.168.1.10:389      DC01       - Type: 1 (A) (Serial: 1679412345)
DNS         192.168.1.10:389      DC01       - Address: 10.10.10.100
```
{% endtab %}

{% tab title="modify" %}
Modifies the IP address of an existing `A` record.

{% hint style="info" %}
*   **`RECORD` (required):** FQDN of the record to modify.
*   **`DATA` (required):** The new IP address.
{% endhint %}

**Command:**
```bash
netexec ldap <DC_IP> -u <user> -p <pass> -M dns -o ACTION=modify RECORD=new-pc.winterfell.local DATA=10.10.10.101
```

**Output:**
```
LDAP        192.168.1.10:389      DC01      [+] winterfell.local\User:Password123!
DNS         192.168.1.10:389      DC01      Modifying record
DNS         192.168.1.10:389      DC01      LDAP operation completed successfully
```
{% endtab %}

{% tab title="remove" %}
Temporarily removes a DNS record by "tombstoning" it.

{% hint style="info" %}
*   **`RECORD` (required):** FQDN of the record to remove.
*   **`DATA` (optional):** Used to remove a specific record if multiple IPs exist for the same name.
{% endhint %}

**Command:**
```bash
netexec ldap <DC_IP> -u <user> -p <pass> -M dns -o ACTION=remove RECORD=new-pc.winterfell.local
```

**Output:**
```
LDAP        192.168.1.10:389      DC01      [+] winterfell.local\User:Password123!
DNS         192.168.1.10:389      DC01      Target has only one record, tombstoning it
DNS         192.168.1.10:389      DC01      LDAP operation completed successfully
```
{% endtab %}

{% tab title="ldapdelete" %}
Permanently deletes a DNS record object directly from the LDAP database.

{% hint style="info" %}
*   **`RECORD` (required):** FQDN of the record to delete.
{% endhint %}

**Command:**
```bash
netexec ldap <DC_IP> -u <user> -p <pass> -M dns -o A=ldapdelete R=new-pc.winterfell.local
```

**Output:**
```
LDAP        192.168.1.10:389      DC01      [+] winterfell.local\User:Password123!
DNS         192.168.1.10:389      DC01      Deleting record over LDAP
DNS         192.168.1.10:389      DC01      LDAP operation completed successfully
```
{% endtab %}
{% endtabs %} 
