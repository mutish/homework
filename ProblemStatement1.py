def simple_calculator(var1 = 45, var2 = 45):
    if var2 == 0:
        print("Error!")
    else:
        total = var1 + var2
        diff = var1 - var2
        multi = var1 * var2
        quo = var1 / var2


        print(total)
        print(diff)
        print(multi)
        print(quo)
        if var1 == var2:
            print("var1 is equal to var2")
        return


var1 = int(input(" Enter value "))
var2 = int(input(" Enter value"))

print(simple_calculator(var1, var2))

def calculator(c, d):
    if type(c) == int and type(d) == int:
        sum = c + d
        difference = c - d
        multiplication = c * d
        if d == 0:
            return "division by zero not allowed"
        else:
            division = c / d
            if c == d:
                return "a and b are equal\nsum: {}\nproduct: {}\ndivision: {}".format(sum, difference, multiplication, division)
            else:
                return "sum: {}\nproduct: {}\ndivision: {}".format(sum, difference, multiplication, division)

    else:
        return "invalid input"

c = int(input("enter c: "))
d = int(input("enter d: "))
print(calculator(c, d))