import uuid
from collections import OrderedDict

class Job():

    def __init__(self,steps):
        name = ""
        if len(steps) > 1:
            name = "-".join(steps)
        else:
            name = steps[0]
        self.name = str(uuid.uuid4()).split("-")[0] + "-"+name
        self.cpu = 1
        self.nodes = 1
        self.steps = OrderedDict()

