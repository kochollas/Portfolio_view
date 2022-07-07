from schemas.database_tables import *
from utils.libraries import *

import sqlite3
from sqlite3 import Error
from os.path import exists

import logging
if not os.path.isdir('Log'):
    os.mkdir('Log')
#setting up basic logging
logging.basicConfig(filename='Log/log.txt',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def jsons_gen(json_data,table_schema):
    '''Calls above with json_data from api generate dict list of the data'''
    newer_dict = []
    for alist in json_data:
        for adict in alist:
            a_dict = adict
            parsed = handle_column_naming_datetime(a_dict, table_schema)
            newer_dict.append(parsed)
    return newer_dict
        


def write_csv(alist_of_dict,table, table_schema = []):
    df = pd.DataFrame(alist_of_dict)
    cols = list(df.columns)
    if len(cols) > len(table_schema):
        print(list(cols), len(cols),len(table_schema))
        remove_list = list(set(cols) - set(table_schema))
        print(remove_list)
        df = df.drop(remove_list, axis = 1)
    df.to_csv('{}data3/{}.csv'.format(path,table), index = False)
    print(list(df.columns))
    return df

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_tasks(conn,PROJECT,DATASET,TABLE):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM `tms.db`")

    rows = cur.fetchall()
    counter = 0
    for row in rows:
        
        Q = 'INSERT INTO `{}.{}.{}` VALUES {}'.format(PROJECT,DATASET,TABLE, row)
        print(row)        
        QUERY = (Q)
        try:
            query_job = client.query(QUERY)
            rows = query_job.result()
            print("UPDATE SUCCESS:{}:{}".format(TABLE, row[0]))
        except:
            logger.error('UPDATE ERRORs:{}:{}'.format(TABLE, row[0]))
        counter +=1
    logger.info('SUCCESSFUL BIGQUERY POPULATION : {} ({})'.format(TABLE, counter))


def Alternative_insert(table,table_schema,PROJECT = PROJECT, DATASET = DATASET):
    json_data = incremental_api_call(table)
    jd = jsons_gen(json_data,table_schema)    
    df = write_csv(jd,table,table_schema)
    df.head()
    TABLE = table
    file_exists = exists('tms.db')
    if file_exists:
        os.remove('tms.db')

    conn = create_connection('tms.db')

    df.to_sql("tms.db", conn, if_exists='append', index=False)
    select_all_tasks(conn, PROJECT,DATASET,TABLE)



#References
Alternative_insert(table="References",table_schema=References)

#FormValueTypes
Alternative_insert(table="FormValueTypes",table_schema=FormValueTypes)

# Files   
Alternative_insert(table="Files",table_schema=Files)

#AuditLogEntries
Alternative_insert(table="AuditLogEntries",table_schema=AuditLogEntries)

#Comments
Alternative_insert(table="Comments",table_schema=Comments)

