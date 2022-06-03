# GENERATING LIST3 
# Reads from List2 (aggregated)
# Calls the api to generate minute data
# Approx 5000 in 8mins

from libraries import *
import os
import datetime
import json
import logging

if not os.path.isdir('Log3'):
    os.mkdir('Log3')

if not os.path.isdir('data3'):
    os.mkdir('data3')
#setting up basic logging
logging.basicConfig(filename='Log3/log3.txt',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def process_run(symbol, date1, index):
    
    data_in_list = [] 
    result = {}
    url ="https://api.polygon.io/v2/aggs/ticker/{}/range/1/minute/{}/{}?adjusted=true&sort=asc&limit=10".format(symbol,date1,date1)
    stocks_data = api_call(url)
    if stocks_data.status_code == 200:
        stock_json = stocks_data.json()                
        #logger.info('{} : {}'.format(i,stock_json['resultsCount']))
        if stock_json['resultsCount'] != 0:            
            data_raw = stock_json['results']

            for j in range(len(data_raw)):
                stock_inner = {}                
                stock_inner['stock_symbol']=stock_1_minute['stock_symbol']
                stock_inner['stock_name']=stock_1_minute['stock_name']
                stock_inner['Open']=data_raw[j]['o']
                stock_inner['High']=data_raw[j]['h']
                stock_inner['Low']=data_raw[j]['l']
                stock_inner['Close']=data_raw[j]['c']
                stock_inner['Volume']=data_raw[j]['v']
                stock_inner['Date']=formated_time((data_raw[j]['t']/1000))[0:10]
                stock_inner['Timestamp']=formated_time((data_raw[j]['t']/1000))[11:]
                #logger.info(stock_inner) 
                data_in_list.append(stock_inner)
    result[index] = data_in_list
    return result



def incremental_read_from_csv(start,size, datafile):
    '''This function reads chunks of data from a csv file'''
    tab_data = pd.read_csv(datafile,header = None,skiprows = start+1,nrows =size)
    return tab_data

counter = 0
N = 26212
while counter <= N:        
    
    init = incremental_read_from_csv(counter,1,'final2/final_list2_5200.csv')
    logger.info(init)

    stock_1_minute = {'stock_symbol':init.iloc[0,0], 'stock_name':init.iloc[0,7],'date':init.iloc[0,1] }
    logger.info('*'*10)
    logger.info(stock_1_minute['stock_symbol'])
    logger.info(stock_1_minute['stock_name'])
    logger.info(stock_1_minute['date'])
    logger.info('*'*10)
    logger.info('********** {}:{} ******************'.format(counter, stock_1_minute['stock_symbol']))
    logger.info('START : {}'.format(datetime.datetime.now()))
    new_stocks = process_run(stock_1_minute['stock_symbol'], stock_1_minute['date'], counter)
    stocks_written = 'data3/new_data{}'.format(counter)
    # WRITE JSONS FOR DOWN-STREAM PROCESSINGS
    with open(stocks_written, 'w') as outfile:
        json.dump(new_stocks, outfile)

    logger.info('STOP : {}'.format(datetime.datetime.now()))
    counter +=1
    


