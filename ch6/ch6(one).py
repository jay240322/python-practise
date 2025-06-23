# Write a program to find the greatest of four numbers entered by the user.
a1 = int(input("enter the first number :"))
a2 = int(input("enter the first number :"))
a3 = int(input("enter the first number :"))
a4 = int(input("enter the first number :"))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greates",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greates",a2)
elif(a3>a1 and a3>a4 and a3>a1):
    print("a3 is greates",a3)
else:
    print("a4 is greates",a4)
