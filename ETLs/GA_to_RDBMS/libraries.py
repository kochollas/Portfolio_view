import sys
import os
import re

#path_to_modules = '/home/mikes/Documents/upwork'
path_to_modules = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if path_to_modules not in sys.path:
    sys.path.insert(0, path_to_modules)
#from components.database_management import *

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
import pymysql
import sqlalchemy
import datetime
from datetime import datetime as datenow

print("---LOADED LIBRARIES SUCCESSFULLY---")
# To work with dates ['daily', 'weekly'] date ranges

def date_range(duration = 'daily'):
    day = datenow.now().date()
    if duration == 'weekly':  
        yesterday = day - datetime.timedelta(days=1)
        start_date = day - datetime.timedelta(days=7)
        end_str = yesterday.strftime("%Y-%m-%d")
        start_str = start_date.strftime("%Y-%m-%d")
        return start_str, end_str      

    else:
        yesterday = day - datetime.timedelta(days=1)
        start_str = yesterday.strftime("%Y-%m-%d")
        end_str = yesterday.strftime("%Y-%m-%d")
        return start_str, end_str

# Pulls data for a single metric given query output and metric name
def single_metric_output(query_string, metric_KPI):
    df = pd.DataFrame(query_string)
    headers = df['reports'].iloc[0]['columnHeader']
    df1 = pd.DataFrame(df['reports'].iloc[0]['data']['rows'])
    df1[metric_KPI] = df1['metrics'].apply(lambda x: x[0]['values'][0])
    df1 = df1.drop('metrics',axis=1)
    df1    
    return df1[metric_KPI][0]

# Returns dataframe of a single metric with a dimension
def single_metric_single_dimension_output(query_output, metricKPI, dimKPI):
    df = pd.DataFrame(query_output)
    headers = df['reports'].iloc[0]['columnHeader']
    df1 = pd.DataFrame(df['reports'].iloc[0]['data']['rows'])
    df1[metricKPI] = df1['metrics'].apply(lambda x: x[0]['values'][0])
    df1[dimKPI] = df1['dimensions'].apply(lambda x: x[0])
    df1 = df1.drop('metrics',axis=1)
    df1 = df1.drop('dimensions',axis=1)
    return df1
# Returns a dictionary of Landing page including virtual will be useful in geting excluded segment
def landing_page_include_virtual(urlsData):
    landpageView = {} 
    df1 = urlsData.loc[urlsData["url"].str.contains('virtual', flags =re.I, regex=True)]        
    landpageView["landingPage containing virtual"]=pd.to_numeric(df1.iloc[:,0]).sum()
    return landpageView

# returns a dictionary of various destinations for users sessions and entrances
def destination_data(destinations,urlsData):
    destinationView = {}
    for destination in destinations:
        df1 = urlsData.loc[urlsData["url"].str.contains(destination, flags =re.I, regex=True)]        
        destinationView[destination]=pd.to_numeric(df1.iloc[:,0]).sum()
    return destinationView

# Separates URL and url parameters
def url_separator(url):
    if "?" in url:
         
        return url[0:url.find('?')]
        
    else:
        return url
        
def destination_dataEntrance(destinations,urlsData):
    urlsData["url_reduced"] = urlsData["url"].apply(url_separator) # added a function to separate url in parts
    destinationView = {}
    for destination in destinations:
        df1 = urlsData.loc[urlsData["url_reduced"].str.contains('/'+destination, flags =re.I, regex=True)]        
        destinationView[destination]=pd.to_numeric(df1.iloc[:,0]).sum()
    return destinationView


# Returns a dictionary of Destination pages entrance with the url part
def elopement_packages(urlsData, url_part):
    destinationView = {}    
    df1 = urlsData.loc[urlsData["url"].str.contains(url_part, flags =re.I, regex=True)]        
    destinationView["Destination Pages entrances"]=pd.to_numeric(df1.iloc[:,0]).sum()
    return destinationView


print("--- LOADED FUNCTIONS SUCCESS ---")

