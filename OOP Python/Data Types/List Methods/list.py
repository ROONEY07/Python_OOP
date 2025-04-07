n = int(input("Enter the values: "))
list1 = []

for i in range(n):
    useInput = input("Enter the list value (id name salary): ").split(" ")
    
    try:
        # Attempt to convert the input into appropriate types (int, string, float)
        id = int(useInput[0])  # Convert first value to int
        name = useInput[1]  # Name is a string
        salary = float(useInput[2])  # Convert salary to float
        
        # Append as a tuple (id, name, salary)
        list1.append((id, name, salary))  # Append tuple to list
    except ValueError:
        print("Invalid input. Please ensure the ID is an integer and the salary is a float.")

print(list1)



nameList = ['Harsh','Pratik','Bob']
print(nameList[1][-1])