# ldap-web-api
Basic LDAP search platform intended for back-end consumption of services that may not support it. I built this to be used as part of a Graylog Lookup Table.

## Why?
I kept needing a way to resolve data from Windows event logs that may not have been included, or that I wanted to add some contextual data to.

For example, some event logs were only giving me an object GUID or a user SID (probably a problem I need to fix somewhere else), or I'd like to look up if a user is in a certain group.
