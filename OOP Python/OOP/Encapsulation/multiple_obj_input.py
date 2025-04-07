class Employee:
    id = None
    name = ""
    salary = None
    
    # Constructor
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    # diplay through function
    def display(self):
        print(self.id,self.name,self.salary)

        
    
# to create multiple object and pass the value . we can do it with loop
# em = Employee(98,"Roney",45563.4355)
# em2 = Employee(45,"Rohan",353443.3455)
# em3 = Employee(64,"karim",2453454.345)

n = int(input("Enter the number of object: "))
# create an list for multiple object
employee = []

for em in range(n):
    value = input("Enter the values: ").split(" ") # spit akta list return kore 
    em = Employee(int(value[0]),value[1],float(value[2])) # so indexing korte parbo
    employee.append(em)


# to display more we can do it with loop
# em.display()
# em2.display()
# em3.display()
for em in employee:
    em.display()