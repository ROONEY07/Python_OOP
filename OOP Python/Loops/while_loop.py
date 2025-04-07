# print the number from 1 to 100
i = 1
while i<=100:
    # print(i)
    i+=1    


# print the number from 100 t0 1
j = 100
while j>=1:
    # print(j)
    j-=1



# print the multiplication table of n
# n = int(input("Which multiplication table you want: "))
i = 1
while i <= 10:
    # print(n,"*",i,"=",i*n)
    i+=1



# print the element of the following list using loop
# list = [1,4,9,16,25,36,49,64,81,100]

list1  = [1,4,9,16,25,36,49,64,81,100]

a = 0
while a <= len(list1)-1:
    # print(list1[a],end=" ")
    a+=1
# print("\nThe length of list:",len(list1))




# search the number x in this tuple using loop
tu = (1,4,9,16,25,36,49,64,81,25,100)
# x = int(input("Enter the number to Search: "))
i = 0
# while i < len(tu):
    # if tu[i] == x:
        # print("found on",i)
    # else:
        # print("Finding.....")
    # i+=1





# print the all even numbers: 
i = 1
while i<=10:
    if i%2==0:
        i+=1
        continue
    # print(i)
    i+=1


a = 1
while a<=10:
    # print(a,end=" ")
    a+=1
# else:
    # print("\nloop is end")







# WAP to find the sum of first n numbers
n = int(input("Enter the numbers: "))
i = 1
sum = 0
while i<=n:
    sum+=i
    i+=1
print("sum of first n numbers:",sum)




