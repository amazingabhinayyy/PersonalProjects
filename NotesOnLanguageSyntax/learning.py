#https://www.learnpython.org/en/Modules_and_Packages
# 
# #classes and objects
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)
myobjectx.function()

class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'
#init is basically a constructor 

#Strings
# astring.split(" ")
# in a normal print: print("Hello, %s!" % name) 
# with multiple: print("%s is %d years old." % (name, age))
# index(index)
# count(letter)
# astring[3:7] to substring it, can step by doing [3:7:2] 
# reverse a string by doing [::-1]
# upper(), lower()
# boolean startswith(string), boolean endswith(string)

# Conditionals 
# and exists - if name == "john" and age == 23:
# in exists - if name in ["name1", "name2"]
# is operator matches instances, so 
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False
# not exists 

# for loops
# for variable in list:
# for x in range(5) - generates 0 - 4
# for x in range(3,8,2) starts at 3 steps by 2 until 7 
# while loops are the same
# berak statements exist out of a loop, continue skip block of code and returns to the loop 

# list methods
# append to add to end (var)
# insert to add wherever (index, var)
# remove(var)
# clear()
# pop()
# sort() - sort list in place

# index(index)
# 50 in numbers = False
# count(var)
# reverse()
# copy()
# can do [1, 2, 3] *3 to repeat the list 3 times

# functions
def my_function():
    print("Hello From My Function!")
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
def sum_two_numbers(a, b):
    return a + b

#tuples
# declared like (1,2,3) are read only, count and index methods
# coordiates = (1,2,3)
# x,y,z = coordinates 
# also for Lists

#Dictionaries 
phonebook = {}
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
#how to delete dictionary entreis
del phonebook["John"]
phonebook.pop("John")

#how to delete dictionary entreis
print(phonebook)
#either this notation phonebook["John"] = 938477566
#or this one "John" : 938477566,
#iterate using the items method, 
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))


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

#Writing modules

#mygame/game.py

#mygame/draw.py

#The Python script game.py implements the game. It uses the function draw_game from the file draw.py
#Modules are imported from other modules using the import command. 

# game.py
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
# draw.py looks like this

def draw_game():
    ...

def clear_screen(screen):
    ...

from draw import draw_game
#importing specific functions from another class
def main():
    result = play_game()
    draw_game(result)

#from draw import * imports everything rom draw


#Direcotry searching
import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))