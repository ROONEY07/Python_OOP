my_list = []
Userinput = input("Enter the values: ").split()
for i in Userinput:
    try:
        i = int(i)
    except ValueError:
        try:
            
            i = float(i)
        except ValueError:
            i = str(i)
    my_list.append(i)

print(my_list)
        
    