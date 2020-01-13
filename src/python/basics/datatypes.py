print("#################################")
print("####### DataType: Integer #######")
print("#################################")
#DataType: Integers
#int
x = 3; 
print("DataType: int")
print(type(3))
print(isinstance(x, int))

#float
x = 3.0
print("DataType: float")
print(type(3))
print(isinstance(x, float))

#complex
x = 3 + 1j 
print("DataType: complex")
print(type(3))
print(isinstance(x, complex))


print("################################")
print("####### DataType: String #######")
print("################################")
#DataType: String
singleQuotes = 'Single quotes string'

doubleQuotes = "Double quotes string"

tripleQuotes = '''Triple quotes string'''

print(singleQuotes)
print(doubleQuotes)
print(tripleQuotes)

#String is immutable
secondLetter = singleQuotes[1]
print(secondLetter)

#Can't modify letter at index 1
#singleQuotes[1] = 'g'
#secondLetter = singleQuotes[1]
#print(secondLetter)



print("#################################")
print("####### DataType: Boolean #######")
print("################################")

#DataType: Boolean
print(type(True))

print(type(False))

if (True == False):
  print("Checking True")
else:
  print("Checking False")

print("##############################")
print("####### DataType: List #######")
print("##############################")

#Creating list
fruits = []
print("Empty List")
print(fruits)

fruits=['apple', 'orange', 'kiwi']
print("Creating list")
print(fruits)

#nested list: list in another list
fruits = [['orange', 'kiwi', 'naval orange'], 'banana', 'apple']
print("Creating nested list")
print(fruits)

#updating a list
fruits[0] = ['squash', 'zucchini', 'spinach']
print("updating list ")
print(fruits)


print("###############################")
print("####### DataType: Tuple #######")
print("###############################")



print("#############################")
print("####### DataType: Set #######")
print("#############################")
fruits={'apple', 'orange', 'kiwi'}
print(fruits)

#can have duplicates when creating Set.
#It removes the duplicates lateron
fruits={'apple', 'orange', 'kiwi', 'orange'}
print(fruits)

#mixed datatypes
itemsInBag = {1, 'coins', False}
print(itemsInBag)

#Using set() function
#Using one item
fruits=set('apple')
print(fruits)

#Using list
fruits=set(['apple', 'orange', 'kiwi'])
print(fruits)

#Using tuple
fruits=set(('apple', 'orange', 'kiwi', 'orange'))
print(fruits)

#add item in set
fruits.add('banana')
print("Set after adding banana")
print(fruits)

#Remove item(s) from set

#using item at a specific index.
#KeyError could occur when item doesn't exist
fruits.remove('apple')
print("Set after removing apple")
print(fruits)

#using item at a specific index without KeyError
fruits.discard('orange')
print("Set after removing orange")
print(fruits)

#remove last item of the set
lastItem = fruits.pop()
print("Removed lastItem: " + lastItem)

#Remove all items from set
fruits.clear()
print("Set after removing ALL items")
print(fruits)

print("####################################")
print("####### DataType: Dictionary #######")
print("####################################")

#Creating empty dictionary
myDict = {}
print("Empty dictionary")
print(myDict)

#Dictionary with integer sorted
myDict = {1: 'suman', 2: 'sally', 3: 'ride'}
print("Dictionary with integer keys")
print(myDict)

#Dictionary with mixed data type keys
myDict = {1: 'suman', 'suman_age': 25, 2: 'sally', 'sally_age': 30, 3: 'ride', 'ride_age': 28}
print("Dictionary with mixed data type keys")
print(myDict)

#Creating dictionary using dict() function
myDict = dict({1: 'suman', 2: 'sally', 3: 'ride'})
print("Creating dictionary using dict() function")
print(myDict)

#Creating dictionary using pairs
myDict = dict([(1,'suman'), (2, 'sally'), (3, 'ride')])
print("Creating dictionary using pairs")
print(myDict)

#Adding items to dictionary
myDict[4] = 'Rashi'
print("Added item to dictionary")
print(myDict)

#Updating item in dictionary
myDict[3] = 'Manny'
print("Updated item in dictionary")
print(myDict)

#Accessing items in dictionary using key
name = myDict[1]
print("Accessing items in dictionary using key")
print(name)

#Removing items from dictionary

#Removing item for given key
del myDict[4]
print("Dictionary after removing item at given key")
print(myDict)

#Removing specific key and returning corresponding item
item = myDict.pop(3)
print("Remove key and return its value in dictionary")
print(item)
print(myDict)

#Removing item
item = myDict.popitem()
print("Remove last item from dictinary")
print(item)
print(myDict)

#Remove all items from dictionary
myDict.clear()
print("Dictionary after removing ALL items")
print(myDict)