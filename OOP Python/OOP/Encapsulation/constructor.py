class student:
    id = None
    name = ""
    
    # default construct
    def __init__(self,id=None,name=""):
        if id is None or name == "":
          print("I am default constructor...")
        else:
          self.id = id
          self.name = name
    
    # parameterized constructor
    # def __init__(self,id,name):
        
    
    # display function
    def display(self):
        print(self.id,self.name)



# create an object
# st1 = student()
# st = student(98,"roney")

# st.display()













class triangle:
    base = None
    height = None
    
    # constructor
    def __init__(self,base,height):
       self.base = base
       self.height = height
    
    # calculate area
    def Area(self):
        area = 0.5*self.base*self.height
        print("The area of triangle:",area)


t1 = triangle(10,20)
t2 = triangle(20,30)

# t1.Area()
# t2.Area()











class student1:
    # constructor
    def __init__(self,fullname):
        self.name = fullname
        print("I am default constructor")


s1 = student1("roney")
s2 = student1("ahammed")
print(s1.name)
print(s2.name)

