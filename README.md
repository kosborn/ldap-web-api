# ldap-web-api
Basic LDAP search platform intended for back-end consumption of services that may not support it. I built this to be used as part of a Graylog Lookup Table.

## Why?
I kept needing a way to resolve data from Windows event logs that may not have been included, or that I wanted to add some contextual data to.

For example, some event logs were only giving me an object GUID or a user SID (probably a problem I need to fix somewhere else), or I'd like to look up if a user is in a certain group.

## Use
First install the dependencies from `requirements.txt`

Configure `config.py.example` and rename to `config.py`

If you're usnig Graylog, create a Data Adapter for a Lookup Table.

```
Lookup URL:            http://localhost:8888/ldap/objectGUID/${key}
Single value JSONPath: $.attributes.sAMAccountName[0]
Multi value JSONPath:  $.attributes
```

Modify Singel value to the parameter from LDAP you'd like to pull. I've created multipl data lookups,  `/objectGUID/` and `/objectSID/`, to match the currently bulnded flask endpoints. My cache table has a verty long expiry (I wouldn't expect most of the data I want when querying objectGUID and objectSID to change, such as common name, samaccount, dn, etc.)
