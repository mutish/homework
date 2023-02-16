# a variable is only available in the region it has been created
# local & global scope
# 
# local scope : variables created inside function
def sampleMethod():
    global y
    x = 100
    y = 200
    return x + y

print(sampleMethod())

# what of a scope when a function is inside a funcyion
def sampleFunction():

    def innerFunction():
        print(y)
        return innerFunction()

sampleFunction()