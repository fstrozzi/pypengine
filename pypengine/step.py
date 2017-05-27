class Step():

    def __init__(self,name,run,cpu,mem,nodes,pre,multi=None):
        self.name = name
        self.run = run
        self.cpu = cpu
        self.mem = mem
        self.nodes = nodes
        self.prerequisite = pre
        self.multi = multi

    def multiSample(self):
        if self.multi == None:
            return False
        else:
            return True

    def has_prerequisite(self):
        if self.pre == None:
            return False
        else:
            return True

