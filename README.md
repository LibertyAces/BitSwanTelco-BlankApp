# Creating blank BitSwan for Telco application

## Prerequisites
 - python3
 - pip
 - docker


## Configure
Modify TODOs in the ./etc/site.conf file.


## Run on your computer

### Install
Install required libraries:
```bash
$ pip install asab bspump bspumptelco
```
Clone git repository to your work directory:
```bash
$ git clone git@github.com:LibertyAces/BitSwanTelco-BlankApp.git bstelco-blank-app
```

### Run

```
./bstelco-blank-app.py -c ./etc/site.conf 	
```


## Run in Docker
Move to the directory (it is `bstelco-blank-app` in our case):
```bash
$ cd bstelco-blank-app
```
Then you can build your docker image:
```bash
$ docker build -t bstelco-blank-app .
```
Once you have your docker image built, run it in a container:
```bash
$ sudo docker run bstelco-blank-app
```


## Customize
From here you should have your BitSwan for Telco application up and running. You may go on and customize it to your needs. 
