# GENERATE LIST0
# CALLS TICKER AND TICKER DETAILS APIS
# APPXIMATE :30MINS
from libraries import *
import logging
import os
import datetime

if not os.path.isdir('Log0'):
    os.mkdir('Log0')

if not os.path.isdir('final0'):
    os.mkdir('final0')
#setting up basic logging
logging.basicConfig(filename='Log0/log0.txt',
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('START --------------------------- : {}'.format(datetime.datetime.now()))
url1 = "https://api.polygon.io/v3/reference/tickers?active=true&sort=ticker&order=asc&limit=1000"
M = ticker_names(url1)

print(M[0])

# creating first df
list01 = pd.DataFrame(M[0])
list01.to_csv('final0/final_list0.csv', index = False, mode = 'a', header=False)

#creating second ...  data frames

for val in M[1]:
    
    df02 = pd.DataFrame(val)
    df02.to_csv('final0/final_list0.csv', index = False, mode = 'a', header=False)
    logger.info('pagination : {} Added successfully {}'.format('####',len(df02)) )
    

logger.info('STOP --------------------------- : {}'.format(datetime.datetime.now()))

# PROCESSING THE RESULTS OF LIST0 CHECK 1
'''
check1 = ['NASDAQ','AMEX  American Exchange (AMX)','NYSE (NYE)','Arca']
check1_lower = [v.lower() for v in check1]



def check_one(row):
    row = row.lower()
    for value in check1_lower:
        if row in value or row[1:] in value:
            check_is = True
            break
        else:
            check_is = False
    return check_is
    
# Add the check1 to df

list_01['check1'] = list_01.exchange.apply(check_one)

list_01 = list_01.loc[list_01['check1']==True]



# PROCESSING THE RESULTS OF LIST0 CHECK 2

check2 = ['%',
    '%','/','ETF','Bond','Class A', '- Class B', 'Class D','Class E',
    'Series A', 'Series B', 'Series D','Series E','ordinary shares',
    'mutual funds', 'mutualfund']

    
check2_lower = [v.lower() for v in check2]

def check_two(row):
    row = row.lower()
    for value in check2_lower:
        if value in row:
            check_is = False
            break
        else:
            check_is = True
    return check_is


# add check 2 to df
list_01['check20'] = list_01.exchange.apply(check_two)
list_01['check21'] = list_01.name.apply(check_two)
list_01['check2'] = list_01.apply(lambda x:x['check20'] or x['check21'], axis = 1)

list_01 = list_01.loc[list_01['check20']==True]
list_01 = list_01.loc[list_01['check21']==True]
list_01 = list_01.loc[list_01['check2']==True]
# Add check 3

def check_three(row):
    row = row.lower()
    if row[len(row)-3:] in '.ws':
        check_is = False
    else:
        check_is = True
    return check_is


list_01['check30'] = list_01.symbol.apply(check_three) 
list_01['check31'] = list_01.name.apply(check_three) 
list_01 = list_01.loc[list_01['check30']==True]
list_01 = list_01.loc[list_01['check31']==True]
# working on the last test

df = list_01

# Remove duplicated u
tickers = list(df['symbol'].to_numpy())
tickers = [v.lower() for v in tickers]
Ws = [x for x in tickers if x[-1]=='w']
Us = [x for x in tickers if x[-1]=='u']

w_delete = []
for value in tickers:
    for val in Ws:
        if value == val[0:len(val)-1]:
            w_delete.append(val)
            break
            

u_delete = []            
for value in tickers:
    for val in Us:
        if value == val[0:len(val)-1]:
            u_delete.append(val)
            break



def remove_duplicates_U(row):
    row = row.lower()
    for k in u_delete:
        if row == k:
            state = 'delete'
            break
        else:
            state = 'okay'
    return state
   
def remove_duplicates_W(row):
    row = row.lower()
    for j in w_delete:
        if row == j:
            state = 'delete'
            break
        else:
            state = 'okay'
    return state   
    
    
df['check40'] = df.symbol.apply(remove_duplicates_U)

df['check41'] = df.symbol.apply(remove_duplicates_W)
    
df = df.loc[df['check40']=='okay']
df = df.loc[df['check41']=='okay']


print(len(df))
print(df.head(10))
df.to_csv('df4.csv',index = False)  
'''