import os,sys
from os.path import exists
from google.cloud import bigquery
import datetime

from dotenv import load_dotenv
load_dotenv('/home/mikes/Documents/upwork/Jan/bubble_bigQuery_service/app.env')

PROJECT = os.environ['PROJECT']

DATASET = os.environ['DATASET']

path = os.environ['path'] #data path

path_to_mod = os.environ['path_to_mod'] 

import logging
if not os.path.isdir('Log'):
    os.mkdir('Log')
#setting up basic logging
logging.basicConfig(filename='Log/log.txt',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('START : {}'.format(datetime.datetime.now()))

path_to_modules = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if path_to_modules not in sys.path:
    sys.path.insert(0, path_to_modules)


from schemas.database_tables import *
from utils.libraries import *


job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
)

def write_bq(csv_source, table_id):
    '''to write to big query specified data set'''
    with open(csv_source, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    job.result()  


def actual_bq_insert(table , cols_to_delete = [], add_columns=[], table_schema = []):
    '''calls api generate csv and write big query'''
    global API_SUCCESS 
    API_SUCCESS = False
    global CSV_SUCCESS 
    CSV_SUCCESS = False
    path = os.environ['path']
    TABLE = table
    csv_source = '{}/data/{}.csv'.format(path,TABLE)
    csv_source2 = '{}/data2/{}.csv'.format(path, TABLE)

    table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
    try:  
        json_data = incremental_api_call(table)
        logger.info("SUCCESSFUL API FOR: {}".format(table))
        logger.info(csv_source)
        API_SUCCESS = True
    except:
        logger.info("ERROR WITH API FOR: {}".format(table))
    file_exists = exists(csv_source)
    if file_exists:
        os.remove(csv_source)
    try:
        res_dict = jsons_gen(json_data,table_schema)
        write_csv(res_dict, table,table_schema)
        logger.info("SUCCESSFUL CSV DUMPS: {}".format(table))
        CSV_SUCCESS = True
    except:
        logger.info("ERROR WITH CSV DUMP: {}".format(table))
 
    try:
        if CSV_SUCCESS:
            write_bq(csv_source, table_id)
            logger.info("SUCCESSFUL BIGQUERY POPULATION: {}".format(table))

    except:
        logger.info("ERROR WITH BIGQUERY POPULATION: {}".format(table))
        ''' Implemented a second approach for problematic files'''
        if API_SUCCESS:
            res_dict = jsons_gen(json_data,table_schema)
            write_csv(res_dict, table,table_schema)
        #try:
            logger.info("ATTEMPT TWO ")
            write_bq(csv_source2, table_id)
            logger.info(csv_source2)
            logger.info("SUCCESSFUL BIGQUERY POPULATION ATTEMPT2: {}".format(table))
        #except:
            #logger.info(e)
            logger.info("ERROR BIGQUERY POPULATION ATTEMPT2: {}".format(table))
    
#Clean the big Query Tables
from schemas.schema import *
# 1. AttachmentTypes
actual_bq_insert(table = "AttachmentTypes", table_schema= AttachmentTypes)

# 2. Attachments
actual_bq_insert(table = "Attachments", table_schema= Attachments)     

# 4. ChargeTypes
actual_bq_insert(table = "ChargeTypes", table_schema= ChargeTypes)

# 7. Currencies
actual_bq_insert(table = "Currencies", table_schema = Currencies)

# 8.Customers
actual_bq_insert(table = "Customers",table_schema = Customers)

# 11. FileStatuses
actual_bq_insert(table = "FileStatuses", table_schema = FileStatuses)

 #12. FileTypes
actual_bq_insert(table = "FileTypes", table_schema = FileTypes)

# 13. Financials
actual_bq_insert(table = "Financials", table_schema = Financials)

# 19. ReferenceTypes
actual_bq_insert(table = "ReferenceTypes",table_schema = ReferenceTypes)

# 20. Roles
actual_bq_insert(table = "Roles", table_schema = Roles)

# 21. Timestamps
actual_bq_insert(table = "Timestamps", table_schema = Timestamps)

# 22. TimestampTypes
actual_bq_insert(table = "TimestampTypes", table_schema = TimestampTypes)

# 23. User

actual_bq_insert(table = "User",table_schema = User)

# 24. VisibilityTypes
actual_bq_insert(table = "VisibilityTypes",table_schema = VisibilityTypes)

# 25. Deletion
actual_bq_insert(table = "Deletion", table_schema = Deletion)

actual_bq_insert(table="Forms",table_schema=Forms)

# 9 ExchangeRates
actual_bq_insert(table = "ExchangeRates",table_schema = ExchangeRates)

## OTHER INSERTS
from ops.inserts import *
from ops.companies import *

# ADDING DATA FOR REFERNCE TABLES
from ops.reference_tables import *

# ADDING DATA FOR LOCATIONS
from ops.location_dump import *

logger.info('END : {}'.format(datetime.datetime.now()))




