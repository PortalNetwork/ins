# Tutorial

## Requirement

Python 3.6, install here: https://www.python.org/downloads/release/python-366/

## Install


Install leveldb 
```
brew install leveldb
```

To start ICON and use SCORE to develop, we have to install the following projects and libraries.

```
mkdir icon
cd icon
```

- icon-service: ICON Service for python
```
git clone https://github.com/icon-project/icon-service.git
```

- icon-commons: ICON commmon package for python
```
git clone https://github.com/icon-project/icon-commons.git
```

- earlgrey: Python AMQP RPC library
```
git clone https://github.com/icon-project/earlgrey.git
```

- icon-rpc-server: ICON RPC Server
```
git clone https://github.com/icon-project/icon-rpc-server.git
```

- t-bears: Test suite for ICON SCORE development
```
git clone https://github.com/icon-project/t-bears.git
```

## Using virtual environment
```
virtualenv -p python3 venv
source venv/bin/activate

pip install tbears
```

You can find tbears commands: [HERE](https://github.com/icon-project/t-bears#how-to-use-t-bears)

```
tbears start
```

![tbears](../assets/tbears.png)
