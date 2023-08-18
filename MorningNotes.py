
# COMMENT HEAVILY
    # the # is the signifier for a comment
    print("Hello World") # this will print hello world
    # Create a comment line # at the beginning: CTRL + 1
    # This is a comment
    # Comments are a great way to create pseudo code
    # Comments do not execute in python
    
#%% Section Break - Let's you organize your code

# Code

#%%% Sub-Section

# Subsection

#%% Keyboard shortcuts in Spyder
    # 1) Ribbon
    # 2) Shortcuts
        # F9 -> runs a single line of code
        # CTRL + Enter -> run a 'cell' of code
        # F5 -> runs all of your code
        # CTRL + 1 to comment
    # See all: Tools -> Preferences -> Keyboard Shortcuts
    
#%% Data types in python

# Main types of information you will deal with:
    # 1) Numerical
    # 2) Strings -> text
    
# Types of numberical values
    # 1) Numbers
        # 1) Integers
        # 2) Float
    # 2) Dates
    
    # to create a variable varName = ...
x = 5
type(x)
y = 2.2
type(y)

# We can change a number's type by 'casting'
z = 5
z = float(z)

x + y

# When casting to int you discard all precision
w = 5.7
w = int(w)

# Page 15 shows all math operators
# Incrementers
x = x + 1
x += 1

#%% Strings in python

# "Sort of" LIVE NOTES FILE:  https://github.com/jawook/py1Aug18

x = "Hi"
y = 'Hello'

'hello' == 'Hello'

# Print to console print(string)
print('Hello World')

# Variable creation best practices
first year = 12
    # cannot have spaces
    
camelCase = 'variable'
snake_case = 'varaible'

# Combining strings
firstName = 'Jamie'
lastName = 'Wilkie'

print(firstName + ' ' + lastName)
# In python, you concatenate with the +

playerIntro = 'Wayne Gretzkys jersey number was '
jerseyNum = 99

print(playerIntro + jerseyNum)
# This is an error because you can't concat numbers with strings

print(playerIntro + str(jerseyNum))

#%%% String Methods

# general syntax: string.method(arguments)

myName = 'Jamie Wilkie'
myName.upper()

# To get a list of available methods: dir(type)
dir(myName)

# To get documentation:
help(print)
    # google python .upper method
    
company = '   Bell Canada'
company.strip() #strip removes white space at the begin or end of a string
company = company.strip()

company = '----   Telus ----'
company = company.strip('-') # specify other characters
company = company.strip()

company = company.strip('-').strip() # can chain together methods to do more

marketCap = '$123,456,789'
# Other helpful string methods: replace(), split(), join()

#%% Lists in python

# Lists store data in a one dimensioal array
# Data items in that list are identified by an index number
    # Python indices start at zero

list1 = ['a', 'b', 'c']
# We create lists with square brackets and separate items with commas

# Lists can contain mixed info.
list2 = ['A', 3.3, 12]

list3 = [list1, list2]

# Accessing lists
    # Use index numbers
print(list1[1])

# Reassigning in a list
list1[0] = 3
# Notice that list 1 within list 3 ALSO updated

list3[0][1] = 12

# Accessing slices of lists
list1 = ['a', 'b', 'c', 'e', 'd']
list1[0:3]
# In python, when you refer to a slice, it is INCLUSIVE of the bottom item, 
# exclusive of the top item

list1[1:3]

# Slicing works for strings too
hw = 'Hello World'    
hw[0:5]
hw[:5] #omit the beginning of slice, it starts at the beginning
hw[-5:]

list1[-2]

#%%% List Methods:

# .append()
list1.append('f')
list1.append(['g', 'h'])
    # append will add whatever you specify as ONE SINGLE ITEM to the end of list
    
# .extend
addOn = ['g', 'h']
list1.extend(addOn)

# .insert
list1 = ['a', 'b', 'c', 'e', 'd']
list1.insert(1, 'New Item')
    # Adds new item and shifts to the right
    
# .pop
    # Remove (by default) the last item in the list AND return it
list1 = ['a', 'b', 'c', 'e', 'd']
list1.pop()
removed = list1.pop()
    # pop a specific index by entering as an argument
list1.pop(1)

# Other popular methods for lists: .sort, .remove

#%% Dictionaries

# Another very common data storage structure.  Rather than using and indexed
# array, we use key:value pairs

# Creating dictionaries with {}
    # Syntax: dict = {key1: value, key2: value2...., keyn: valuen}
    # We access dictionaries with their KEYS
    
dict1 = {'AAPL': 140, 'NFLX': 600, 'TSLA': 800}

# Accessing an item from a dictionary
dict1['NFLX']

# Adding a new item
dict1['MSFT'] = 300

# Changing an item
dict1['MSFT'] = 400

# Removing an item
dict1.pop('MSFT')

# Duplicates result in replacement with the LAST ITEM provided
dict1 = {'AAPL': 140, 'NFLX': 600, 'TSLA': 800, 'AAPL': 290}

# Dictionaries can contains LISTS, INTs, FLOATS, Other Dictionaries

aaplDict = {'Price': 140, 'EPS': 1.05}
nflxDict = {'Price': 600, 'EPS': 4.55}

dict1 = {'AAPL': aaplDict, 'NFLX': nflxDict}
    # json files are 'basically' dictionaries of dictionaries
    
dict1['AAPL']['Price']
dict1['NFLX']['EPS']





