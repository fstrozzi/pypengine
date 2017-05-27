import uuid

class Job():

    def __init__(self,name):
        self.name = uuid.uuid4().hex().split("-")[0] + "-"+name
        self.steps = []
        self.cpu = 1
        self.nodes = 1





