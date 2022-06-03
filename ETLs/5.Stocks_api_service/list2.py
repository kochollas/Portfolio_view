# Handling list2
# Ingest List1 in chunks process based on b/s logic
# writes the output incrementally to a csv 
# APPROX 1hr for 15million rows



import pandas as pd
import os
import logging
import datetime

if not os.path.isdir('Log2'):
    os.mkdir('Log2')

if not os.path.isdir('final2'):
    os.mkdir('final2')
#setting up basic logging
logging.basicConfig(filename='Log2/log2.txt',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def incremental_read_from_csv(start,size, datafile):
    '''This function reads chunks of data from a csv file'''
    tab_data = pd.read_csv(datafile,header = None,skiprows = start+1,nrows =size)
    return tab_data

def high_over_close(h,c,d,o):
    if d >= 1.0:
        res = h/c
    else:
        res = h/o
    return res

def twenty_five_percentage(row):
    if row >= 1.25:
        result = True
    else:
        result = False
    
    return result

logger.info('START:-------------------------- : {}'.format(datetime.datetime.now()))

N = 10000
i = 0
size = 10000
while i <= N:
    logger.info('PROCESSING AT {}'.format(i))
    list1_data = incremental_read_from_csv(i,size,'final1/final_list1.csv')

    list1_data.columns = ['stock_symbol','stock_name','Close','High', 'Low', 'Open','Volume','Date', 'Timestamp','Day']


    df2 = list1_data.groupby(['stock_symbol','Date'])

    list2 = []

    for name, group in df2:
        list2_dict = {}
        #logger.info(name)
        #logger.info(group.values)
        list2_dict['stock_symbol'] = name[0]
        list2_dict['Date'] = name[1]
        list2.append(list2_dict) 
        o = group['Open'].values
        list2_dict['Open'] = o[0]
        c = group['Close'].values
        list2_dict['Close'] = c[-1]
        h = group['High'].values
        list2_dict['High'] = max(h)
        l = group['Low'].values
        list2_dict['Low'] = min(l)
        d = group['Day'].values
        list2_dict['Day'] = min(d)
        sn = group['stock_name'].values
        list2_dict['stock_name'] = sn[0]
        v = group['Volume'].values
        list2_dict['Volume'] = max(v)
        
        
    df_2 = pd.DataFrame(list2)
    df_2.head(20)


    df3 = df_2.groupby(['stock_symbol'])

    df3_list = []

    for name, group in df3:    
        #logger.info(name)
        group['Close_lag']=group['Close'].shift(1)
        group['D_lag']=group['Date'].shift(1)
        group['Difference'] = (pd.to_datetime(group['Date']) - pd.to_datetime(group['D_lag'])).dt.days
        group['h_over_c'] = group.apply(lambda x: high_over_close(x.High, x.Close_lag,x.Difference,x.Open), axis=1)
        df3_list.append(group)
    
     
    
    list_02 = pd.concat(df3_list, ignore_index= True)
    list_02 = list_02.drop(['Close_lag','D_lag','Difference'], axis=1)

    list_02['h_over_c_pass'] = list_02.h_over_c.apply(twenty_five_percentage)

    list_02_save = list_02.loc[list_02['h_over_c_pass']==True]

    if i == 0:
        heading = True
    else:
        heading = False
        
    list_02_save.to_csv('final2/final_list2.csv', index = False, mode = 'a', header=heading)

    logger.info('Data Row Count on chunk {}:is {}'.format(i,len(list_02_save)))    

    i+=size

logger.info('STOP:-------------------------- : {}'.format(datetime.datetime.now()))


#log the final tabulated yearly results

tab_data = pd.read_csv('final2/final_list2.csv')

tab_data['year'] = tab_data.Date.apply(lambda x:x[0:4])

df2 = tab_data.groupby(['year']).count()

logger.info(df2['stock_symbol'])