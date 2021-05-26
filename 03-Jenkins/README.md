
# Install Jenkins 

## Install Default JDK 
```
apt-get update; apt-get install default-jdk -y
java -version 
```

## Download Jenkins WAR File
```
wget https://get.jenkins.io/war-stable/2.277.4/jenkins.war
```

## Initalize Jenkins on HTTP Port 9090
```
java -jar jenkins.war --httpPort=9090 &
```
