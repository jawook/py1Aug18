# -*- coding: utf-8 -*-
"""
Mini Pandas Assignment Solution
"""

#%% Questions

#1) Load Apple data set (StockData --> aapl.csv) 
    #and Financing Deals data set (ExData --> Data Manip --> Clean tab)

#2) Find all the days of Apple where closing share price was between 70 and 75
    
#3) Financing Deals data (Data Manip file) --> find all deals done by GS and JPM

#4) Find all the deals done in May of 2006
#5) Find all the deals done by Merrill Lynch in Real Estate
#6) Calculate the returns of Apple's closing share price
    #what is the average return and standard deviation?
    
    
#%% Solutions
import pandas as pd
#1
aapl = pd.read_csv("StockData/aapl.csv")
finData = pd.read_excel("ExData/Data Manipulation Worksheet.xlsx",
                        sheet_name="Financing Table Clean")


#2
aaplFilter = aapl[ (aapl['Close']>=70) & (aapl['Close']<=75)]
    #  .between(x, y, inclusive=True)
aaplFilter2 = aapl[aapl['Close'].between(70,75,inclusive=True)]

#3
filter3 = finData[ (finData['LEAD UNDERWRITER']=="Goldman Sachs") | (finData['LEAD UNDERWRITER']=="J.P. Morgan")]
filter3.info()

filterList = ['Goldman Sachs','Lehman Brothers','J.P. Morgan']
    # .isin(list)
    
filter3v2 = finData[finData['LEAD UNDERWRITER'].isin(filterList)]
    #contains filter

#4 - May 2006 deals
filter4 = finData[(finData['DATE']>='2006-05-01') & (finData['DATE']<'2006-06-01')]

#Extracting days, months, years from a date ---> table['colname'].dt.year, .month, .day
finData['Day'] = finData['DATE'].dt.day
finData['Month'] = finData['DATE'].dt.month
finData['Year'] = finData['DATE'].dt.year

filter4 = finData[(finData['DATE'].dt.month == 5) & (finData['Year'] == 2006)]


finData2 = finData.set_index(["DATE"])
finData2.loc['2006-05']


#5
filter5 = finData[ (finData['LEAD UNDERWRITER']=="Merrill Lynch") & 
                  (finData['INDUSTRY']=="Real Estate")]

#6
aapl['Returns'] = aapl['Close'].pct_change()
avgReturn = aapl['Returns'].mean()
stdRetrun = aapl['Returns'].std()
maxRetrun = aapl['Returns'].max()
aapl['Returns + 1']=aapl['Returns']+1
geomMean = aapl['Returns + 1'].product() - 1

