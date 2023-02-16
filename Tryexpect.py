# # try, expect else finally
# try: allows u to test a block of code for errors
# except : handling the errors
# else: no error executed in the code
# finally : runs regardless of any error

# Exception handling
x = -1
try:
    print(x)
except:
    print("an error occurred, check if x is defined")
else:
    print(str(x) + " from else")
finally:
    print("Finally block")

# raise  : works with a condition if condition is met , raise an error message
if x < 0:
    raise TypeError("sorry x shouldn't be less than zero")