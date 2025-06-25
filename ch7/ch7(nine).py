# Write a program to print the following star pattern.
# * * *
# *   *       for n = 3
# * * *

number = int(input("enter the number:"))
for i in range(1, number + 1):
    if i == 1 or i == number:
        print("* " * number)
    else:
        print("*" + " " * (2 * (number - 2) + 1) + "*")
