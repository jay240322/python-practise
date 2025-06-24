# Write a program to print the following star pattern:
# *
# **
# *** for n = 3

number = int(input("enter the number :"))
for i in range(1,number+1):
     print("*"*i,end=" ")   #this for print the *
     print(" ")