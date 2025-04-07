student = {"name" : "john", "age" : 25, "Grade" : 'A+'}
# print(student)
# print(student.keys())
print(student.values()) 
print(type(student.values()))
for key, val in student.items():
    print(key, ":", val)
