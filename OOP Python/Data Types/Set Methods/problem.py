# Yor are given a list of subjects for students . Assumes one classroom is required for 1 subject. How many classrooms are needed by all students
"""
    'python' , 'java', 'C++', 'python', 'javaScript', 'java' , 'python', 'java', 'C++','C' 
"""

# sub = input("Enter a subjects: ").split()
# my_set = set()
# for i in sub:
#     my_set.add(i)

# print(my_set)
# print("the required classroom is: ",len(my_set))









# Fiqure out a way to store 9 and 9.0 as separate values in the set

# val = (input("Enter the value: ").split())
# my_set = set()

# for i in val:
#     try:
#         i = int(i)
#     except ValueError:
#         try:
#             i = float(i)
#         except ValueError:
#             i = str(i)
#     my_set.add(i)
# print(my_set)


my_tuple = (('int',9),('float',9.0))
my_set = set()
my_set.update(my_tuple)
print(my_set)