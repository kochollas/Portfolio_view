#LIST 3 JSON DUMP PROCESSOR


import json
from datetime import datetime
import pandas as pd
import logging
from libraries import *
import os

if not os.path.isdir('Log3'):
    os.mkdir('Log3')

if not os.path.isdir('final3'):
    os.mkdir('final3')
#setting up basic logging
logging.basicConfig(filename='Log3/json_processor.txt',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)



#cleaning json and merging


def cleaning(jsonfile, i):
    
    with open(jsonfile, 'r') as outfile:
        jd = json.load(outfile)  
        
       
        if len(jd[str(i)]) !=0:
            #upp checking if list not empty                
            dfi = pd.DataFrame(jd[str(i)])
        else:
            logger.info("Empty List {}".format(jsonfile))

        return dfi
        
        

def merging_individual_dfs(start, N):    
    '''creating a single datafile  N=number of dumpfiles'''
    i = start
    
    while i <= N:
        
        jsonfile = 'data3/new_data{}'.format(i)
        logger.info('processing : {}'.format(jsonfile))
        try:
            df = cleaning(jsonfile, i)
            if len(df) > 0:  

                if i == 0:                    
                    heading = True            
                else:
                     heading = False
                df.to_csv('final3/final3_temp.csv', index = False, mode = 'a', header=heading)
            else:
                logger.info("No dataframe created {}".format(jsonfile))
                
                
        except:
            logger.info("Serious Error {}".format(i))
        i +=1
        
       
    
        

logger.info('START-------------------------- : {}'.format(datetime.datetime.now()))
    
merging_individual_dfs(0,5198)  # start of json to the end confirm from logfile
#merging_individual_dfs(0,10)  # start of json to the end confirm from logfile

final_csv = pd.read_csv('final3/final3_temp.csv')




logger.info('STOP-------------------------- : {}'.format(datetime.datetime.now()))


x = final_csv
y = x.groupby(['stock_symbol'])


df3list = []
for name, group in y:    
    logger.info(name)
    df3 = group.sort_values(by = 'Date', ascending = True)
    df3['Day'] = range(1,len(df3)+1)
    logger.info(len(df3))
    #logger.info(df3)
    df3list.append(df3)
    

    
list3 = pd.concat(df3list,ignore_index= True)
logger.info(list3.head())
list3.to_csv('final3/final_list3.csv')
