# LIST 1 GENERATOR FROM LIST0 
# PROVIDE LIST0
# LOGS TO LOG1/LOG1.TXT
# USES THREADING
# APPROX : 11 TO 22 HRS

from libraries import *
import os
import datetime
import json
import logging

if not os.path.isdir('Log1'):
    os.mkdir('Log1')

if not os.path.isdir('data1'):
    os.mkdir('data1')
#setting up basic logging
logging.basicConfig(filename='Log1/log1.txt',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

start_on = datetime.date(2007, 5, 1)
numdays = 5110
dateList = []
for x in range (0, numdays):
    dateList.append(start_on + datetime.timedelta(days = x))
    

year_dates = [d.strftime("%Y-%m-%d") for d in dateList ]
n = len(year_dates)


id_range = year_dates

subset = id_range

from threading import Thread


def process_range(id_range, result, index):
    
    data_in_list = []    
    for i in range(len(id_range)):    
                url ="https://api.polygon.io/v2/aggs/ticker/{}/range/30/minute/{}/{}?adjusted=true&sort=asc&limit=10".format(stock_30_minute['stock_symbol'],id_range[i],id_range[i])
                stocks_data = api_call(url)
                if stocks_data.status_code == 200:
                    stock_json = stocks_data.json()                
                    #logger.info('{} : {}'.format(i,stock_json['resultsCount']))
                    if stock_json['resultsCount'] != 0:            
                        data_raw = stock_json['results']
                                    

                        for j in range(len(data_raw)):
                            stock_inner = {}
                            stock_inner['Day']='D{}'.format(i+1)
                            stock_inner['stock_symbol']=stock_30_minute['stock_symbol']
                            stock_inner['stock_name']=stock_30_minute['stock_name']
                            stock_inner['Open']=data_raw[j]['o']
                            stock_inner['High']=data_raw[j]['h']
                            stock_inner['Low']=data_raw[j]['l']
                            stock_inner['Close']=data_raw[j]['c']
                            stock_inner['Volume']=data_raw[j]['v']
                            stock_inner['Date']=formated_time((data_raw[j]['t']/1000))[0:10]
                            stock_inner['Timestamp']=formated_time((data_raw[j]['t']/1000))[11:]
                            #print(stock_inner) 
                            data_in_list.append(stock_inner)
    result[index] = data_in_list
    return result



def threaded_process_range(nthreads, id_range):
    """process the id range in a specified number of threads"""
    result = {}
    threads = []
    # create the threads
    for i in range(nthreads):
        ids = id_range[i*nthreads:i*nthreads+nthreads:1]
        t = Thread(target=process_range, args=(ids,result,i))
        threads.append(t)

    # start the threads
    [ t.start() for t in threads ]
    # wait for the threads to finish
    [ t.join() for t in threads ]
    return result




# IMPLEMENT A FUNCTION TO LOOP OVER ALL SYMBOLS 
#df = pd.read_csv('final0/final_list0.csv')  #LIST0

#N = len(df)
counter = 0
while counter <= 600: #range(len(df)):    )      

    init = incremental_read_from_csv(counter,1,'final0/final_list0.csv') # LIST0

    stock_30_minute = {'stock_symbol':init.iloc[0,0], 'stock_name':init.iloc[0,1] }
    print('*'*10)
    print(stock_30_minute['stock_symbol'])
    print('*'*10)
    logger.info('********** {}:{} ******************'.format(counter, stock_30_minute['stock_symbol']))
    #CALLING THE INNER FUNCTION USING THREADS TO PROCESS STOCK SYMBOL  FROM 2007 TO 2022
    
    logger.info('START -----------------------: {}'.format(datetime.datetime.now()))
    try:
        res2 = threaded_process_range(nthreads = 300,id_range = subset)
    except:
        logger.error("{}:{}".format(counter, stock_30_minute))

    stocks_written = 'data1/json_data{}'.format(counter)
    # WRITE JSONS FOR DOWN-STREAM PROCESSINGS
    with open(stocks_written, 'w') as outfile:
        json.dump(res2, outfile)

    logger.info('STOP-------------------------- : {}'.format(datetime.datetime.now()))

    counter +=1
