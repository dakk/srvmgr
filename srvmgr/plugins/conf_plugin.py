import sys
import os
import getopt
from .plugin import Plugin

class ConfPlugin (Plugin):
    NAME = "conf"
    HELP = """
conf-plugin
  handle srvmgr configuration

  usage:
    svrmgr conf server list         list all servers
    srvmgr conf services list       list all services
  
    """
    def __init__ (self, conf, args):
        self.conf = conf
        self.args = args

    def list_servers(self):
        for x in self.conf.get_servers('ALL'):
            print ("  %s %s" % (x['name'], x['host']))

    def list_services(self):
        sces = self.conf.get_services()
        for x in sces:
            b = sces[x]
            if type(b) == int:
                print ("  %s => remote as %s local as %d" % (x, b, b))
            else:
                print ("  %s => remote as %s local as %d" % (x, b[0], b[1]))

    def run(self):
        cmd = (self.args[0], self.args[1])
        if cmd == ('server', 'list'):
            return self.list_servers()
        if cmd == ('services', 'list'):
            return self.list_services()