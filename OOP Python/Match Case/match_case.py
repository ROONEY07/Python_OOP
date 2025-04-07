value = 10
match value:
    case 5:
        print(f'this value is {value}')
    case 10:
        print(f'this value is {value}')
    case _:
        print("This value is something else")