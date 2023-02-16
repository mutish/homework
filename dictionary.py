# used to store items in key and value pairs
# features : r changeable and ordered and dont allow duplicates
# shoppingDictionary = {
#     "item1" : 5,
#     "item2" : "milk",
#     "item3" : "flour",
# }
shoppingDictionary = {
    "item1" : "Bread",
    "item2" : "milk",
    "item3" : "Flour",
}
# get length of the dictionary
print(len(shoppingDictionary))

# access is done by referencing the key name inside[]
print(shoppingDictionary["item2"])

x = shoppingDictionary.get("item3")
print(x)
#to get keys :
x = shoppingDictionary.keys()
print(x)
# get all values
print(shoppingDictionary.values())
# items method : returns @ item as tuples in a list
print(shoppingDictionary.items())
#check if keys exist in a dictionary
check = "item7"
if check in shoppingDictionary:
    print("yes, the item is there ")
else:
    print("no, item does not exist ")

# updating....
shoppingDictionary["item3"] = "salt"
print(shoppingDictionary)
# inbuilt method
shoppingDictionary.update({"item2" : "flour"})
print(shoppingDictionary["item2"])

#add
shoppingDictionary["item4"] = "sugar"
#update can also be used to add
shoppingDictionary.update({"item5" : "eggs"})
print(shoppingDictionary.values())

# removing items
# 1. POP method
shoppingDictionary.pop("item5")
print(shoppingDictionary.values())
# pop item removes any random item
shoppingDictionary.popitem()
print(shoppingDictionary.values())
del shoppingDictionary["item1"]
print(shoppingDictionary.values())
# to empty
shoppingDictionary.clear()
print(shoppingDictionary.values())

#copy a dictionary
copyDictionary = dict(shoppingDictionary)
dictDictionary = dict(shoppingDictionary)
print(copyDictionary)
print(dictDictionary)

# myFamily = {
#     "child1" : {
#         "name" : "Stacey"
#                  "age" : "18"
# },
#    "child2": {
#     "name": "Kyla"
#             "age": "8"
# },
# "child3": {
#     "name": "Coi"
#             "age": "16"
# },
#
# }
# print(myFamily["child2"]["name"])
# print(myFamily["child3"]["name"]["age"])
# # access to nested dictionaries
# # say we wanted name info on child two
# # reference child 2 using the key and then get the details you want using the key
# print(myFamily["child2"]["name"])
# print(myFamily["child3"]["name"]["firstname"])
