import sys
import os
import getopt
from .plugin import Plugin

class SSHAliasPlugin (Plugin):
	NAME = "ssh_alias"
	HELP = """
ssh_alias-plugin
  create shell aliases for shell

  usage:
	srvmgr ssh_alias srv            create shell alias for the given server or ALL

  bashrc:
	insert the output `srvmgr ssh_alias srv` on .bashrc
	"""

	def __init__ (self, conf, args):
		self.conf = conf
		self.args = args

	def run(self):     
		srvs = self.conf.get_servers(self.args[0])
		
		for srv in srvs:
			users = ['root']
			services = []

			if 'user' in srv:
				users = ['root', srv['user']]

			if 'services' in srv:
				services = srv['services']
			services.append(None)

			for u in users:
				for sr in services:
					alias = srv['name'] 
					if u == 'root' and len(users) > 1:
						alias += '.root'

					opts = ''
					if sr != None:
						alias += '.' + sr
						ports = self.conf.get_service(sr)
						if type(ports) == int:
							opts += ' -L%d:127.0.0.1:%d' % (ports, ports)
						else:
							opts += ' -L%d:127.0.0.1:%d' % (ports[0], ports[1])

					cmd = 'ssh %s@%s %s' % (u, srv['host'], opts)

					print ("alias %s='%s'" % (alias, cmd))