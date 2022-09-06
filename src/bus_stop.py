class BusStop:
    def __init__(self, name):
        self.name = name
        self.queuelength = 0
    
    def queue_length(self):
        return self.queuelength

    def add_to_queue(self, person):
        self.queuelength += 1

    def clear(self):
        self.queuelength = 0

    