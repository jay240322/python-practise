# Write a python program using function to convert Celsius to Fahrenheit.

def c_to_f(c):
    return (c*9/5)+32

c = int(input("enter the celsius :"))
print(f"{c_to_f(c)}","Fahrenheit")


# °F = (°C * 9/5) + 32