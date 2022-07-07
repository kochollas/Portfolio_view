from utils.libraries import * 
from schemas.database_tables import Companies
import pandas as pd

import logging
if not os.path.isdir('Log'):
    os.mkdir('Log')
#setting up basic logging
logging.basicConfig(filename='Log/log.txt',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


TABLE = "Companies"
csv_source = '{}/data/{}.csv'.format(path, TABLE)
csv_source2 = '{}/data2/{}.csv'.format(path, TABLE)

table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)

def api_call_modified(url,cursor=0):
    #This function is for making the various API calls by providing the URLs within bubble.io
    headers = {'Authorization': 'Bearer 629ed23ef839b0b9f4557672d94137b3'}
    result = requests.get(url, headers=headers,params={'limit':'100','cursor':cursor}) 
    if result.status_code ==200:
        output = result.content        
        output = output.decode('utf8')
        data = json.loads(output)
        return data
    else:
        print('Problem with api call: {}'.format(url))


table = "Companies"
url = "https://tms.airexpresshaiti.com/version-test/api/1.1/obj/{}".format(table)

json = api_call_modified(url = url)
json = json['response']['results']

Comps = []
for data in json:
    cols = list(data.keys())
    to_drop =  list(set(cols) - set(Companies))
    for k in to_drop:
        del(data[k])
    to_add = list(set(Companies)- set(cols))
    for k in to_add:
        data[k] = 'NA'
    Comps.append(data)


write_csv(Comps,table = "Companies",table_schema = Companies)
write_bq(csv_source, table_id)
logger.info("SUCCESSFUL BIGQUERY POPULATION: {}".format(TABLE))
