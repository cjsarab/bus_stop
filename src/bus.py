class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengercount = 0

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return self.passengercount

    def pick_up(self, person):
        self.passengercount += 1

    def drop_off(self, person):
        self.passengercount -= 1

    def empty(self):
        self.passengercount = 0

    def pick_up_from_stop(self, bus_stop):
        self.passengercount = bus_stop.queuelength