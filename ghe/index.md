# Lessons Learned Managing a GHE Instance



## What's this?

Hopefully a few helpful notes for support engineers who have been assigned issues with Github Enterprise. These nuggets are won from practical experience (and exactly *zero training*) with a fairly-standard build of GHE 2.10 that was migrated from LDAP to SAML auth on my watch. YMMV, remember to floss.



### Abuse Throttle

* "The Abuse Throttle" can make stability problems ***much worse*** in a large corporate network. Unauthenticated API calls will have their ```rate_limit_key``` set to the caller's IP, and any user routed through that IP address will be treated as an abusive user. 
 
 
Admins on networks that segregate traffic between PC and development networks with acess routers or firewalls please take note. 



### Github Organizations

* Organization invitations from members who left the group are in a Twilight Zone where they cannot be accepted or deleted.

* A group mentioned in a repo CODEOWNERS file must have explicit write access to the repo to work properly.


### Interactions between git and GHE:

* You may make an end-run around a potentially bad .gitconfig with ```HOME="" git cmd```

* Account's at my $EMPLOYER have different homedirs on some hosts. ```GIT_SSH_COMMAND="ssh -i /$PATH_TO_SSH_KEY" git clone ...```

* GHE trusts whatever is in .gitconfig, with potentially hilarious results. This is frequently demonstrated with nonsensical committer names.

* If you git mv or rename a file the log is restarted. Use ```git log --follow``` to track all changes.



### Interactions between Jenkins and GHE:

* Jenkins pipeline scans process *every* tag and *every* branch of *every* repo of a target organization.  

***If you do not perform regular housekeeping on organizations Jenkins will hammer on the Api::RepoCommits API endpoint and potentially slow/crash a GHE instance.***



### Github Enterprise Auth

* A token with no permissions can clone repositories, but there is no such animal as a "read-only user"



### Github Enterprise

* If a search shows code but serves 404 links, reindex the code @ ```https://$URL.com/stafftools/repositories/$ORG_NAME/$REPO_NAME/search```  

* OAUTH authentication (specifically for GitHub Desktop) will fail in strange ways if a user is provisioned without an email address.  

* You PRs can only be assigned to collaborators.  

* If you have an internal CA, remember to append the intermediate certificate underneath the server PEM and upload this entire SSL package. Browsers have trust intermediary certs pushed by IT, the Java integrations do not.

Intermediate certificate errors look-like:

```
+com.sun.jersey.api.client.ClientHandlerException: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
```



### GHE Integration

* python git libraries honor .netrc content, this may be unexpected.



### GHE Username/Profile Links

* Clickable links for a username are driven by the named user's email address
