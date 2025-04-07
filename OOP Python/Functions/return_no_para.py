def min_max():
    my_list = []
    userInput = input("Enter the numbers: ").split()
    for i in userInput:
        my_list.append(int(i))
    
    
    min_val = min(my_list)
    max_val = max(my_list)
    return min_val,max_val


min_val,max_val = min_max()

print("The min value is: ",min_val)
print("The max value is: ",max_val)