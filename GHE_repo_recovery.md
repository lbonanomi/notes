# Cherry Picking GHE Repos for Recovery

## Instance a git server

```
yum install git-core -y;
useradd git;
mkdir /git;
chown git:git /git;
```

```
mkdir /git/$REPO;
cd /git/$REPO && git init --bare
```


### If you are recovering a repo from a static backup:

1. Find the on-disk location of the git repository.  
    A. If the primary appliance is up and the repository is browseable, its probably easiest to go-to https://github.enterprise.url/stafftools/repositories/$ORG/$REPO/disk 
    
    [On-Disk Storage screen capture](images/On-Disk_Storage.png)

    B. If the repository *isn't* browseable, login to the GHE replica appliance and run ```/usr/local/bin/ghe-repo $ORG/$REPO``` to su to the git user and be cd'd into the on-disk location of the repository. Make-note of the current working directory, and log-out of the appliance.  
    
    C. If no appliance is available the backup directory may be trolled with a find command to search for a known filename. ***Please note that this is a very time-consuming process***


### If you are recovering a repo from a replica instance:

If the repository *isn't* browseable, login to the GHE replica appliance and run ```/usr/local/bin/ghe-repo $ORG/$REPO``` to su to the git user and cd into the on-disk location of the repository.
