# store following word meaning in a python dictionar
"""
     table : " a piece of furniture ", " list of facts & fiqures"
     cat : " a small animal "
"""


# dict = {
#     'table' : [" a piece of furniture ", " list of facts & fiqures"],
#     'cat' : 'a small animal'
# }

# print(dict)





# my_dict = {}

# for i in range(3):
#     key = input("Enter the keys: ")
#     val = input("Enter the values: ")  
    
#     my_dict[key] = val

# print(my_dict)








# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks
# ad value

# my_dict = {}
# for i in range(3):
#     key = input("Enter the movie as key: ")
#     val = input("Enter the movies name as value: ")
    
#     my_dict[key] = val

# for key,val in my_dict.items():
#     print(f'{key} : {val}')




my_dict = {}
for i in range(3):
    key = input("Enter the subject: ")
    val = input("Enter the marks: ")
    my_dict.update({key:val})

print(my_dict)