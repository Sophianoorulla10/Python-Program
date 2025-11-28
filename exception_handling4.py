try:
    a=int(input("enter the first num:"))
    b=int(input("enter the second num:"))
    c=a/b
except ValueError:
    print("Invalid input:")
except ZeroDivisionError:
    print("cant't divide by zero")
    
