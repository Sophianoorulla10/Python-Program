try:
    a=int(input("enter first num:"))
    b=int(input("enter second num:"))
    c=a/b
except ZeroDivisionError:
    print("can't divide by zero")
else:
    print("successfully done")
          
