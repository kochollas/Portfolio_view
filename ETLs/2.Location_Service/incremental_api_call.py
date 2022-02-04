import base64
import requests
import pandas as pd
from generate_Lot_and_Plan_No import *

def incremental_read_from_csv(start,size):
    '''This function reads chunks of data from a csv file'''
    tab_data = pd.read_csv(os.getcwd()+r'/XXX.csv',header = None,skiprows = start+1,nrows =size)
    return tab_data


def incremental_read_from_db(start, size):
    '''This function helps to read chunks of data from the database for forward processing'''
    tab_data = pd.read_sql_query("SELECT * FROM `address.db` LIMIT {},{}".format(start,size), conn1)
    return tab_data


def generate_payload_input(data_chunk, index_val):
    ''' This function generates single lot and plan number for small data chunks obtained 
    from incremental_read_from_db() return value'''
    if index_val < len(data_chunk):
        input_list = [str(data_chunk.iloc[index_val,0]),data_chunk.iloc[index_val,1]]
        return input_list
    else:
        print('The index_val cannot exceed the length of the your input data chunks')





def api_call(LotNumber, PlanNumber):
    '''This function makes the api call and returns a json object'''
    payload = {
    "ValidateLotPlan": {
        "MeshblockOption": "Exclude",
        "LotNumber": XXX,
        "PlanNumber": XXX
    }

    }
    userpass = 'XXX' + ':' + 'XXX'
    encoded_u = base64.b64encode(userpass.encode()).decode()
    headers = {"Authorization": "Basic %s" % encoded_u}

    private_api_URL = "XXX"
    r = requests.post(private_api_URL, json=payload, headers=headers) 
    resp = r.json()  
    return resp



def json_response_handler(jsondata,payload_args):
    '''This function will handle the api response and returns a dictionary'''
    is_successful_output = jsondata['ValidateLotPlanResponse']['ValidateLotPlanResult']['ResultCount']
    result_dict = {}
    if is_successful_output == '1':
        created_at = jsondata['ValidateLotPlanResponse']['ValidateLotPlanResult']['Results']['Result']['MetaData'][0]['Value']
        address = jsondata['ValidateLotPlanResponse']['ValidateLotPlanResult']['Results']['Result']['MetaData'][1]['Value']
        Latitude = jsondata['ValidateLotPlanResponse']['ValidateLotPlanResult']['Results']['Result']['Geocode']['Latitude']
        Longitude = jsondata['ValidateLotPlanResponse']['ValidateLotPlanResult']['Results']['Result']['Geocode']['Longitude']
        result_dict['lot_number'] = payload_args[0]
        result_dict['plan_number'] = payload_args[1]
        result_dict['created_at'] = created_at
        result_dict['address'] = address
        result_dict['Latitude'] = Latitude
        result_dict['Longitude'] = Longitude
    else:
        result_dict['lot_number'] = payload_args[0]
        result_dict['plan_number'] = payload_args[1]
        result_dict['created_at'] = np.nan
        result_dict['address'] = np.nan
        result_dict['Latitude'] = np.nan
        result_dict['Longitude'] = np.nan
    return result_dict

 

def sequential_api_call(size_of_data_file, chunking_size):
    '''This function calls the api with the data chunks in an incremental fashion and writes to csv file'''
    chunks_init = 0
    while chunks_init < size_of_data_file:
        
        data_chunk = incremental_read_from_csv(chunks_init,chunking_size)
        temp_df = pd.DataFrame()

        for i in range(len(data_chunk)):
            #print(i)
            payload_args = generate_payload_input(data_chunk,i)
            #print(payload_args)
            '''Call the api here and write the output on a temp file'''
            json_response = api_call(payload_args[0],payload_args[1])
            dict_response = json_response_handler(json_response,payload_args)
            # create a temp dataframe to hold every chunk processed and write it to db            
            temp_df = temp_df.append(dict_response, ignore_index=True)  

        print(chunks_init)
        #Write to csv or database of choice
        temp_df.to_csv('processed_lotplan.csv', index = False, mode = 'a', header=False)
        chunks_init +=chunking_size
    
def merging_to_previous_data():
    '''This function helps in joining api results to the initial dataset'''
    api_data = pd.read_csv('processed_lotplan.csv', header=None)
    api_data.columns = ['Lot No','Plan.No','Created_at','Address','Latitude','Longitude']
    #merging to initial data
    initial_data = pd.read_csv('Base_lotplan.csv')
    final_data = initial_data.merge(api_data, how = 'left', on= ['Lot No','Plan.No'])
    final_data.to_csv('finalProcessedData.csv', index = False)
    print("---END--- \n CHECK FOR finalProcessedData.csv")
    return final_data.head()
