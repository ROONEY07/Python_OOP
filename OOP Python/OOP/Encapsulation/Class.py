"""
class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute

    def _greet(self):   # Protected method
        print(f"Hello, my name is {self._name} and I am {self._age} years old.")

p = Person("Alice", 30)
print(p._name)  # Technically accessible, but discouraged
p._greet()  # Technically accessible, but discouraged

"""



class student:
    id = ""
    Name = ""
    
    def display(self):
        print(self.id)
        print(self.Name)
        
class student2:
    name = "arman"


class Student3:
    id = 56
    age = 2345

st = student()
st2 = student2()
st3 = Student3()


# st.id = 94
# st.Name = "ROney"

# st.display()                                                                                                                                                          
# print(st2.name)

# print(st3.age,st3.id)



class area:
    weight = None
    Height = None
    
    # constructor
    def __init__(self, weight,Height):
        self.weight = weight
        self.Height = Height
        
    # declare e function/method for display
    def display(self):
        Area = self.weight * self.Height
        print("The area is:",Area)
    
A = area(56,65)
# A.display()






class Student:
    collage_name = "MKC college"
    
    # constructor
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    
    # function
    def welcome(self):
        print("Welcome to our collage")
    
    # get marks
    def get_marks(self):
        return self.mark


s1 = Student("roney",58)
s1.welcome()
print(s1.get_marks())
print(s1.collage_name)
        



