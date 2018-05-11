# Idioms for managing Linux users in Active Directory


Clear Active Directory "Disabled" checkbox:

```
printf "
dn: CN=$GROUP,OU=$GROUP_OU,DC=$SERVER,DC=$DOMAIN,DC=com
changetype: modify
replace: userAccountControl
userAccountControl: 544
" | /usr/bin/ldapmodify -h $SERVER.$DOMAIN.com -D "CN=$admin_username,OU=$USER_OU,DC=$SERVER,DC=$DOMAIN,DC=com" -w "$admin_password" -f -
```


Add user to Active Directory group "$GROUP":

```
printf "
dn: CN=$GROUP,OU=$GROUP_OU,DC=$SERVER,DC=$DOMAIN,DC=com
changetype: modify
member: DN=$USER,OU=$USER_OU,DC=$SERVER,DC=$DOMAIN,DC=com
" | /usr/bin/ldapmodify -h $SERVER.$DOMAIN.com -D "CN=$admin_username,,OU=$USER_OU,DC=$SERVER,DC=$DOMAIN,DC=com" -w "$admin_password" -f -
```


Get users last password reset time in LDAP times. 

```
/usr/bin/ldapsearch -D 'CN=$admin_username,OU=$USER_OU,DC=$SERVER,DC=$DOMAIN,DC=com' -w '$admin_password' -h $SERVER.$DOMAIN.com -b  "DC=$SERVER,DC=$DOMAIN,DC=com" samAccountName=$USER_TO_CHECK pwdLastSet
```
