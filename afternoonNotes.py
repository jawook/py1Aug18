# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 13:50:44 2023

@author: wilkijam
"""

#%% TUPLEs

# A tuple is a list that you cannot change.
# List but use () instead of []
# Immutable

tup1 = (0, 1, 2)
tup1[1] = 'a'
tup1 = (0, 'a', 2)

#%% Logic in Python

# We can check the logic of any statement.

# Check for Equality
a = 2
b = 2
a == b

# Check for inquality
a = 2
b = 2
a != b

# Other logical operators: >, <, >=, <=

# Not logic -> flipping your standard logic
a = 2
b = 2
not(a != b)

# And logic
5>5 and 7>5
6>5 and 7>5

# OR logic
5>5 or 7>5
5>5 or 3>5

# Other and/or logic operators: bitwise logic
    # condition1 & condition2  AND
    # condition1 | condition2  OR
    # If you use this with standard number check, you will get unexpected results
    
#%% IF Statements

# Syntax:
    # if condition:
        # [CODE THAT YOU WANT TO RUN IF ABOVE IS TRUE]
    # [CODE THAT ALWAYS RUNS]
    
a = 3
b = 5
if a > b:
    print('a is greater than b')
print('This will always print')

# Else statements

a = 10
b = 5
if a > b:
    print('a is greater than b')
else:
    print('b is greater than or equal to a')
print('This will always print')

# Elif statements

a = 5
b = 5
if a > b:
    print('a is greater than b')
elif a <= b:
    print('a less than or equal to b')
elif a == b:
    print('a is equal to b')
else:
    print('other')
print('This will always print')

#%% FOR and WHILE

# FOR Loop: runs code a defined number of times
# WHILE loop: keeps running code until some condition is no longer true

# For loops:
    # Most common: i need code to run X times through the loop
    # A for loop iterates over an iterable
    # We can use the range() function to create an iterable list of #s
    
# Range function:
    # Syntax 1: range(x) = a series of numbers from 0 to x-1
    # Syntax 2: range(x, y) = a series of numbers from x to y-1
    # Syntax 3: range(x, y, z) = a series of numbers from x to y-z, count by z
    
for j in range(5): # j=0, j=1... j=4
    print(j)

for jw in range(2, 28, 2):
    print(jw)
    
epsEst = [0.25, 1.23, 4.60, 2.20]

# CHALLENGE: print out the price target for each EPS if you used a 15x multiple

for j in range(len(epsEst)):
    print(epsEst[j] * 15)

for j in epsEst: # j=0.25, j=1.23...
    print(j * 15)

#%% While loop

# Syntax:
    # while condition:
        # [CODE TO EXECUTE AS LONG AS CONDITION IS TRUE]
    # [CODE THAT RUNS AFTER THE LOOP IS DONE]
    
# Most common while loop uses a counter

i = 0

while i < 5:
    print(i)
    # something has to happen in your loop that COULD cause the condition to
    # become false eventually
    i += 1

# If you're stuck in a loop, hit the red stop button.

i = 0

while i < 5:
    if i >= 2:
        break # -> exit the loop if you get to this line
    print(i)
    i += 1


    