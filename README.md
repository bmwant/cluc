## CLUC

ClusterCreator

#### List instances
```
$ cluc vms  # show only your instances
$ cluc vms --all
```

#### List templates
```
$ cluc templates  # show only your templates
$ cluc templates --all
```

#### Get info about instance
```
$ cluc info <vm-alias>
```
`vm-alias` is either VM id or VM name.

#### Sync local directory with the remote one
```
$ cluc sync <vm-alias> --src <local-path> --dest <remote-path> 
```

```
$ cluc sync <vm-alias> --dest <remote-path>
```

```
$ cluc sync <vm-alias>
```

#### SSH into remote instance
```
$ cluc ssh <vm-alias>
```
`vm-alias` is either VM id or VM name.

#### Terminate instance
```
$ cluc terminate <vm-alias>
```
`vm-alias` is either VM id or VM name.


### Commands with interface

#### Create new virtual machine
Will get you through the set of questions determining which exact
configuration you need for the future virtual machine.
```
$ cluc create
```

#### Provision virtual machine
Will allow you to choose deployment type (playbook + set of variables)
which will be used to provision target virtual machine.
```
$ cluc provision <vm-alias>
```
`vm-alias` is either VM id or VM name.


### Development
```
$ mkvirtualenv -p python3 cluc
$ pip install -r requirements.txt
```


### Say thanks

[Donate less than 1$ here](https://gimmebackmyson.herokuapp.com/)
