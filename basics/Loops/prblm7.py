while True:
    number = int(input("enter a value between 1 and 10: "))
    if 1 <= number <= 10:
        print("this is a valid number")
        break
    else:
        print("invalid number, try again")