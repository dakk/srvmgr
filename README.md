# srvmgr

A pluggable server manager for all your needs.


## Install

```bash
git clone github.com/dakk/srvmgr
cd srvmgr
python3 setup.py install
```

## Configuration

Create a file called ```.srvmgr.json``` in your home directory. Services is a dict of services
with the remote port to tunnel to the given local port.

```json
{
    "services": {
        "http": [ 80, 8082 ]
    },
    "servers": [
        { "name": "test1srv", "user": "test", "services": ["http"], "host": "127.0.0.1" }
    ]
}
```


## Plugins

### SSH Plugin
```
ssh-plugin
  connect to ssh servers

  usage:
    srvmgr ssh srv [opts]           ensatablish an ssh connection to srv

  options:
    -r, --root                      force root user
    -u user, --user=user            connect as custom user
    -p port, --port=port            use a different ssh port (default is 22)
    -s service, --service=service   bind a remote service to localhost port
    -e cmd, --exec=cmd              exec a command in the remote server
```

### Conf Plugin
```
conf-plugin
  handle srvmgr configuration

  usage:
    svrmgr conf server list         list all servers
    srvmgr conf services list       list all services
```

### Status Plugin
```
status-plugin
  inspect the status of your servers

  usage:
	srvmgr status srv [fields] [opts]    ensatablish an ssh connection to srv

  fields:
	ping                                 ping reply time
	disk                                 free disk
	cpu                                  cpu usage
	mem                                  memory usage

  options:
	-r, --realtime                       show realtime data updated every delay seconds
	-d secs, --delay secs                change delay for realtime (default 10)       

  example:
	srvmgr status ALL disk,mem           show the disk and memory usage for all servers
```

### SSH Alias Plugin
```
ssh_alias-plugin
  create shell aliases for shell

  usage:
	srvmgr ssh_alias srv            create shell alias for the given server or ALL

  bashrc:
	insert the output `srvmgr ssh_alias srv` on .bashrc
```


## License

```
MIT License

Copyright (c) 2019 Davide Gessa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```