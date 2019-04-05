import sys
import os
import subprocess
import getopt
from .plugin import Plugin

def ping(s):
	p = subprocess.run(["ping", "-c", "1", s['host']], stdout=subprocess.PIPE)
	out = p.stdout.decode('ascii')
	try:
		out.index('100.0% packet loss')
		return 'offline'
	except:
		return out.split('time=')[1].split('\n')[0]


def cpu(s):
	if 'user' in s:
		user = s['user']
	else:
		user = 'root'

	c = "grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage \"%\"}'"
	p = subprocess.run(["ssh", user+'@'+s['host']] + c.split(' '), stdout=subprocess.PIPE)
	return p.stdout.decode('ascii').replace('\n', '')[0:4] + '%'



def mem(s):
	if 'user' in s:
		user = s['user']
	else:
		user = 'root'

	c = "free | grep Mem | awk '{print $3/$2 * 100.0}'"
	p = subprocess.run(["ssh", user+'@'+s['host']] + c.split(' '), stdout=subprocess.PIPE)
	return p.stdout.decode('ascii').replace('\n', '')[0:4] + '%'


def disk(s):
	if 'user' in s:
		user = s['user']
	else:
		user = 'root'

	c = "df --output=pcent /"
	p = subprocess.run(["ssh", user+'@'+s['host']] + c.split(' '), stdout=subprocess.PIPE)
	return p.stdout.decode('ascii').split('\n')[1].replace(' ', '')


class StatusPlugin (Plugin):
	NAME = "status"
	HELP = """
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
	"""

	STATS = {
		"ping": ping,
		"cpu": cpu,
		"disk": disk,
		"mem": mem
	}

	def __init__ (self, conf, args):
		self.conf = conf
		self.args = args


	def run(self):
		srvs = self.conf.get_servers(self.args[0])
		if len(self.args) >= 2:
			what = self.args[1].split(',')
		else:
			what = ['ping', 'cpu', 'disk', 'mem']

		template = "{host:20}| {ip:18}"
		for x in what:
			template += "| {%s:10}" % x

		print(template.format(
			host="HOST", ping="PING", ip="IP", cpu="CPU", disk="DISK", mem="MEM"
		))

		for x in srvs:
			values = {
				"host": x['name'],
				"ip": x['host']
			}

			for w in what:
				if w in self.STATS:
					values[w] = self.STATS[w](x)
			
			print (template.format(**values))