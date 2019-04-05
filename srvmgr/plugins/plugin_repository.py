class PluginRepository:
    def __init__(self, conf):
        self.plugins = {}
        self.conf = conf

    def register(self, c):
        self.plugins[c.NAME] = c

    def help(self):
        for v in self.plugins:
            p = self.plugins[v]
            print (p.HELP)

    def handle(self, args):
        if len(args) == 0:
            return self.help()

        if args[0] in self.plugins:
            pl = self.plugins[args[0]](self.conf, args[1::])
            pl.run()
        else:
            return self.help()