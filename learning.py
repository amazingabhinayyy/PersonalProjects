# list methods
# append to add to end (var)
# insert to add wherever (index, var)
# remove(var)
# clear()
# pop()
# sort()
# index(index)
# 50 in numbers = False
# count(var)
# reverse()
# copy()

#tuples
# declared like (1,2,3) are read only, count and index methods
# coordiates = (1,2,3)
# x,y,z = coordinates 
# also for Lists

#Key Value Pair
customer = {
    "name": "John Smith",
    "age": 30,
    "is verififed": True
}
#customer["name"] returns John Smith
# get method, 
# can add eys by doing customer[bday] = "blah"

numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}


num = input("Enter a number: ")
str = ""
for letter in num:
    str += numbers[letter] + " "
print(str)