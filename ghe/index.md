# Lessons Learned Managing a GHE Instance

## What's this?

Hopefully a few helpful notes for support engineers who have been assigned issues with Github Enterprise. These nuggets are won from practical experience (and exactly *zero training*) with a fairly-standard build of GHE 2.10 that was migrated from LDAP to SAML auth on my watch. YMMV, remember to floss.


### Github Organizations

Organization invitations from members who left the group are in a Twilight Zone where they cannot be accepted or deleted.


### Interactions between git and GHE:

You may make an end-run around a potentially bad .gitconfig with ```HOME="" git cmd```

GHE trusts whatever is in .gitconfig, with potentially hilarious results

If you git mv or rename a file the log is restarted. Use ```git log --follow``` to track all changes.


### Github Enterprise Auth

A token with no permissions can clone repositories, but there is no such animal as a "read-only user"


### Github Enterprise UI

If a search shows code but serves 404 links, reindex the code @ https://$URL.com/stafftools/repositories/$ORG_NAME/$REPO_NAME/search  

OAUTH authentication (specifically for GitHub Desktop) will fail in strange ways if a user is provisioned without an email address.  

You PRs can only be assigned to collaborators.  


### GHE Integration

python git libraries honor .netrc content, this may be unexpected.
