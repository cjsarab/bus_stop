class BusStop:
    def __init__(self, name):
        self.name = name
        self.queuelength = []
    
    def queue_length(self):
        return len(self.queuelength)

    def add_to_queue(self, person):
        self.queuelength.append(person)

    def clear(self):
        self.queuelength.clear()

    