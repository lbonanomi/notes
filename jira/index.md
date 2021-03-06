# Assorted Opinions and Maxims for Jira Engineering

> *In every real man a child is hidden that wants to play.*  
> -Friedrich Nietzsche  

## What's this?
Various hints and instructions for the installation, engineering and management of Atlassian's Jira project management system.  

If it didn't need a complete [script](https://github.com/lbonanomi/scripts/#atlassian-jiracrowd-things) it ended-up here.


### User directories and user management

**Password Qualifications**

Employer's security team insists on a 90 day password expiration, after which an account gets a "must-change" flag in Active Directory. ***Accounts that "Must change password at next login" cannot log in to Jira until their password has changed***. This has scalded my hands so-many times I puzzled-out the [LDAP query to check user's last password change](https://github.com/lbonanomi/notes/blob/master/active_directory/index.md) and later wrote a [python check-script](https://github.com/lbonanomi/scripts/blob/master/active_directory_last_password_reset.py) for confirming a user's last password change.


**PSQL Password Reset**

Force a new password "JiraPassword" to a local user in a Postgres-backed Jira instance

```update cwd_user set credential='{PKCS5S2}b3c19ePbQB4BAWzb6NogB7oTuSKOATvJxT1JP/1knh+fi1ZwJ8TGmnzmssJsBYvG' where user_name='SOME_ADMIN';```


**Directory Precedence**

Users are authenticated by the first directory that their name appears-in. 

* Create a user in the local directory who's name duplicates a user in an LDAP/Active Directory to barge-in on existing accounts without external tools like Script-Runner.
* Jira with Crowd can be configured to "aggregate groups" to allow for group management without sharing LDAP write permissions.


**Have a Jira-internal admin user**

If the LDAP connector fails for whatever-reason having an internal user will allow an admin to log-in to a running instance to make repairs.


**Restrict Volume of Synced Active Directory Users**

Filter-out Active Directory users with a pwdLastSet value of '0'; they won't be able to log-in, anyway.


 **Create a duplicate LDAP directory**

Create a duplicate user directory in a disabled state. You can't alter a directory you're logged-in through.


### Plugins

**Installed Jira plugins can be queried with cURL:**

```curl -s -k -u  $USER:$PASSWORD   https://jira.host.com/rest/plugins/1.0/```


**Jira plugins can be installed with cURL:**

```
token=$(curl -sI "http://$ADMIN:$PASSWORD@jira.host.com/rest/plugins/1.0/" |strings|awk '/upm-token/{print $NF}');
curl -X POST "http://$ADMIN:$PASSWORD@jira.host.com/rest/plugins/1.0/?token=$token" -F "plugin=@$FILENAME"
```


**Jira plugins can be disabled with cURL if you know the plugin key value:**

```
curl -s -k -u $ADMIN:$PASSWORD https://jira.host.com/rest/plugins/1.0/$PLUGIN_KEY | sed -e 's/"enabled":true/"enabled":false/' > /tmp/killer;
curl -s -k -u $ADMIN:$PASSWORD -X PUT -H "Content-Type: application/vnd.atl.plugins.plugin+json" --data @/tmp/killer https://jira.host.com/rest/plugins/1.0/$PLUGIN_KEY
```

[Example script](https://github.com/lbonanomi/scripts/blob/master/sniper.sh)


**You can make Jira webhooks out of thin-air with cURL calls:**

```
curl -k -u ADMIN_NAME:ADMIN_PASSWORD -X POST  -H "Content-Type: application/json" -d '{"name":"WEBHOOK_NAME","description":"WEBHOOK DESCRIPTION","url":"http://TARGET_URL","events":["board_created"],"enabled":true,"filters":{"issue-related-events-section":""},"excludeBody":false}' https://jira.host.com/rest/webhooks/1.0/webhook
```


### Avatars

**Use a private avatar server**

[intravatar](https://github.com/bertbaron/intravatar) is perfect for centrally managing user avatars

### Jira email

**Jira emails can be customized by altering Velocity templates at:**  
```
atlassian-jira/WEB-INF/classes/templates/email/subject/*.vm
```


### Jira & Selenium

**Install DejaVu-Sans fonts packages on your JIRA hosts**

Otherwise you will get non-Roman characters, which will choke-out [Selenium](https://www.seleniumhq.org/)

![Jira displaying non-Roman characters](sources/images/Jira_Sanskrit.png)


```
yum install ghostscript;
yum install dejavu-fonts-common;
yum install dejavu-sans-fonts;
yum install dejavu-sans-mono-fonts;
yum install motif;
```

### Misc Jira scripting

**Get a WebSudo Token for cURL**

```
curl -s -o /dev/null -k -c cookies.txt -d "os_username=$jira_username&os_password=$jira_password" https://jira.company.com/login.jsp;
TOKEN=$(awk '!/^#/ && !/^$/ { print $NF }' cookies.txt)
```
