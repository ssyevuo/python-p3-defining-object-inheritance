from vehicle import Vehicle

# class Car is a subclass of Vehicle hence car inherits from Vehicle
class Car(Vehicle):
    # overwriting the inherited methods from Vehicle
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"