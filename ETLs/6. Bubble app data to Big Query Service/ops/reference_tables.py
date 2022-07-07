# references tables generation
import numpy as np
from schemas.database_tables import *
from utils.libraries import *

import logging
if not os.path.isdir('Log'):
    os.mkdir('Log')
#setting up basic logging
logging.basicConfig(filename='Log/log.txt',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def references_generator(json_data):
    '''Calls above with json_data from api generate dict list of the data'''
    newer_dict = []
    for alist in json_data:
        for adict in alist:
            parsed = adict
            newer_dict.append(parsed)
        
    return newer_dict



def ref_generator(df, x="Cost", y="_id"):
    df = df[[x,y]]
    small_list = []
    for key,row in df.iterrows():
        if type(row[x]) == list and len(row[x]) > 0:
            col1 = row[x]
            col2 = row[y]
            small_dict = {}
            for value in col1:
                small_dict[x]=value
                small_dict[y]=col2
                small_list.append(small_dict)
            
    df = pd.DataFrame(small_list)           
    return df


def insert_reference_tables(TABLE = "Rel_Files_Cost", table = "Files",x="Cost"):    
    saveto = '{}/data3/{}.csv'.format(path,table)
    table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
    json_data = incremental_api_call(table)
    jd = references_generator(json_data)
    df = pd.DataFrame(jd) 
    df = ref_generator(df,x, y="_id")
    df.to_csv(saveto, index=False)
    try:
        write_bq(saveto, table_id)
        print(saveto)
        logger.info("SUCCESSFUL REFERENCE TABLE INSERT: {}".format(TABLE))
    except:
        #print(e)
        logger.error("ERROR REFERENCE TABLE INSERT: {}".format(TABLE))


insert_reference_tables(TABLE = "Rel_Files_Cost", table = "Files",x="Cost")
#Rel_Files_Forms
insert_reference_tables(TABLE = "Rel_Files_Forms", table = "Files",x="Forms")
#Rel_Files_References
insert_reference_tables(TABLE = "Rel_Files_References", table = "Files",x="References")

#Rel_Files_Revenue
insert_reference_tables(TABLE = "Rel_Files_Revenue", table = "Files",x="Revenue")

#Rel_Files_Timestamps
insert_reference_tables(TABLE = "Rel_Files_Timestamps", table = "Files",x="Timestamps")


#Rel_Forms_Forms
insert_reference_tables(TABLE = "Rel_Forms_Forms", table = "Forms",x="SubForms")

#Rel_Forms_FormValues
insert_reference_tables(TABLE = "Rel_Forms_FormValues", table = "Forms",x="Values")
