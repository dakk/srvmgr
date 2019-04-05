import sys
import os
import getopt
from .plugin import Plugin

class SSHPlugin (Plugin):
	NAME = "ssh"
	HELP = """
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
	"""

	def __init__ (self, conf, args):
		self.conf = conf
		self.args = args

	def run(self):     
		exc = None  
		service = None 
		port = None
		srv = self.conf.get_server(self.args[0])
		if not srv:
			print ('server %s not found' % self.args[0])
			return

		if 'user' in srv:
			user = srv['user']
		else:
			user = 'root'

		try:
			opts, args = getopt.getopt(self.args[1:], "rs=e=u=p=", ["root", "service=", "exec=", "user=", "port="])
		except getopt.GetoptError:
			print (SSHPlugin.HELP)
			sys.exit ()

		for opt, arg in opts:
			if opt in ("-r", "--root"):
				user = 'root'
			elif opt in ("-s", "--service"):
				service = arg
				if srv['services'].index(service) == -1:
					print ('service %s not available in %s' % (service, srv['name']))
					return	
			elif opt in ("-p", "--port"):
				port = int(arg)
			elif opt in ("-u", "--user"):
				user = arg
			elif opt in ("-e", "--exec"):
				print (opt, arg)
				exc = arg

		opts = ''
		if service:
			ports = self.conf.get_service(service)
			if type(ports) == int:
				opts += ' -L%d:127.0.0.1:%d' % (ports, ports)
			else:
				opts += ' -L%d:127.0.0.1:%d' % (ports[0], ports[1])

		if port:
			opts += ' -p ' + str(port)

		if exc:
			opts += " '%s'" % exc

		cmd = 'ssh %s@%s %s' % (user, srv['host'], opts)
		print(cmd)
		os.system(cmd)