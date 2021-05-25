# Vagrant Virtual Machine Setup

## Now provision three virtual machines with following commands:

```
cd vagrant-setup/devops/
# vagrant.exe up


# vagrant.exe status
Current machine states:

master                    running (virtualbox)
worker1                   running (virtualbox)
worker2                   running (virtualbox)
```
## Login to master node 

```
vagrant.exe ssh master
sudo su - 
```

## Shutdown the VM 
```
vagrant.exe halt master
```

## To Destroy/Removce VM 
```
vagrant.exe destroy master
```
