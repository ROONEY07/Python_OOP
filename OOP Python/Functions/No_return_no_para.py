def Sort():
    a,b,c = map(int,input("Enter the numbers: ").split())
    my_list = []
    my_list.append(a)
    my_list.append(b)
    my_list.append(c)
    
    my_list2 = my_list.copy()
    my_list.sort()
    
    print("After sort:",my_list)
    print("Before sort:",my_list2)

Sort()