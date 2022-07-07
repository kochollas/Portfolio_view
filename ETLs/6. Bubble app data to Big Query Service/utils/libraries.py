import os
import pandas as pd
from google.cloud import bigquery
import requests
import json
import datetime
from dotenv import load_dotenv
load_dotenv('/home/mikes/Documents/upwork/Jan/bubble_bigQuery_service/app.env')

PROJECT = os.environ['PROJECT']

DATASET = os.environ['DATASET']

path = os.environ['path'] #data path

path_to_mod = os.environ['path_to_mod'] 

print("---libraries imported successfully---")
print('PROJECT :{} DATASET :{}'.format(PROJECT, DATASET))

client = bigquery.Client.from_service_account_json(path_to_mod)

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



def api_call_contrained(url,cursor=0):    
    day = datetime.datetime.now().date()
    yesterday = day - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y-%m-%d")
    yesteday = '{}'.format(yesterday)

    '''This function is for making the various API calls by providing the URLs within bubble.io'''
    headers = {'Authorization': 'Bearer 629ed23ef839b0b9f4557672d94137b3'}
    constraints = [{ "key": "Modified Date", "constraint_type": "equals", "value": yesteday }] 

    url = "https://tms.airexpresshaiti.com/version-test/api/1.1/obj/{}?constraints={}".format(table.lower(),constraints)

    result = requests.get(url, headers=headers,params={'limit':'100','cursor':cursor}) 
    if result.status_code ==200:
        output = result.content
        output = output.decode('utf8').replace("'", '"')
        data = json.loads(output)
        return data
    else:
        print('Problem with api call: {}'.format(url))



def api_call(url,cursor=0, modified = False):
    '''This function is for making the various API calls by providing the URLs within bubble.io'''
    headers = {'Authorization': 'Bearer 629ed23ef839b0b9f4557672d94137b3'}
    result = requests.get(url, headers=headers,params={'limit':'100','cursor':cursor}) 
    if result.status_code ==200:
        output = result.content
        output = output.decode('utf8').replace("'", '"')        
        data = json.loads(output)
        return data
    else:
        print('Problem with api call: {}'.format(url))



def generate_csv(json_response):
    res = json_response['response']['results']
    df = pd.DataFrame(res)
    return df

def drop_listed_columns(column_list, dataframe, add_columns=[]):
    col_list = dataframe.columns
    for val in column_list:
        if val in col_list:
            dataframe.drop([val], inplace=True, axis=1)
    '''Add some empty columns to match bubble and big query schema'''
    if len(add_columns) >= 1:
        for value in add_columns:
            dataframe[value] = ""

        
    return dataframe


def incremental_api_call(table = "AttachmentTypes"):
    remainder = 1
    cursor = 0
    master = []
    while remainder !=0:
        url = "https://tms.airexpresshaiti.com/version-test/api/1.1/obj/{}".format(table.lower())
        json_obj = api_call(url, cursor=cursor)
        data = json_obj['response']['results']
        master.append(data)
        print(json_obj['response']['count'])
        remainder = int(json_obj['response']['remaining'])
        print(remainder)
        cursor +=100
    return master
        



def data_for_bq(cols_to_delete ,json_data, table = "AttachmentTypes",add_columns=[]):
    i = 0
    while i < len(json_data):
        df = pd.DataFrame(json_data[i])
        df = drop_listed_columns(cols_to_delete, df,add_columns)
        if i == 0:
            headerflag = True
        else:
            headerflag = False
        saveto = '{}data/{}.csv'.format(path,table)
        df = handle_datetime_columns(df)
        df.to_csv(saveto, index = False, mode = 'a', header=headerflag)

        i +=1

def datetime_gen(row):
    z = row[0:len(row)-5]+'Z'
    z = datetime.datetime.strptime(z, "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d %H:%M:%S')
    return z



def handle_datetime_columns(df):
    cols = df.columns
    if "Created Date" in cols:
        df["Created_Date"] = df["Created Date"].apply(datetime_gen)
        df["Created_Date"] = pd.to_datetime(df["Created_Date"])
        
    if "Modified Date" in cols:
        df["Modified_Date"] = df["Modified Date"].apply(datetime_gen)
        df["Modified_Date"] = pd.to_datetime(df["Modified_Date"])
    # ExchangeRates 
    if "EffectiveDateEnd" in cols:
        df["EffectiveDateEnd"] = df["EffectiveDateEnd"].apply(datetime_gen)
        df["EffectiveDateEnd"] = pd.to_datetime(df["EffectiveDateEnd"])
    if "EffectiveDateStart" in cols:
        df["EffectiveDateStart"] = df["EffectiveDateStart"].apply(datetime_gen)
        df["EffectiveDateStart"] = pd.to_datetime(df["EffectiveDateStart"])
    #Timestamps
    if "Timestamps" in cols:
        df["Timestamps"] = df["Timestamps"].apply(datetime_gen)
        df["Timestamps"] = pd.to_datetime(df["Timestamps"])
        
    return df





def handle_column_naming_datetime(a_dict, table_schema = []):
    '''matching schemas and runs on single dict'''
    cols = list(a_dict.keys())
    for key in cols:
        if key == 'Created Date':
            a_dict['Created_Date']=datetime_gen(a_dict[key])  
            del(a_dict['Created Date'])
        if key == 'Modified Date':
            a_dict['Modified_Date']=datetime_gen(a_dict[key])
            del(a_dict['Modified Date'])
        if key == 'Created By':
            a_dict['Created_By']= a_dict[key]
            del(a_dict['Created By'])
        if key == 'Text':
            a_dict['Text']= a_dict[key][0:30] 
    
    
    '''Check the keys of the returned dict if it matches the table structure'''
    if len(cols) != len(table_schema):        
        missing = list(set(table_schema) - set(cols))
        print(missing)
        for k in missing:
            if k in ('Created_Date','Modified_Date'):
                a_dict[k] = '2000-06-15 12:00:00' 
            else:
                a_dict[k] = 'NA'   
    '''  
    if len(cols) > len(table_schema):
        extra = list(set(cols) - set(table_schema))
        for j in extra:
            del(a_dict[j])    
    '''
    return a_dict



def jsons_gen(json_data,table_schema):
    '''Calls above with json_data from api generate dict list of the data'''
    newer_dict = []
    for alist in json_data:
        for adict in alist:
            a_dict = adict            
            parsed = handle_column_naming_datetime(a_dict, table_schema)            
            newer_dict.append(parsed)
    return newer_dict

def write_csv(alist_of_dict,table,table_schema = []):
    df = pd.DataFrame(alist_of_dict)
    cols = list(df.columns)
    if len(cols) > len(table_schema):
        print(list(cols), len(cols),len(table_schema))
        remove_list = list(set(cols) - set(table_schema))
        print(remove_list)
        df = df.drop(remove_list, axis = 1)
    #df = df[table_schema]
    if len(table_schema) != 0:
        df = df[table_schema]
    df.to_csv('{}data2/{}.csv'.format(path,table), index = False)
    df.to_csv('{}data/{}.csv'.format(path,table), index = False)
    return df
    

#incremental_api_call_yesterday

def incremental_api_call_yesterday(table = "AttachmentTypes"):
    remainder = 1
    cursor = 0
    master = []
    while remainder !=0:
        url = "https://tms.airexpresshaiti.com/version-test/api/1.1/obj/{}".format(table.lower())
        json_obj = api_call_contrained(url,cursor=cursor)
        data = json_obj['response']['results']
        master.append(data)
        print(json_obj['response']['count'])
        remainder = int(json_obj['response']['remaining'])
        print(remainder)
        cursor +=100
    return master






