import json
import os
import sys

DEFAULT_PATH = os.path.expanduser("~/.srvmgr.json")

class Config:
	def __init__ (self):
		self.servers = []
		self.services = {}

	def load(self, fpath = DEFAULT_PATH):
		try:
			f = open(fpath, 'r')
		except:
			print ('no %s file found, please create one' % fpath)
			sys.exit()

		conf = json.loads(f.read())
		self.servers = conf['servers']
		self.services = conf['services']
		f.close()

	def save(self, fpath = DEFAULT_PATH):
		conf = {'services': self.services, 'servers': self.servers}
		f = open(fpath, 'w')
		f.write(json.dumps(conf))
		f.close()


	def get_servers(self, name):
		if name == 'ALL':
			return self.servers
		else:
			return list(filter(lambda s: s['name'].startswith(name), self.servers))

	def get_server(self, name):
		l = list(filter(lambda s: s['name'] == name, self.servers))
		if len(l) == 1:
			return l[0]
		else:
			return None


	def get_services(self):
		return self.services

	def get_service(self, name):
		if name in self.services:
			return self.services[name]
		else:
			return None