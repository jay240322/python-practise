# Write a python function which converts inches to cms.
def in_to_cm(inch):
    return inch * 2.54

n = int(input("enter the inch :"))
print(f"the inch {n} to cm is :{in_to_cm(n)}")