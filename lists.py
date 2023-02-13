# used to store multiple values in a single variable
shoppingBasket = ["kales", "flour", "oranges","kales", "flour", "oranges "]
#features on lists
3#ordered : changeable and allow duplicate values
# indexed : start counting from zero
# can be accesed added or removed

print(shoppingBasket[0]) #
print(shoppingBasket[-1]) #-ve indexing : start frm end
print(shoppingBasket[2:5]) # ranges use position flow, only removing elements in the start position
print(shoppingBasket[:4]) # returns the first n elements
print(shoppingBasket[2:]) # removes the first n elements
print(shoppingBasket[-4:-2])

#checking if items exist in a list
x = input("check basket")
if x in shoppingBasket:
    print("yes" + x + "in basket")
else:
    print("no" + x + "in basket")

#changing a list of otems
shoppingBasket[1:4] = ['apples', 'oranges', 'Juice']
print(shoppingBasket)

# to change is to also insert
shoppingBasket.insert(0, "Spinach")
print(shoppingBasket)
#how to add/ insert
#refernce the index and new value
#append
shoppingBasket.append("cereals")
print(shoppingBasket)

#to extend is also to add
toolShopping = ['hammer', 'screws', 'panga']
shoppingBasket.extend(toolShopping)
print(shoppingBasket)
#you can also add other iterables
tupleExample = ('kiwi', 'gel')
shoppingBasket.extend(tupleExample)
print(shoppingBasket)

#removing lists
#1 remove method
shoppingBasket.remove("flour")
print(shoppingBasket)
#2 pop up + index
shoppingBasket.pop(1)
#if index is not specified the last item is removed
shoppingBasket.pop()
print(shoppingBasket)
#3 del key
del shoppingBasket[2]
print(shoppingBasket)
#4 empty basket
shoppingBasket.clear()
print(shoppingBasket)


