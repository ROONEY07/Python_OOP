X = 5
class Triangle:
    weight = None
    height = None
    
    # constructor
    def __init__(self,weight,height):
        self.weight = weight
        self.height = height
    
    # print the area
    def Area(self):
        area = 0.5*self.weight*self.height
        print("The area of triangle:",area)
    
    
# declare an object
# weight = int(input("Enter the weight: "))
# height = int(input("Enter the height: "))
# t = Triangle(weight,height)
# t.Area()


class car:
    wheels = 4
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def print_val(self):
        A = 15
        print(A)
    
    def display(self):
        print("Car brand is:",self.brand,"and model is",self.model)

print(X)
C = car("toyota","CHR")
C.print_val()
C.display()
print(car.wheels)
print(C.wheels)