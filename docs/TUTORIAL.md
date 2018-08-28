# Tutorial

## Architecture Overview

![https://raw.githubusercontent.com/icon-project/t-bears/master/images/components.png](https://raw.githubusercontent.com/icon-project/t-bears/master/images/components.png)

## Requirement

Python 3.6, install here: https://www.python.org/downloads/release/python-366/

## Install Dependency

To start ICON and use SCORE to develop, we have to install the following projects and libraries.

### Install LevelDB 
```
brew install leveldb
```

### Install RabbitMQ
```
brew install rabbitmq
```

### Create a folder for the service
```
mkdir icon
cd icon
```

### Install ICON Service
- icon-service: ICON Service for python
```
git clone https://github.com/icon-project/icon-service.git
```

#### Building source
```
virtualenv -p python3 venv  # Create a virtual environment.
source venv/bin/activate    # Enter the virtual environment.
./build.sh                  # run build script
pip install iconservice
```

### Install ICON Commons
- icon-commons: ICON commmon package for python
```
git clone https://github.com/icon-project/icon-commons.git
```

#### Building source
```
virtualenv -p python3 venv  # Create a virtual environment.
source venv/bin/activate    # Enter the virtual environment.
./build.sh                  # run build script
pip install iconcommons
```

### Install ICON RPC Server
- icon-rpc-server: ICON RPC Server
```
git clone https://github.com/icon-project/icon-rpc-server.git
```

#### Building source
```
virtualenv -p python3 venv  # Create a virtual environment.
source venv/bin/activate    # Enter the virtual environment.
./build.sh                  # run build script
pip install iconrpcserver
```

### Install t-bears
- t-bears: Test suite for ICON SCORE development
```
git clone https://github.com/icon-project/t-bears.git
```

#### Building source
```
virtualenv -p python3 venv
source venv/bin/activate
./build.sh
pip install tbears
```

## Start ICON

Start RabbitMQ for ICON Service
```
brew services start rabbitmq
```

You can find tbears commands: [HERE](https://github.com/icon-project/t-bears#how-to-use-t-bears)

```
tbears start
```

![tbears](../assets/tbears.png)
