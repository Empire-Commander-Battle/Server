# Setup
https://www.fsegames.eu/forum/index.php?topic=11836.0

## Windows
### Install git
https://git-scm.com/download/win

### Install make
Open
https://sourceforge.net/projects/ezwinports/files/
Download
make-X.X.X-without-guile-w32-bin.zip
Extract the contents at mingw64 folder which can be found by
opening explorer > This PC > search > mingw64

### Install Visual C++ Redistributable 2013 x86
https://www.microsoft.com/en-us/download/details.aspx?id=40784
*IMPORTANT: INSTALL THE x86 VERSION NOT THE x64 ONE*
(it is not nessecary if you arleady have MSVCR120.DLL)

### Run the server
Open git bash
```bash
cd <SERVER_PATH_HERE>/Dedicated
./run.bat
```

## Linux
### Enter shell
```bash
./guix-shell.sh
```
### Building
```bash
./build.sh
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
New features should be in separate branches named "feature/<name_of_feature>"
