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


#%% Takeup A1 -> Q2

deal_value = '$123,456,789'

deal_value * 2

deal_value = deal_value.strip('$')
deal_value = deal_value.split(',')
deal_value.replace(',', '')
deal_value = ''.join(deal_value)
deal_value = int(deal_value)
deal_value * 2

#%% Takeup A1 -> Question 4

grades = {'Bob':71, 'Alice':65, 'Jim':70, 
          'Jen':90, 'Tim':86, 'Trish':85, 
          'Tony':75}

# Initialize the letter_grade dictionary
letter_grade = {}

# Loop through the pct grade ditionary and figure out the correct letter grade
# Looping through dictionaries
for key in grades.keys():
    print(key)

for value in grades.values():
    print(value)

for item in grades.items():
    print(item)

for key in grades.keys():
    gr = grades[key]
    if gr >= 90:
        letter_grade[key] = 'A+'
    elif gr >= 85:
        letter_grade[key] = 'A'
    elif gr >= 80:
        letter_grade[key] = 'A-'
    elif gr >= 75:
        letter_grade[key] = 'B+'
    elif gr >= 70:
        letter_grade[key] = 'B'
    else:
        letter_grade[key] = 'B-'
        
# Assign that letter grade to the appropriate person in the letter grade dict

#%% numpy Package

# Numerical Python
# Numpy is extremely popular for doing a lot of math.  In particular:
    # 1) random number generation
    # 2) statistical calculation
    # 3) matrix math
    # 4) other packages rely on numpy
    
# Numpy has a great set of docs

#%% Pandas

# Pandas is spreadsheets for python
# But it can handle millions of rows
    # Doesn't bog down....  too bad.
    
# Importing packages
import pandas as pd

# Importing data from csv
    # Create a dataframe variable
sp500 = pd.read_csv('StockData/SP500.csv')
# Relative reference, relative to project folder

sp500 = pd.read_csv('C:/Users/wilkijam/OneDrive - AMT/Training - Marquee FS/Wells Fargo/2023/py1Aug18/Python Project/StockData/SP500.csv')
# Absolute reference

sp500 = pd.read_csv('C:\Users\wilkijam\OneDrive - AMT\Training - Marquee FS\Wells Fargo\2023\py1Aug18\Python Project\StockData\SP500.csv')
# The NORMAL file path in windows will result in an error, flip you slashes

#%%% Descriptive information about a dataset

len(sp500)

sp500.info()

sp500.describe()

sp500.tail() # the last 5 records

sp500.head() # first 5

sp500.head(3)

#%%% Reading an Excel

finDeals = pd.read_excel('Python Project/ExData/Data Manipulation Worksheet.xlsx')
# If you don't specify sheet name, it goes with the first sheet

finDeals = pd.read_excel('Python Project/ExData/Data Manipulation Worksheet.xlsx',
                         sheet_name='Financing Table Clean')

#%%% read_html

ipos = pd.read_html('https://www.iposcoop.com/last-100-ipos/')

#%%% getting info from a dataframe

#%%%% columns

# Syntax 1: dfName['colName']
# Syntax 2: dfName.colName

sp500['Volume']
sum(sp500['Volume'])
sum(sp500.Volume)

sum(sp500['Adj Close'])
sum(sp500.Adj Close)

sp500[['Date', 'Adj Close']]

#%%% Getting datetimes (rather than text in pandas)

sp500['Date'] = pd.to_datetime(sp500['Date'])
#After you already imported use pd.to_datetime to convert

sp500 = pd.read_csv('Python Project/StockData/SP500.csv', parse_dates=['Date'])
# Converts dates WHILE reading the file

#%%% Setting your index column

sp500 = sp500.set_index(['Date'])
# After import was already done

sp500 = pd.read_csv('Python Project/StockData/SP500.csv', parse_dates=['Date'],
                    index_col=['Date'])
# Specify index while importing

#%%% Two approaches to access rows

    # 1) Index numbers .iloc -> integer loc
    # 2) Fancy index name -> .loc
    
# ILOC uses integer numbers to access data

sp500.iloc[2]
sp500.iloc[2:4]

# LOC method uses index 'name' (date) to access

sp500.loc['2013-10-01']
sp500.loc['20131001']
sp500.loc['2013-10-01': '2013-10-15']

sp500.loc['2013-10']
sp500.loc['2013']

sp500.loc['2013-10']['Close']
sp500.loc['2013-10'][['Open', 'Close']]

sp500.loc['2013-10-01']['Close']
