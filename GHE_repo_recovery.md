# Cherry Picking GHE Repos for Recovery

## Instance a git server

#### Install git server package

```
sudo yum install git-core -y;
sudo mkdir /git;
sudo chmod 777 /git;
```

#### Setup SSH user access

##### Setup SSH key authentication

====================================================================================

### If you are recovering a repo from a static backup:

1. Find the on-disk location of the git repository.  
    A. If the primary appliance is up and the repository is browseable, its probably easiest to go-to https://github.enterprise.url/stafftools/repositories/$ORG/$REPO/disk 
    
    [On-Disk Storage screen capture](images/On-Disk_Storage.png)
    
    B. If the repository *isn't* browseable, login to the GHE replica appliance and run ```/usr/local/bin/ghe-repo $ORG/$REPO``` to su to the git user and be cd'd into the on-disk location of the repository. Make-note of the current working directory, and log-out of the appliance.  
    
    ```
    REPLICA-APPLIANCE: /usr/local/bin/ghe-repo lbonanomi2/scripts
    git@REPLICA-APPLIANCE:/data/repositories/d/nw/d1/e4/03/100002219/7678.git$
    ```
    C. If no appliance is available the backup directory may be trolled with a find command to search for a known filename. ***Please note that this is a very time-consuming process***

2. Create tarballs of the repository's .git directory and network.git directory.
  ```
  git@REPLICA-APPLIANCE:/data/repositories/d/nw/d1/e4/03/100002219/7678.git$ cd ..
  tar -cvf /var/tmp/7678.tar 7678.git;  
  tar -cvf /var/tmp/7678_network.tar network.git;  
  ```
3. Transfer the tarballs to the standalone git repo under /git  
4. SSH to the standalone git repo, and untar tarballs under /git  
5. *From another terminal* ```git clone $STANDALONE_GIT_SERVER:/git/7678.git```
  

### If you are recovering a repo from a replica instance:

If the repository *isn't* browseable, login to the GHE replica appliance and run ```/usr/local/bin/ghe-repo $ORG/$REPO``` to su to the git user and cd into the on-disk location of the repository.
