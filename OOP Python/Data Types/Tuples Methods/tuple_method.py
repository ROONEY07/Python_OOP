my_tuple = (12,3,4,5,6,77)
index = my_tuple.index(12)
count = my_tuple.count(3)
# print(index)
# print(count)




# WAP to count the numbers of students with 'A' grade in the following tuples
my_ty = ('C','D','A','A','B','B','A')
countGrade_A = my_ty.count('A')
print(countGrade_A)



# WAP to store the above values in a list and sort them from 'A' to 'D'
my_list = list(my_ty)
my_list.sort()
print(my_list)



countries = ('spain','Italy','india','England','Germany')
tmp = list(countries)
tmp.append("Bangladesh")
print(tmp)
print(type(countries))