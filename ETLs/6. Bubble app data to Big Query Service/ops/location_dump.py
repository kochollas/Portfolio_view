import numpy as np
from utils.libraries import *
from schemas.database_tables import *
import os
import logging
if not os.path.isdir('Log'):
    os.mkdir('Log')
#setting up basic logging
logging.basicConfig(filename='Log/log.txt',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# references tables generation
def references_generator(json_data):
    '''Calls above with json_data from api generate dict list of the data'''
    newer_dict = []
    for alist in json_data:
        for adict in alist:
            parsed = adict
            newer_dict.append(parsed)
        
    return newer_dict



#generate single data values from the dictionary

def dict_split(row, key):
    row = row[key]
    return row
    

# Files
json_data = incremental_api_call("Files")


jd = references_generator(json_data)
df = pd.DataFrame(jd)
df = df[['Customer','Origin','Destination']]
df = df[df['Origin'].notnull()]
df = df[df['Destination'].notnull()]

df['OriginLat'] = df.Origin.apply(dict_split,key='lat')
df['OriginLng'] = df.Origin.apply(dict_split,key='lng')
df['OriginAddress'] = df.Origin.apply(dict_split,key='address')


df['DestinationLat'] = df.Destination.apply(dict_split,key='lat')
df['DestinationLng'] = df.Destination.apply(dict_split,key='lng')
df['DestinationAddress'] = df.Destination.apply(dict_split,key='address')

df = df.drop(['Origin','Destination'], axis=1)
df.to_csv('files_location.csv', index = False)


# Timestamps

json_data = incremental_api_call("Timestamps")
jd = references_generator(json_data)
df = pd.DataFrame(jd)
df = df[['_id','Location']]
df = df[df['Location'].notnull()]
df['LocationLat'] = df.Location.apply(dict_split,key='lat')
df['LocationLng'] = df.Location.apply(dict_split,key='lng')
df['LocationAddress'] = df.Location.apply(dict_split,key='address')
df = df.drop(['Location'], axis = 1)
df.to_csv('timestamp_location.csv', index = False)


# sending data to bigQuery

def bq_insert(TABLE):
    csv_source = '{}.csv'.format(TABLE)
    table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
    write_bq(csv_source, table_id)
    logger.info('SUCCESSFUL LOCATION TABLE INSERT : {}'.format(TABLE))


bq_insert(TABLE = 'files_location')
bq_insert(TABLE = 'timestamp_location')

