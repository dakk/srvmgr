import sys
from . import Config
from .plugins import PluginRepository, SSHPlugin, ConfPlugin, StatusPlugin

# srvmgr status * --realtime
# srvmgr ssh hb.blog
# srvmgr ping *

def main():
	conf = Config()
	conf.load()

	pr = PluginRepository(conf)
	pr.register(SSHPlugin)
	pr.register(ConfPlugin)
	pr.register(StatusPlugin)

	pr.handle(sys.argv[1::])


	"""
	try:
		opts, args = getopt.getopt(sys.argv[1:], "VD:v:h", ["help"])
	except getopt.GetoptError:
		usage()
		sys.exit ()

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage ()
			sys.exit ()
	"""

