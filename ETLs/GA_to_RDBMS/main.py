# Create a datbase for the GA data points and provide login credentials
import sqlalchemy as db
import pandas as pd
from GAminer import *


#database_connect
class db_connection():

    def __init__(self,database_name="report_2"):
        if database_name == 'report_2':
            #report_2_connection
            self.database = 'report_2'
            self.server = 'localhost' 
            self.username = 'root' 
            self.password = '54321'       


        self.engine = db.create_engine("mysql+pymysql://"+self.username+":"+self.password+"@"+self.server+"/"+self.database) 
    
    def get_query(self,query):
        '''
        Returns a pandas DF From an SQL query
        '''
        df = pd.read_sql(query,self.engine)
        return df
    
    def upload_df(self,df,table,index=True,index_label='id',if_exists='append'):
        '''
        Appends a DF to a table.
        Uses the index as the id for the table, so make sure the index is the right one. 
        '''
        df.to_sql(table,self.engine,index=index,if_exists=if_exists,index_label=index_label)
        
    def get_last_index(self,table):
        '''
        Returns an integer that is the max id of a table.
        '''
        query = "select max(id) as max from {}".format(str(table))
        df = pd.read_sql(query,self.engine)
        max_id = df['max'].iloc[0]
        return max_id
    
    def add_primary_key(self,table,define_id):
        try:
            query = 'alter table {} add primary key ({})'
            query = query.format(table,define_id)
            self.engine.execute(query)
            print ("Primary KEY added to: "+ table)
        except Exception as e:
            print (table+" Table Error: "+e.args[0])
    def get_row_count(self,table):
        '''Returns the number of rows in the table'''
        query = "select COUNT(*) as row_total from {}".format(str(table))
        df = pd.read_sql(query,self.engine)
        total_rows = df['row_total'].iloc[0]
        return total_rows
    

mysql =db_connection()


def insert_index(df,first_index=1):
    df.insert(0,'id',range(first_index,first_index + len(df)))
    return df



def inserting_df_toDB(df, tablename,conn):
    # check if table is empty
    if conn.get_row_count(tablename) > 0:
        n = mysql.get_last_index(tablename)
        insert_index(df,n+1)
        df.set_index('id')
        df.to_sql(tablename, mysql.engine,if_exists='append',index_label='id', index = False)
        print("*****************DATABASE UPDATE SUCCESS************************")
        
    else:
        insert_index(df,1)
        df.set_index('id')
        df.to_sql(tablename, mysql.engine,if_exists='append',index_label='id', index = False)
        print("*****************DATABASE UPDATE SUCCESS************************")

#DATABASE UPDATE
print("DAILY GOOGLE ANALYTICS UPDATE")
df = ga_Query_Calls(duration='daily')

#INSERTING DAILY DATA TO THE DB TABLES
inserting_df_toDB(df[0],'primary_metrics',mysql) 
inserting_df_toDB(df[1],'non_virtual_ga_metrics',mysql) 
inserting_df_toDB(df[2],'marketwise_traffic',mysql) 
inserting_df_toDB(df[3],'marketwise_traffic',mysql) 
inserting_df_toDB(df[4],'marketwise_traffic',mysql)  
inserting_df_toDB(df[5],'non_virtual_ga_metrics',mysql) 
inserting_df_toDB(df[6],'primary_metrics',mysql)

print("WEEKLY GOOGLE ANALYTICS UPDATE")

df = ga_Query_Calls(duration='weekly')
#INSERTING WEEKY DATA TO THE DB TABLES
inserting_df_toDB(df[0],'primary_metrics',mysql) 
inserting_df_toDB(df[1],'non_virtual_ga_metrics',mysql) 
inserting_df_toDB(df[2],'marketwise_traffic',mysql) 
inserting_df_toDB(df[3],'marketwise_traffic',mysql) 
inserting_df_toDB(df[4],'marketwise_traffic',mysql)  
inserting_df_toDB(df[5],'non_virtual_ga_metrics',mysql) 
inserting_df_toDB(df[6],'primary_metrics',mysql) 
# Script running after table population 

import mysql.connector as dbCon
from mysql.connector import Error

connection = dbCon.connect(host=mysql.server,
                            database=mysql.database,
                            user=mysql.username,
                            password=mysql.password)
mycursor = connection.cursor()

#Create a table to hold similar names for market table and destination users

mycursor.execute("DROP TEMPORARY TABLE IF EXISTS `name_and_id_temp`")
mycursor.execute("CREATE TEMPORARY TABLE `name_and_id_temp` (`name` varchar(100),`market` varchar(100), id INT)")

#Populate the created table name_and_id_temp with matching market names on both tables
query1='''
 INSERT INTO name_and_id_temp select LOWER(M.name),M.name, M.report_market_id from market as M where lower(M.name) IN (select distinct destination from marketwise_traffic)
'''
mycursor.execute(query1)
# Non matching names are added manually here
query2 = '''INSERT INTO name_and_id_temp VALUES('new-york-city', 'New York City', 1),('new-orleans', 'New Orleans', 2),('key-west', 'Key West', 27),
('lake-tahoe','Lake Tahoe',26),('las-vegas','Las Vegas',31),('san-diego','San Diego',22),('big-sur','Big Sur',29),('san-francisco','San Francisco',23),('st-augustine','St. Augustine',37),('washingtondc','Washington DC',43),('sun-valley','Sun Valley',46),('charleston','Charleston',50);

'''
mycursor.execute(query2)

mycursor.execute("SELECT * FROM name_and_id_temp")
markets = mycursor.fetchall()
market_list = []
for market in markets:
    market_list.append(market)

total_market_count = len(market_list)

for k in range(total_market_count):
    x = market_list[k][2]
    y = market_list[k][1]
    z = market_list[k][0]
    query3 = "UPDATE marketwise_traffic SET market_id = {0} ,market_name = '{1}' WHERE destination = '{2}'".format(x,y,z)

    mycursor.execute(query3)

connection.commit()

print("*****************END OF SCRIPT CHECK YOUR DB TABLES************************")
