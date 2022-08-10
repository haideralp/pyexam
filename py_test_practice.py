# create a function called user_name
def user_name


#How would you iterate over the following list: arr = [1,2,3,4,5] ?
# display the list with help for the loop and a print statement
arr = [1, 2, 3, 4, 5]
# Iterating list using for loop
for i in list:
    print(i)

# && AND || and and which one is correct boolean/value operator ?

and

#what is the diff between tuple and a list ?

tuple - immutable
list - mutable


#could you add an element to a tuple?

- concatenate to tuple

- modify it by unpacking tupe with *


# Appending to a tuple with list conversion
a_tuple = (1, 2, 3)
a_list = list(a_tuple)
a_list.append(4)
a_tuple = tuple(a_list)
print(a_tuple)
# Returns: (1, 2, 3, 4)

#can you have multiple data in a tuple ?

- You can have multiple data types
eg

# data_type ={'0':0, '1':1, '2':2} what type of data collection is this
- dictionary

# how to create object of a class DevOps():

class Devops:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Devops("Haider", 30)

print(p1.name)
print(p1.age)


# adds 5 to the following list ?
arr = [1,2,3,4]
arr.append(5)
 print(arr)/return arr


# using a function that takes 1 arg, return True if arg is equal to devops, otherwise False.

def course(devops):
    if devops == True
    return True
    else:
    return: false

# how to inherit a class - write correct syntax if you had class Y and Class z- inherit class Z from Y


# how to declare super
super().__init__() # inherit base class

# function should return True if value is contained in [list] at an even index False otherwise.


# create 4 functions that takes 2 args each percentage (value1, value 2) (v1 is percentage if v2), divide, calculate DOB, multiple
#each function MUST RETURN correct mathematical value.


# searching odd an even numbers using a function that an arguments of ints
#using range ()


# create a function to calculate the total value of shopping bill
# shopping_list = {5 items with values in a key value format.
# MUST RETURN the total amount only.

d = {'key1':1,'key2':14,'key3':47}   # d is dictionary of items
values = d.values()    # defining what d.values is.
#Return values of a dictionary
total = sum(values)
return total


def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final