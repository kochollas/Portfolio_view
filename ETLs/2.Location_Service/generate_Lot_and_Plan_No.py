#IMPORTING NECESSARY LIBRARIES
import sys, os
import numpy as np
import pandas as pd
#import sqlite3
#from sqlite3 import Error # To habdle database errors

print('COMPLETED LIBRARY SET-UP ...')
#setting path to the provided csv files saved on a folder named Data
csv_folder = os.getcwd()+r'/Data/'

# Reading desc data
desc = pd.read_csv(csv_folder+"spu159mtg.land_description.csv",low_memory=False)
print(desc.columns)
print(len(desc))
desc = desc.iloc[0:5000,:]

desc.loc[desc['Plan Type'] == "CP", "Plan.No"] = desc['Plan No']
desc.loc[desc['Plan Type'] != "CP", "Plan.No"] = desc['Plan Type']+desc['Plan No']

desc.to_csv('Base_lotplan.csv', index = False)

desc = desc.dropna()
# write a csv copy of generated lot and plan numbers for api calling
desc = desc[['Lot No','Plan.No']]
desc.to_csv('lotplan.csv', index = False)

tab_data = len(desc)
'''
# Will be used with database set up
print("COMPLETED CSV INGESTION AND DATA PROCESSING...")

#Setting up SQLite database connection
def create_connection(database_file, path_to_working_directory = os.getcwd()):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(path_to_working_directory+'/'+database_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

conn1 = create_connection(database_file="address.db")

desc.to_sql("address.db", conn1, if_exists='append', index=False)

print("COMPLETED DATABASE UPDATE...")

tab_data = pd.read_sql_query("SELECT COUNT(*) FROM `address.db`", conn1)
print(tab_data)
'''
#conn1.close()

print("All Data processed saved on address.db ")
print(tab_data)
print("---END---")


