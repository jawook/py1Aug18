"""
Marquee Python - Manipulating Data using pandas - Exercise Solutions
"""
import pandas as pd
import numpy as np

#%% Exercise 1

ba = pd.read_csv('StockData/BA.csv')
print(ba.info())
ba['Date'] = pd.to_datetime(ba['Date'], format=r'%Y-%m-%d')
ba.set_index('Date', inplace=True) # Don't specifiy as ba['Date']
print(ba.info())

ba = pd.read_csv('StockData/BA.csv', header=0, index_col=0,
                 parse_dates=True)
ba.info()

print(ba.head(10))
print(ba.tail(3))

ba = pd.read_csv('StockData/BA.csv', header=0, index_col=0,
                 parse_dates=False)
ba.info()
# Notice now that the index is now a DateTime data type
######################################################################################

#%% Exercise 2


sp500 = pd.read_csv('StockData/SP500.csv', header=0, index_col=0, parse_dates=True)
ba = pd.read_csv('StockData/BA.csv', header=0, index_col=0, parse_dates=True)

sp500oc = sp500[['Open','Close']].copy()
ba_oc = ba[['Open','Close']].copy()

sp500oc['Close_1'] = sp500oc['Close'].shift(1)
ba_oc['Close_1'] = ba_oc['Close'].shift(1)

print(sp500oc.head())
print(ba_oc.head())

sp500oc['rtns'] = (sp500oc['Close'] - sp500oc['Close_1'])/sp500oc['Close_1']
sp500oc['log_rtns'] = np.log(sp500oc['Close']) - np.log(sp500oc['Close_1'])

ba_oc['rtns'] = (ba_oc['Close'] - ba_oc['Close_1'])/ba_oc['Close_1']
ba_oc['log_rtns'] = np.log(ba_oc['Close']) - np.log(ba_oc['Close_1'])

print(sp500oc.head())
print(ba_oc.head())

merged_df = sp500oc.merge(
    ba_oc, how='left', left_index=True, right_index=True, suffixes =('_sp','_ba'))
merged_df.head()

print('Mean SP500 Daily Return: {:%}'.format(np.mean(merged_df['rtns_sp'])))
print('Mean SP500 Daily Log-Return: {:%}'.format(np.mean(merged_df['log_rtns_sp'])))
print('Mean BA Daily Return: {:%}'.format(np.mean(merged_df['rtns_ba'])))
print('Mean BA Daily Log-Return: {:%}'.format(np.mean(merged_df['log_rtns_ba'])))

merged_df.describe()
#######################################################################################
#%% Exercise 3
import pandas as pd

sp500 = pd.read_csv('StockData/SP500.csv', header=0, index_col=0, parse_dates=True)
ba = pd.read_csv('StockData/BA.csv', header=0, index_col=0, parse_dates=True)

sp500oc = sp500[['Open','Close']].copy()
ba_oc = ba[['Open','Close']].copy()

sp500oc['Close_1'] = sp500oc['Close'].shift(1)
ba_oc['Close_1'] = ba_oc['Close'].shift(1)

print(sp500oc.head())
print(ba_oc.head())

sp500oc['Pos_Day'] = sp500oc['Close'] > sp500oc['Open']
ba_oc['Pos_Day'] = ba_oc['Close'] > ba_oc['Open']

merged_df = sp500oc.merge(
    ba_oc, how='left', left_index=True, right_index=True, suffixes =('_sp','_ba'))
print(merged_df.head())

merged_df['ba_pos_sp_neg'] = merged_df.apply(
    lambda x: 1 if (x['Pos_Day_ba'] == True) and (x['Pos_Day_sp'] == False) else 0, axis=1)
print(merged_df.head(10))

merged_df.dropna(inplace=True)

print(merged_df['ba_pos_sp_neg'].value_counts())
#######################################################################################

#%% Exercise 4
# Joining with a gap in the index
bbus = pd.read_csv('StockData/BB/BB_NYSE.csv', index_col='Date', parse_dates=True)
print(bbus.head())
bbcad = pd.read_csv('StockData/BB/BB_TO.csv', index_col='Date', parse_dates=True)
print(bbcad.head())

# Subset to only Jan
bbus = bbus['2018-01']
bbcad = bbcad['2018-01']

bb = bbcad.join(bbus, lsuffix='_tse', rsuffix='_nyse')
print(bb.loc['2018-01-12':'2018-01-17'])

#######################################################################################
#%% Exercise 5

