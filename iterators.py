# enables items to be traversed or looped
mytuple = ("1", "2", 3)
myIterable = iter(mytuple)
print(next(myIterable))
print(next(myIterable))
print(next(myIterable))
x = "Stacey"
myIterable = iter(x)
print(next(myIterable))

#just loop over iterables using a for loop
# create an iterator that returns no starting with 1 and increases with 1