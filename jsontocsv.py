# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:29:07 2019

@author: prasa
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:24:24 2019

@author: prasa
"""

import csv
import json
import pandas

from datetime import datetime

with open(r'F:\Talend\stock info\FB_stock.json') as jsonfile:
    json_data = json.load(jsonfile)

    lst_high = []
    lst_date = []
    lst_low  = []
    lst_open  = []
    lst_close  = []
    lst_volume  = []
    lst_adj_close  = []
    
    
    
    for key in json_data:
        
        ts = int(key)/1000
        lst_date.append(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d'))
        lst_high.append(json_data[key]['High'])
        lst_low.append(json_data[key]['Low'])
        lst_open.append(json_data[key]['Open'])
        lst_close.append(json_data[key]['Close'])
        lst_volume.append(json_data[key]['Volume'])
        lst_adj_close.append(json_data[key]['Adj Close'])


        
    dfObj = pandas.DataFrame(columns = ['Date' , 'High', 'Low' , 'Open','Close', 'Volume', 'Adj Close'])

 
    for i in range(0,len(lst_close)):  
        dfObj = dfObj.append({'Date' : lst_date[i] , 'High' : lst_high[i], 'Low' : lst_low[i], 'Open' : lst_open[i], 'Close' : lst_close[i],'Volume' : lst_volume[i],'Adj Close' : lst_adj_close[i]} ,ignore_index=True)



    with open('FB_stock.csv' , 'w') as out:
        dfObj.to_csv("FB_stock.csv", index=False)
        