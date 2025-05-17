class Point():
    # The __init__ method is a special method, also known 
    # as the constructor. It is automatically called when a 
    # new object(instance) of the class is created.
    
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
        
p = Point(2, 8)
print(p.x)
print(p.y)
