# Setup
## Linux setup
```bash
git clone https://github.com/Empire-Commander-Battle/Server.git
```
Edit file Dedicated/CONFIG_VARIABLES.txt to set passwords
```bash
./build.sh
./run-server.sh
```

## Windows setup
WINDOWS SETUP IS UNTESTED

In order to run the server you need to
### Build module
Run
```
Source/Sourcecode/mm dev - MS/build\_module.bat
```
### Configure passwords
Edit
```
Dedicated/CONFIG_VARIABLES.txt
```
### Build init file
Use make on
```
Dedicated/Makefile
```
### Start server
Run
```
Dedicated/run.bat
```

# Commands
## Linux
### Enter shell
```bash
./guix-shell.sh
```
### Building
```bash
./build.sh
```

### Picking configuration
```bash
make -C Dedicated <config_here>
```

### Running server
```
./run-server.sh
```

### Connect to server repl
```
python3 remote-shell.py
```
# Contributing
New features should be in separate branches named "feature/<name\_of\_feature>"
