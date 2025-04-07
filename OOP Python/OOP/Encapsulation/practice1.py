# class student:
#     # constructor
#     def __init__(self,name,mark1,mark2,mark3):
#         self.name = name
#         self.mark = mark1
#         self.mark = mark2
#         self.mark = mark3
    
#     # method
#     def av(self):
#         average = (self.mark + self.mark + self.mark) / 3
#         print(f"The avarege of 3 subject of {self.name}'s mark is {average}")


# s1 = student('Roney',45,65,464)
# s1.av()










# class student:
#     # constructor
#     def __init__(self,name,mark=[]):
#         self.name = name
#         self.mark = mark
    
#     # method
#     def av(self):
#         average = (self.mark[0] + self.mark[1] + self.mark[2]) / 3
#         print(f"The avarege of 3 subject of {self.name}'s mark is {average:.2f}")


# marks = [45,65,456]
# s1 = student('Roney',marks)
# s1.av()
        
        
        






# class student:
#     # constructor
#     def __init__(self,name,mark):
#         self.name = name
#         self.mark = mark
    
#     # method
#     def av(self):
#         sum = 0
#         for i in self.mark:
#             sum+=i
            
#         average = sum / 3
#         print(f"The avarege of 3 subject of {self.name}'s mark is {average:.2f}")


# marks = []
# val = input("Enter the value: ").split()
# for i in val:
#     marks.append(int(i))

# s1 = student('Roney',marks)
# s1.av()



import sys


name = "roney"
name2 = 'A'
none_value = 28
none_value2 = None
print(sys.getsizeof(none_value))  # Output: 16 bytes
print(sys.getsizeof(none_value2))  # Output: 28 bytes
print(sys.getsizeof(name))  # Output: 28 bytes
print(sys.getsizeof(name2))  # Output: 28 bytes
