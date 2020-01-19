# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:39:52 2019

@author: prasa
"""

import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import quandl
from iexfinance.stocks import get_historical_data

download_source1 = (r'F:\Talend\stock info\apple_stock.xlsx')
download_source2 = (r'F:\Talend\stock info\amazon_stock.csv')
download_source3 = (r'F:\Talend\stock info\FB_stock.json')
download_source4 = (r'F:\Talend\stock info\Netflix_stock.xlsx')
download_source5 = (r'F:\Talend\stock info\Tesla_stock.xlsx')

start = dt.datetime(2018,12,1)
end = dt.datetime.today()

df1 = pdr.get_data_yahoo('AAPL',start,end)
df2 = pdr.get_data_yahoo('AMZN',start,end)
df3 = pdr.get_data_yahoo('FB',start,end)


quandl.ApiConfig.api_key = 'yspKg9e44e2WxvzQ33Qh'
data = quandl.get_table('WIKI/PRICES', ticker = ['NFLX'], 
                        qopts = { 'columns': ['ticker', 'date','High','Low', 'adj_close'] }, 
                        date = { 'gte': '2015-12-31', 'lte': '2016-12-31' }, 
                        paginate=True)

f = get_historical_data('TSLA', start, end, output_format='pandas')




print(df1.head())
print(df2.head())
print(df3.head())
print(data.head())
print(f.head())
#print(df4.head())
#print(df5.head())

with open('apple_stock.xlsx', 'w') as myOutputFile1:
    df1.to_excel(download_source1)
    
with open('amazon_stock.csv', 'w') as myOutputFile2:
    df2.to_csv(download_source2)
    
with open('FB_stock.json', 'w') as myOutputFile3:
    df3.to_json(download_source3)
    
with open('Netflix_stock.xlsx', 'w') as myOutputFile4:
    data.to_excel(download_source4)
    
with open('Tesla_stock.xlsx', 'w') as myOutputFile5:
    f.to_excel(download_source5)    
