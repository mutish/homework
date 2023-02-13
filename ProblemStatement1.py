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
