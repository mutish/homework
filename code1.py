# start
a = int(input("Enter a value"))
b = int(input("Enter a value"))
print(a, b)
if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
# stop

# OR

# start
c = int(input("Enter a value"))
d = int(input("Enter a value"))
print(c)
print(d)
if c > d:
    print("c is greater than d")
else:
    print("d is greater than c")
# stop

def compare_numbers(a, b):
    if type(a) == int and type(b) == int:
        if a == b:
            return "a and b are equal"
        elif a > b:
            return  "a is greater than b"
        else:
            return "b is greater than a"
    else:
        return "invalid input"

a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
