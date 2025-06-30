#class Point():
    # The __init__ method is a special method, also known 
    # as the constructor. It is automatically called when a 
    # new object(instance) of the class is created.
    
#    def __init__(self, input1, input2):
#        self.x = input1
#        self.y = input2
        
#p = Point(2, 8)
#print(p.x)
#print(p.y)

class Flight():    
    def __init__(self, capacity):
        self.capacity = capacity
        # this line of code will create an empty list []
        self.passengers = []
    
    def add_passenger(self, name):
        # This will check if there are open seats
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
