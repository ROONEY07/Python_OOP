"""
    Python-e membership operators duita ache: in ar not in. Ei operators ta diye apni check korte paren je kono element, list, tuple, string, dictionary, etc. er moddhe ache kina.
    
    1. in operator: 'in' -> operator ta check kore je element ti specific collection (list, tuple, string, etc.) er moddhe ache kina.
    
    
    2. not in operator: 'not in' -> operator ta check kore je element ti specific collection er moddhe nei kina. Eta negation er moto kaj kore.
"""

fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)  # True
print('grape' in fruits)   # False



fruits = ['apple', 'banana', 'cherry']
print('banana' not in fruits)  # False
print('grape' not in fruits)   # True
