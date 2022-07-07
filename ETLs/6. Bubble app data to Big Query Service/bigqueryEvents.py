from utils.libraries import *
from schemas.database_tables import *
import requests

import sqlite3
from sqlite3 import Error
from os.path import exists


def api_call_contrained(table):    
    day = datetime.datetime.now().date()
    yesterday = day - datetime.timedelta(days=3)
    yesterday = yesterday.strftime("%Y-%m-%d")
    yesteday = '{}'.format(yesterday)

    '''This function is for making the various API calls by providing the URLs within bubble.io'''
    headers = {'Authorization': 'Bearer 629ed23ef839b0b9f4557672d94137b3'}
    constraints = [{ "key": "Modified Date", "constraint_type": "greater than", "value": yesterday }] 

    #url = "https://tms.airexpresshaiti.com/version-test/api/1.1/obj/{}?constraints={}".format(self.table.lower(),constraints)
    url = "https://tms.airexpresshaiti.com/version-test/api/1.1/obj/{}?constraints={}".format(table.lower(),json.dumps(constraints, separators=(',', ':')))
    print(url)
    result = requests.get(url, headers=headers,params={'limit':'100','cursor':0})
    print(result.content) 
    if result.status_code ==200:
        output = result.content
        output = output.decode('utf8').replace("'", '"')
        data = json.loads(output)
        return data
    else:
        print('Problem with api call: {}'.format(url))

def incremental_api_call_yesterday(table):
    remainder = 1
    cursor = 0
    master = []
    while remainder !=0:
        #url = "https://tms.airexpresshaiti.com/version-test/api/1.1/obj/{}".format(self.table.lower())
        json_obj = api_call_contrained(table)
        data = json_obj['response']['results']
        master.append(data)
        print(json_obj['response']['count'])
        remainder = int(json_obj['response']['remaining'])
        print(remainder)
        cursor +=100
    return master


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

def delete_rows(table):
    df = pd.read_csv('{}data3/{}.csv'.format(path,table))
    df = df[['_id']]    

    for k,v in df.iterrows():
        TABLE = table
        ID = v['_id']
        Q = 'DELETE FROM `{}.{}.{}` WHERE _id="{}"'.format(PROJECT,DATASET,TABLE, ID)
        QUERY = (Q)
        try:
            query_job = client.query(QUERY)
            rows = query_job.result()
            print("DELETION SUCCESS:{}:{}".format(TABLE, ID))
        except:
            print('DELETION ERROR: CHECK IF TABLE OR COLUMN EXISTS:{}:{}'.format(TABLE, ID))



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

    for row in rows:
        
        Q = 'INSERT INTO `{}.{}.{}` VALUES {}'.format(PROJECT,DATASET,TABLE, row)
        print(row)        
        QUERY = (Q)
        try:
            query_job = client.query(QUERY)
            rows = query_job.result()
            print("UPDATE SUCCESS:{}:{}".format(TABLE, row[0]))
        except:
            print('UPDATE ERRORs:{}:{}'.format(TABLE, row[0]))
        


def Alternative_insert(table,table_schema,PROJECT = PROJECT, DATASET = DATASET):
    json_data = incremental_api_call_yesterday(table)
    jd = jsons_gen(json_data,table_schema)    
    df = write_csv(jd,table,table_schema)
    df.head()
    delete_rows('Attachments')
    TABLE = table
    file_exists = exists('tms.db')
    if file_exists:
        os.remove('tms.db')

    conn = create_connection('tms.db')

    df.to_sql("tms.db", conn, if_exists='append', index=False)
    select_all_tasks(conn, PROJECT,DATASET,TABLE)


#Actual updates of deleted row.
Alternative_insert(table="AttachmentTypes",table_schema=AttachmentTypes)





