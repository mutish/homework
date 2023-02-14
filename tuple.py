# tuples allow us to store multiple values in a single variable
# are unchangeable
# defined with round brackets
shoppingTuple = ("Bread", "Sugar", "Salt")
print(shoppingTuple)
# are indexed : start at 0
# allow duplicates.
# one can get the length of the tuple
print(len(shoppingTuple))
#tuple with one item
tupleOne = ("Bread",)
# can have items of the same / diff data types
tuple1 = (1, 5, 6,7)
tuple2 = ("string", 1, True, False, "another string")
type(tuple1)
# Accessing a tuple
# access is done by reference to the index number
print(shoppingTuple[1])
# checking if an item is a tuple
search = "milk"
if search in shoppingTuple:
    print("yes")










# Updating a tuple
# to add, remove or change :
# convert the tuple to a list
tempList = list(shoppingTuple)
print(shoppingTuple)
shoppingTuple = tuple(tempList)
print(shoppingTuple)

# add items
tempList.append("flour")
shoppingTuple = tuple(tempList)
print(shoppingTuple)
# add a tuple to a tuple
tuple3 = ("Oranges",)
shoppingTuple += tuple3
print(shoppingTuple)
tempList = shoppingTuple
