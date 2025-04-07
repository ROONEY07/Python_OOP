# WAP to ask the user to enter names of their 3 favorite movies and store  them in a list

# movies = input("Enter the movies name: ").split()
# movie = []a
# for i in movies:
#     movie.append(i)
# print(movie)



# movie = []
# for i in range(1,3):
#     i = input(f"Enter the {i}st movies name: ")
#     movie.append(i)

# print(movie)


movie = []
# movie.append(input("Enter the 1st movie: "))
# movie.append(input("Enter the 2nd movie: "))
# movie.append(input("Enter the 4th movie: "))
# print(movie)







# WAP to check if a contains a palindrome of elements
my_list = []
userInput = input("Enter the values: ").split()
for i in userInput:
    try:
        i = int(i)
    except ValueError:
        try:
            i = float(i)
        except ValueError:
            i = str(i)
    my_list.append(i)


my_list2 = my_list.copy()
my_list2.reverse()


if my_list2 == my_list:
    print("Same")
else:
    print("NOT")

print()
print(my_list)
print(my_list2)