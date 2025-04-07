
while(True):
    a = input("\nEnter value for a: ")
    b = input("Enter value for b: ")

    try:
        a = int(a)
    except:
        try:    
            a = float(a)
        except ValueError:
            print("Invalid input for a. Please enter a number.")
            continue
        
    try:
        b = int(b)
    except:
        try:    
            b = float(b)
        except ValueError:
            print("Invalid input for a. Please enter a number.")
            continue
        
    choice = input("\nEnter your choice: ")
    if choice == '+':
        add = a+b
        if add is float:
            print(f"\nAddition: {add:.2f}")
        else:
            print("\nAddition:",add)
        
    elif choice == '-':
        sub = a-b
        if add is float:
            print(f"\nSubstruction: {sub:.2f}")
        else:
            print("\nSubstruction:",sub)
            
    elif choice == '*':
        multi = a*b
        if add is float:
            print(f"\nMultiplication: {multi:.2f}")
        else:
            print("\nMultiplication:",multi)
            
    elif choice == '/':
        div = a/b
        if add is float:
            print(f"\nDivision: {div:.2f}")
        else:
            print("\nDivision:",div)
            
    elif choice == '%':
        mod = a%b
        if add is float:
            print(f"\nModulus: {mod:.2f}")
        else:
            print("\nModulus:",mod)
            
    elif choice == '//':
        floorDiv = a//b
        if add is float:
            print(f"\Floor division: {floorDiv:.2f}")
        else:
            print("\nFloor division:",floorDiv)
            
    elif choice == '**':
        expo = a**b 
        if add is float:
            print(f"\nExponentiation: {expo:.2f}")
        else:
            print("\nExponentiation:",expo)
    else:
        print("\nInvalid input, Try again.")
        break