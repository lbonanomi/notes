# Assorted Opinions and Maxims for Jira Engineering

*In every real man a child is hidden that wants to play.*

-Friedrich Nietzsche


If it doesn't need a complete [script](https://github.com/lbonanomi/scripts/tree/master/jira) it ends-up here.


**You can make webhooks out of thin-air with cURL calls:**

```
curl -k -u ADMIN_NAME:ADMIN_PASSWORD -X POST  -H "Content-Type: application/json" -d '{"name":"WEBHOOK_NAME","description":"WEBHOOK DESCRIPTION","url":"http://TARGET_URL","events":["board_created"],"enabled":true,"filters":{"issue-related-events-section":""},"excludeBody":false}' https://jira.host.com/rest/webhooks/1.0/webhook
```


**JIRA emails can be customized by altering Velocity templates at:**

``` atlassian-jira/WEB-INF/classes/templates/email/subject/*.vm```


**JIRA plugins can be queried with cURL:**

```curl -s -k -u  $USER:$PASSWORD   https://jira.host.com/rest/plugins/1.0/```


**JIRA plugins can be installed with cURL:**

```
token=$(curl -sI "http://$ADMIN:$PASSWORD@jira.host.com/rest/plugins/1.0/" |strings|awk '/upm-token/{print $NF}');
curl -X POST "http://$ADMIN:$PASSWORD@jira.host.com/rest/plugins/1.0/?token=$token" -F "plugin=@$FILENAME"
```


**JIRA plugins can be disabled with cURL if you know the plugin key value:**

```
curl -s -k -u $ADMIN:$PASSWORD https://jira.host.com/rest/plugins/1.0/$PLUGIN_KEY | sed -e 's/"enabled":true/"enabled":false/' > /tmp/killer;
curl -s -k -u $ADMIN:$PASSWORD -X PUT -H "Content-Type: application/vnd.atl.plugins.plugin+json" --data @/tmp/killer https://jira.host.com/rest/plugins/1.0/$PLUGIN_KEY
```


**Install DejaVu fonts packages on your JIRA hosts**

Otherwise you will get non-Roman characters. This will choke-out [Selenium]()

```
yum install ghostscript
yum install dejavu-fonts-common
yum install dejavu-sans-fonts
yum install dejavu-sans-mono-fonts
yum install motif
```

**Have a Jira-internal admin user**

If the LDAP connector fails this will allow an admin to log-in to a running instance to make repairs.


**Get a WebSudo Token for cURL**

```
curl -s -o /dev/null -k -c cookies.txt -d "os_username=$jira_username&os_password=$jira_password" https://jira.company.com/login.jsp;
TOKEN=$(awk '!/^#/ && !/^$/ { print $NF }' cookies.txt)
```
