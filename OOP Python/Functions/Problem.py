# WAP to print the length of a list

# def length(lst):
#     print("the length of list is: ",len(lst))

# my_list = []
# val = input("Enter the val: ").split()
# for i in val:
#     my_list.append(i)

# length(my_list)










# WAP to print the element of a list in a single line
# def length(lst):
#     for i in lst:
#         print(i,end=" ")
# my_list = input("Enter the val: ").split()
# length(my_list)






# WAP to USD TO TK
# def converter(USD):
#     TK = USD*122.25
#     INR = USD*85.83
#     PAK = USD*281.45
    
#     choice = input("Enter which rate you want to know: ")
#     match choice:
#         case 'TK':
#             print(TK)
#         case 'INR':
#             print(INR)
#         case 'PAK':
#             print(PAK)
#         case _:
#             print("Invalid currency.Try again")



# USD = int(input("Enter the amound of USD: "))
# converter(USD)





# WAF to print the even or odd
def even_odd(num):
    if(num % 2 == 0):
        print("EVEN")
    else:
        print("ODD")


num = int(input("Enter the number: "))
even_odd(num)