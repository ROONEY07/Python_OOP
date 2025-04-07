mark = int(input("Enter your marks: "))

match mark:
    case mark if mark >= 80:
        print("you have got A+")
    case mark if mark >= 70:
        print('you have got A')
    case mark if mark >= 60:
        print('you have got B+')
    case mark if mark >= 50:
        print('you have got B')
    case mark if mark >= 40:
        print('you have got C')
    case _:
        print("you are fail")


