"""
Slicing

aita ke python er slicing bole, er syntax hocche               ->    str[start:stop:step]
R ::  -> er rule hoche 
aita start and stop ke ignore kore step unijaie jabe orthatr.  ->    str[::step]
   
"""


string = "python"
result = string[::-3] 

# python slicing
# str[start:stop:step]
# str[::step]
print(result)






###############




s1 = "python"
s2 = s1[::-1]
s3 = " ".join(reversed(s1))

# join() method is used to join (combine) elements of an iterable (like a list, tuple, or set) into a single string. 
# It’s typically used to concatenate strings with a specified separator.

print(s2)
print(s3)
print(s2 == s3)