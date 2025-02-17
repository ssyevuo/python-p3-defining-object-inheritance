class Vehicle:
    
    #def __init__ wheel_size and wheel_number are attributes 
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    # definition of the instance method go
    def go(self):
        return "vrrrrrrrooom!"
    
    # definition of the instance method fill_up_tank
    def fill_up_tank(self):
        return "filling up!"
