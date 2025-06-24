# Write a program to calculate the factorial of a given number using for loop.
number = int(input("enter the number:"))
product = 1
for i in range(1,number+1):
    product = product * i 

print(f"the factorial of the {number} is {product}") 