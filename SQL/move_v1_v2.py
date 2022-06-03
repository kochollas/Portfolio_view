#import libs
import sys, os, re
import pandas as pd
import numpy as np
import pymysql
import sqlalchemy as db

print("---LOADED REQUIRED PACKAGES---")

class db_connection():

    def __init__(self,database_name="report"):
        if database_name == 'report':
            #report_2_connection
            self.database = 'report'
            self.server = 'localhost' 
            self.username = 'root' 
            self.password = '54321'   
        elif database_name == 'report_2':
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

database_report = db_connection('report')
database_report_2 = db_connection('report_2')

query_market = 'select id, name, search_volume, report_market_id from market'

query_customer = """
select 
c.id,
c.lead_id,
concat(c.first_name," ",c.last_name) as name,
m.name as market_id,
c.cluster_id,
c.venue_id,
c.package_id,
p.name as package_name,
c.city,
c.state,
c.guest_no,
c.hear_about_us,
c.cancel,
date(c.cancel_date) as cancel_date,
c.postponed,
date(r.deposit_date) as created_at,
r.deposit_amount,
r.id as reports_id,
r.invoice_amount,
r.vn_amount_with_spo,
r.vn_amount,
r.se_amount,
r.se_amount_with_spo,
c.wedding_date,
yearweek(r.deposit_date,1) as weekYear
from customers c
left join markets m on m.id = c.location_id
left join reports r on r.customer_id = c.id
left join packages p on p.id = c.package_id
where c.created_at > "2017-09-31"
and c.testing = 'N'
and c.deleted = 0
"""

df_market = database_report_2.get_query(query_market)

df_customer = database_report.get_query(query_customer)

#----customer
df_market.columns = ['id', 'market_id', 'search_volume','report_market_id']
df_customer = df_customer.merge(df_market,on="market_id",how='left')
df_customer = df_customer[['id_x','lead_id','name','id_y','cluster_id','venue_id','package_id','package_name','city','state','guest_no','hear_about_us','cancel','cancel_date','postponed','created_at','wedding_date','deposit_amount','reports_id','invoice_amount','vn_amount_with_spo','vn_amount','se_amount','se_amount_with_spo','weekYear']]
df_customer.columns = ['id','lead_id','name','market_id','cluster_id','venue_id','package_id','package_name','city','state','guest_no','hear_about_us','cancel','cancel_date','postponed','created_at','wedding_date','deposit_amount','reports_id','invoice_amount','vn_amount_with_spo','vn_amount','se_amount','se_amount_with_spo','weekYear']
df_customer['market_id'].fillna(16,inplace=True)
df_customer['deposit_amount'].fillna(0, inplace=True)
df_customer['invoice_amount'].fillna(0, inplace=True)
df_customer['vn_amount_with_spo'].fillna(0, inplace=True)
df_customer['vn_amount'].fillna(0, inplace=True)
df_customer['se_amount'].fillna(0, inplace=True)
df_customer['se_amount_with_spo'].fillna(0, inplace=True)


#df_customer = df_customer.merge(df_customer_type,how='left',on='id')

database_report_2.upload_df(df_customer,'customer',if_exists='replace', index = False)

print("DONE")
