# Generating List 0

import requests
import pandas as pd
import numpy as np
import time
import re
import datetime

# Handling List0

# handling the api calls

def api_call(url):
    '''This function is for making the various API calls by providing the URLs within polygon.io'''
    headers = {'Authorization': 'Bearer xxx'}
    result = requests.get(url, headers=headers)
    return result



def ticker_response_handler(M):
    stocks = []

    for i in range(len(M)):
        k = M[i]['ticker']
        list_date = ticker_details(k)
        if 'list_date' in list_date['results']:
            date_started = list_date['results']['list_date']
        else:
            date_started = 'NA'      
        
        
        if 'primary_exchange' in M[i].keys():
            prim_xchange = M[i]['primary_exchange']
        else:
            prim_xchange = 'NA'            
         
        stocks.append({'symbol':M[i]['ticker'],'name':M[i]['name'],'exchange':prim_xchange,'list_date':date_started})

    return stocks    



def ticker_names(url):
    '''Pull ticker names which should be used downstream'''
    response = api_call(url) 
    response = response.json()
    res = ticker_response_handler(response['results'])
    
    count = 1
    list_of_dict = []
    
    while count <=13: # 'next_url' in response.keys():
        next_url = response['next_url']
        response = api_call(url = next_url)
        response = response.json()
        data = ticker_response_handler(response['results'])
        list_of_dict.append(data)
        print("{}:{}".format(count,next_url))
        
        count +=1
     
    return res, list_of_dict


def ticker_details(ticker_name):
    ticker_url = 'https://api.polygon.io/v3/reference/tickers/{}'.format(ticker_name)
    details = api_call(ticker_url)
    details = details.json()
    return details


def incremental_read_from_csv(start,size, datafile):
    '''This function reads chunks of data from a csv file'''
    tab_data = pd.read_csv(datafile,header = None,skiprows = start,nrows =size)
    return tab_data


def formated_time(unix_time):
    date_time = datetime.datetime.fromtimestamp(unix_time)
    t = date_time.strftime('%Y-%m-%d %H:%M:%S')
    return t


