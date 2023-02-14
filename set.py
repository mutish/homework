shoppingset = {"bread", "sugar", "salt"}
print(shoppingset)
print(len(shoppingset))
# setting items
for x in shoppingset:
    print(x)

check = "bread"
print(check in shoppingset)
shoppingset.add("flour")
print(shoppingset)
juiceflavours = {"mango", "passion", "apple"}
shoppingset.update(juiceflavours)
print(shoppingset)
simplelist = ["coconut", "soap", "kiwi"]
simpletuple = ("forks", "spades")
shoppingset.update(simplelist)
shoppingset.update(simpletuple)
print(shoppingset)

shoppingset.remove("spades")
shoppingset.discard("forks")
print(shoppingset)
x = shoppingset.pop()
print(x)
shoppingset.clear()
print(shoppingset)

set3 = {"item5", 5}
set4 = shoppingset.union(set3)
print(set4)

x = {"apple", "banana"}
y = {"microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana"}
y = {"microsoft", "apple"}
z = x.intersection(y)
print(z)

x = {"apple", "banana"}
y = {"microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana"}
y = {"microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

x = {"apple", "banana"}
y = {"microsoft", "apple", "google"}
z = x.symmetric_difference(y)
print(z)


