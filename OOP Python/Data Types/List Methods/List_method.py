# add the single value to -> append()
my_list = [1,2,3,4,5]
my_list.append(6)
# print(my_list)




my_val = ['abcd']
my_val2 = []
for i in my_val:
    for char in i:
        my_val2.append(char)
print(my_val2)



# add the complete list into another list
my_list.extend(my_val2)
print(my_list)


# insert value into list
# my_list[4] = 100
my_list.insert(4,100)
print(my_list)


#pop the value from the list
my_list.pop()
my_list.pop(4)
print(my_list)