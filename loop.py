#repeat tasks based on condition
#WHILE loop
# print 1-6
start = 1
# while start < 7:
#     print(start)
#     start += 1
    # to stop a loop make the condition false
    #special statements
    #BREAK: allows us to stop the loop even wen the condition is true
    #eg

while start < 7:
    print(start)
    if start == 3:
        break
        start += 1

# CONTINUE
start = 0
while start < 6:
    start += 1
    if start == 3:
        continue
        print(start)

    # ELSE
start = 1
while start < 7:
    print(start)
    start += 1
else:
    print("start is longer than 6")


# FOR LOOP
fruits = ["apple","banana", "cherry"]
tupleFriut = ("apple","banana", "cherry")
for x in fruits:
    if x == "apple":
        print("i have reached apple")
    else:
        print(x)
for x in tupleFriut:
    print(x)

#loop in string
for x in "Joseph":
    print(x)

# range function











































