# RECEIVES JSON DUMPS OF LIST1 AND PROCESS TO GENERATE FINAL LIST1
# LOGS TO LOG1/PROC...TEXT
# DATA TO FINAL1
# APPROX : 6 - 30 mins


import json
from datetime import datetime
import pandas as pd
import logging
from libraries import *
import os

if not os.path.isdir('Log1'):
    os.mkdir('Log1')

if not os.path.isdir('final1'):
    os.mkdir('final1')
#setting up basic logging
logging.basicConfig(filename='Log1/json_processor.txt',
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



D_mapping = {}

for i in range(len(year_dates)):
    D_mapping[year_dates[i]] = 'D{}'.format(i+1)


def D_mapper(row):
    if row in list(D_mapping.keys()):
        D = D_mapping[row]
    else:
        D = None
    return D
    
#cleaning json and merging


def cleaning(jsonfile):
    
    with open(jsonfile, 'r') as outfile:
        jd = json.load(outfile)    
        df_list1_0 = []
        
        for i in range(18):
            if len(jd[str(i)]) !=0:
                #upp checking if list not empty                
                dfi = pd.DataFrame(jd[str(i)])
                df_list1_0.append(dfi)
            else:
                logger.info("Empty List {}".format(jsonfile))

        return df_list1_0
        
        

def merging_individual_dfs(start, N):    
    '''creating a single datafile  N=number of dumpfiles'''
    i = start
    
    while i <= N:
        #df_l1_list = []
        jsonfile = 'data1/json_data{}'.format(i)
        logger.info('processing : {}'.format(jsonfile))
        try:
            df_list = cleaning(jsonfile)
            if len(df_list) > 0:
                df_l1 = pd.concat(df_list, ignore_index= True)
                df_l1['Day2'] = df_l1.Date.apply(D_mapper)
                df_l1.drop('Day', axis=1, inplace =True)
                df_l1.rename(columns={'Day2':'Day'}, inplace = True)
                #df_l1_list.append(df_l1)
                df_l1.to_csv('final1/final1_temp.csv', index = False, mode = 'a', header=False)
            else:
                logger.info("No dataframe created {}".format(jsonfile))
                
                
        except:
            logger.info("Serious Error {}".format(i))
        i +=1
        
        
    
        

logger.info('START-------------------------- : {}'.format(datetime.datetime.now()))
    
merging_individual_dfs(1001,1484)  # start of json to the end confirm from logfile

final_csv = pd.read_csv('final1/final1_temp.csv')
final_csv.columns = ['Close', 'Date', 'High', 'Low', 'Open', 'Timestamp', 'Volume',
       'stock_name', 'stock_symbol', 'Day']


final_csv.to_csv('final1/final_list1.csv')
logger.info('STOP-------------------------- : {}'.format(datetime.datetime.now()))