sp500 = pd.read_csv('StockData/SP500.csv', header=0, index_col=0, parse_dates=True)
sp500.columns = [i.lower().replace(' ','_') for i in sp500.columns]
print(sp500.head())

sp500['adj_close_1'] = sp500['adj_close'].shift()
sp500['log_rtn_c_to_o'] = np.log(sp500['open']) - np.log(sp500['adj_close_1'])
sp500['log_rtn_o_to_c'] = np.log(sp500['adj_close']) - np.log(sp500['open'])

# When finding daily vol, the numbers can become really small decimals.
# We can multiply the returns by 100 before squaring if a numerical problem occurs
sp500['vol_c_to_o'] = (sp500['log_rtn_c_to_o'] ** 2)
sp500['vol_o_to_c'] = (sp500['log_rtn_o_to_c'] ** 2)

vol_weight = 0.5

sp500['vol'] = sp500['vol_o_to_c'] * vol_weight + sp500['vol_c_to_o'] * (1-vol_weight)

sp500['vol_1'] = sp500['vol'].shift(1)
sp500['vol_ma_5'] = sp500['vol_1'].rolling(window = 5, min_periods=5).mean()
sp500['vol_ma_21'] = sp500['vol_1'].rolling(window = 21, min_periods=21).mean()

print(sp500.head(30))
#######################################################################################

#%% Exercise 6
ba = pd.read_csv('StockData/BA.csv', header=0, index_col=0, parse_dates=True)
ba.columns = [i.lower().replace(' ','_') for i in ba.columns]
print(ba.head())

financials = pd.read_csv('StockData/fundamentals.csv', index_col=0)
financials.columns = [i.lower().replace(' ','_') for i in financials.columns]
financials.info()

# Convert to month end to handle alignment with reporting date
# using the previous quarter end to not have information early
ba['match_date'] = ba.index + pd.offsets.MonthEnd(-3)

financials['period_ending'] = pd.to_datetime(financials['period_ending'])
financials['match_date'] = financials['period_ending'] + pd.offsets.MonthEnd(0)

financials['ROA'] = financials['net_income']/financials['total_assets']

max_date = max(financials[financials['ticker_symbol']=='BA']['match_date'])
min_date = min(financials[financials['ticker_symbol']=='BA']['match_date'])

ba_fin = ba.merge(financials[financials['ticker_symbol']=='BA'][['match_date','ROA']], how='left')
ba_fin.info()
ba_fin['ROA'] = ba_fin['ROA'].fillna(method='ffill')

ba_fin = ba_fin[ba_fin['match_date'] <= (max_date + pd.DateOffset(years=1))]
ba_fin = ba_fin[ba_fin['match_date'] >= (min_date)]

#######################################################################################
#%% Exercise 7

#Open FF3 - Fama French Three Factors and CAT
ba = pd.read_csv('StockData/ba.csv', header=0, index_col=0, parse_dates = True)
ba.columns = [i.lower().replace(' ','_') for i in ba.columns]
print(ba.head())

ff3 = pd.read_csv('StockData/FF3.csv', header=0, index_col=0, parse_dates=True)
# the dates in the FF3 file cannot be automatically parsed
# will be imported as a int64index

# The index is not date time
print(ff3.info())

# Create a temporary date column and copy the index
ff3['date'] = ff3.index

# Parse the date time, default is beginning of the month, offset to the end of the month
ff3['date'] = pd.to_datetime(ff3.index,format='%Y%m') + pd.offsets.MonthEnd(0)
ff3.set_index(['date'], drop=True, inplace=True)
print(ff3.head())

# Same rules as previously defined
ohlc_rule = {'open':'first', 'high':'max', 'low':'min',
            'close':'last', 'volume':'sum', 'adj_close':'last'}

# Resample the daily data into monthly data using resample and agg
ba_mon = ba.resample('M').agg(ohlc_rule)
ba_mon.to_csv('StockData/ba_mon.csv')
print(ba_mon.head())

# Log Returns on adjust close
ba_mon['log_rtns'] = np.log(ba_mon['adj_close']) - np.log(ba_mon['adj_close'].shift(1))

# Merge on the index, no need for suffix because there are no duplicate columns
ba_ff = pd.merge(ba_mon, ff3, how='left', left_index=True, right_index=True)
print(ba_ff.head())
# Notice how the returns are multiplied by 100 for the FF3 data, correct this for ba
ba_ff['log_rtns'] = ba_ff['log_rtns'] * 100
print(ba_ff.head())
print(ba_ff.info())
ba_ff.to_csv('StockData/BA_FF3_mon.csv')
