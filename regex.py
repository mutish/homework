# exists as a module
import re
# form a search pattern
text = "it's quite hot today"
# search method
# ^ start with
# $ end with
# * 0 / more occurrences
# , indicates any character
x = re.search("^it.*$", text)
print(x)
# find all
# returns a list containing all possible matches
x = re.findall("raining", text)
print(x)
#split : list where the string has been split at @ match
x = re.split("\t", text)
print(x)
x = re.split("\s",text,1)
print(x)
#sub replaces searched term with a word of choice
x = re.sub("\s","4",text)
print(x)
# match = search