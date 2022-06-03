# RUNS AFTER PROCESSED JSON INCASE OF SEVERAL PROCESS TO MERGE DEFAULT = 5 FOR NOW.
# WILL RESIDE ON THE MAIN FOLDER
# Apprx 1min

import pandas as pd
import logging
import os
'''
if not os.path.isdir('Log1'):
    os.mkdir('Log1')

if not os.path.isdir('final1'):
    os.mkdir('final1')
#setting up basic logging
logging.basicConfig(filename='Log1/join.txt',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)




k1 = pd.read_csv('final1/final1_temp.csv')
logger.info('Done 1 : {}'.format(len(k1)))
k1.columns = ['stock_symbol','stock_name','Close','High', 'Low', 'Open','Volume','Date', 'Timestamp','Day']
logger.info(k1.head())
k1.to_csv('final1/final_list1.csv',index = False)


k2 = pd.read_csv('~/karim2/final1/final1_temp.csv')
logger.info('Done 2 : {}'.format(len(k2)))
k2.columns = ['stock_symbol','stock_name','Close','High', 'Low', 'Open','Volume','Date', 'Timestamp','Day']
logger.info(k2.head())
k2.to_csv('final1/final_list1.csv', index = False, mode = 'a', header=False)


k3 = pd.read_csv('~/karim3/final1/final1_temp.csv')
logger.info('Done 3 : {}'.format(len(k3)))
k3.columns = ['stock_symbol','stock_name','Close','High', 'Low', 'Open','Volume','Date', 'Timestamp','Day']
logger.info(k3.head())
k3.to_csv('final1/final_list1.csv', index = False, mode = 'a', header=False)



k4 = pd.read_csv('~/karim4/final1/final1_temp.csv')
logger.info('Done 4 : {}'.format(len(k4)))
k4.columns = ['stock_symbol','stock_name','Close','High', 'Low', 'Open','Volume','Date', 'Timestamp','Day']
logger.info(k4.head())
k4.to_csv('final1/final_list1.csv', index = False, mode = 'a', header=False)


k5 = pd.read_csv('~/karim5/final1/final1_temp.csv')
logger.info('Done 5 : {}'.format(len(k5)))
k5.columns = ['stock_symbol','stock_name','Close','High', 'Low', 'Open','Volume','Date', 'Timestamp','Day']
logger.info(k4.head())
k5.to_csv('final1/final_list1.csv', index = False, mode = 'a', header=False)

'''


# function to merge files easily

def join_small_to_big_df(folder,smallfile,bigfile):
    smaller_df = pd.read_csv('{}/{}'.format(folder,smallfile))

    smaller_df.to_csv('{}/{}'.format(folder,bigfile), index = False, mode = 'a', header=False)
    print('ADDED {} ROWS'.format(len(smaller_df)))

path = '/media/mikes/F/2022/LISTs/list1'   

join_small_to_big_df(path,'added_list1.csv', 'initial_list1.csv')

