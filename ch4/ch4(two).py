# Write a program to store seven markss in a list entered by the user.
marks = []
first = int(input("enter the first marks :"))
marks.append(first)
second = int(input("enter the second marks :"))
marks.append(second)
third = int(input("enter the third marks :"))
marks.append(third)
fourth = int(input("enter the fourth marks :"))
marks.append(fourth)

marks.sort()
print(marks)