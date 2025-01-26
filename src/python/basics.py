print("Hello, World!")
if 5 < 1 :
    print("Hi there wI am working")

# comment can be added with #
if 25 == 25 :
        print("Hi there wI am working")
        x = 5
        y = "I am Prabhu"
        """
        Multiple 
        Line Comment
        """
        print("Hey" + y + " "+str(x))

# Variable Types

x = 21
y = int(x)
z = float(x)
k = str(x)

print(y)
print(z)
print(k)

name1 =  "John"
name2 = 'John'

if name1 ==  name2:
    print(name1)

# Many values to multiple variable

h1,h2,h3 = 1, "Sam" , 'Turkey'
print(h1)
print(h2)
print(h3)

x = y =  z = 'orange'
print(x)
y = 'apple'
fruits  = [x,y,z]
fruits[2] = 'Honey'
print(fruits)

# functions

def add():
    print(5 + 6)

add()

global schoolName
schoolName=  'Renuga'


def printGlobal():
 print(schoolName)

printGlobal()

'''
Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType
'''

# getting Data type

print(type(schoolName))

# Data type Example
x0 = "Hello World"	#str
x1 = 20	   #int
x2 = 20.5	#float
x3 = 1j	#complex
x4 = ["apple", "banana", "cherry"]	#list
x5 = ("apple", "banana", "cherry")	#tuple
x6 = range(6)	#range
x7 = {"name" : "John", "age" : 36}	#dict
x8 = {"apple", "banana", "cherry"}	#set
x9 = frozenset({"apple", "banana", "cherry"})	#frozenset
x10 = True	#bool
x11 = b"Hello"	#bytes
x12 = bytearray(5)	#bytearray
x13 = memoryview(bytes(5))	#memoryview
x14 = None	#NoneType


#Setting the Specific Data Type
y1 = str("Hello World")	#str
y1 = int(20)	#int
y2 = float(20.5)	#float
y3 = complex(1j)	#complex
y4 = list(("apple", "banana", "cherry"))	#list
y5 = tuple(("apple", "banana", "cherry"))	#tuple
y6 = range(6)	#range
y7 = dict(name="John", age=36)	#dict
y8 = set(("apple", "banana", "cherry"))	#set
y9 = frozenset(("apple", "banana", "cherry"))	#frozenset
y10 = bool(5)	#bool
y11 = bytes(5)	#bytes
y12 = bytearray(5)	#bytearray
y13 = memoryview(bytes(5))	#memoryview


#  Get the characters from position 2 to position 5 *********(not included):
texter = "Hello, World!"
print(texter[2:5])

# string Methods  -- https://www.w3schools.com/python/python_strings_methods.asp
country = 'Brazil'
print(len(country))
print(country[2:4])  # slice  az
print(country[:3])  # slice from the start
print(country[3:])  # slice from the start
print(len(country[2:4]))
print(country[-5:-2]) # Use negative indexes to start the slice from the end of the string:
print(country.upper())
print(country.lower())
print(" Hello world ".strip()) # The strip() method removes any whitespace from the beginning or the end:
print(" Hello world ".replace("H", "J"))  # OP = Jello world
print(" Hello world ".split(" ")) # op ['', 'Hello', 'world', '']

# F-Strings
version = 3.6
currency = 70
print(f"hello I am new type from {version}")
print(f"The price is {currency:.2f} dollars")
print(f"The price is {20 * 59} dollars")
print("We are the so-called \"Vikings\" from the north.")

#The following will return False:

print((False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#Check if an object is an integer or not:
checkInt = 200
print(str(isinstance(checkInt, int)) + "  isinstance helps to  check the variable type")

#operators https://www.w3schools.com/python/python_operators.asp

# Lists
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant"
print(thislist)

thislist.append("orange")
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)

# Remove in List
thislist.remove("orange")
print(thislist)

thislist.pop(1)
print(thislist)

del thislist[0]
print(thislist)
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
[print(x) for x in thislist]


i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# List Comprehension # https://www.w3schools.com/python/python_lists_comprehension.asp
#newlist = [expression for item in iterable if condition == True]

newlist = [x for x in fruits if x != "apple"]

thislist.sort()
thislist.sort(reverse = True)
thislist.sort(key = str.lower)
thislist.reverse()


# copy List
mylist = thislist.copy()
mylist = list(thislist)
mylist = thislist[:]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])

print(len(thisdict))

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "test")

def my_function2(child3, child2, child1):
  print("The youngest child is " + child3)

my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))



class Person:
  def __init__(self, name, age):  # constructor
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

# he local variable can be accessed from a function within the function:

def myfuncT():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfuncT()