import os
from google.cloud import bigquery
from dotenv import load_dotenv
load_dotenv('/home/mikes/Documents/upwork/Jan_german/bubble_bigQuery_service/app.env')

path_to_mod = os.environ['path_to_mod']

client = bigquery.Client.from_service_account_json(path_to_mod)

PROJECT = os.environ['PROJECT']

DATASET = os.environ['DATASET']
#SCHEMA DEFINITIONS

TABLE = "AttachmentTypes"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)

# Drop table then create it
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)

schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("DefaultVisibility", "STRING"),
    bigquery.SchemaField("Enterprise", "STRING"),
    bigquery.SchemaField("Modified_Date", "DATETIME"),
    bigquery.SchemaField("Name", "STRING"),
    bigquery.SchemaField("_id", "STRING"),
    bigquery.SchemaField("active", "STRING")
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

#2.Attachments

TABLE = "Attachments"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)

schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Modified_Date", "DATETIME"),
    bigquery.SchemaField("Name", "STRING"),
    bigquery.SchemaField("Owner", "STRING"),
    bigquery.SchemaField("Type", "STRING"),
    bigquery.SchemaField("Value", "STRING"),
    bigquery.SchemaField("Visibility", "STRING"), 
    bigquery.SchemaField("_id", "STRING")    
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#3.AuditLogEntries

TABLE = "AuditLogEntries"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)

schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "TIMESTAMP"),
    bigquery.SchemaField("Modified_Date", "TIMESTAMP"),
    bigquery.SchemaField("Object", "STRING"),
    bigquery.SchemaField("Owner", "STRING"),
    bigquery.SchemaField("Text", "STRING"),
    bigquery.SchemaField("_id", "STRING")    
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#4.ChargeTypes

TABLE = "ChargeTypes"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Enterprise", "STRING"),
    bigquery.SchemaField("Modified_Date", "DATETIME"),    
    bigquery.SchemaField("Name", "STRING"),    
    bigquery.SchemaField("_id", "STRING")    
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

#


#5.Comments 

TABLE = "Comments"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Modified_Date", "DATETIME"), 
    bigquery.SchemaField("Owner", "STRING"),       
    bigquery.SchemaField("Value", "STRING"),    
    bigquery.SchemaField("Visibility", "STRING"),
    bigquery.SchemaField("_id", "STRING")    
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#5.Companies 

TABLE = "Companies"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "STRING"),
    bigquery.SchemaField("Modified_Date", "STRING"), 
    bigquery.SchemaField("_id", "STRING"),       
    bigquery.SchemaField("active", "STRING"),    
    bigquery.SchemaField("address", "STRING"),
    bigquery.SchemaField("CancelledStatus", "STRING"),
    bigquery.SchemaField("CompanyID", "STRING"),  
    bigquery.SchemaField("Consignee", "STRING"), 
    bigquery.SchemaField("ContactEmail", "STRING"), 
    bigquery.SchemaField("ContactPhone", "STRING"), 
    bigquery.SchemaField("Cost", "STRING"), 
    bigquery.SchemaField("Currency", "STRING"), 
    bigquery.SchemaField("CustomerProjectReference", "STRING"), 
    bigquery.SchemaField("DriverReferenceType", "STRING"),
    bigquery.SchemaField("InitialStatus", "STRING"),
    bigquery.SchemaField("InvoiceTimestamp", "STRING"),
    bigquery.SchemaField("MainReference", "STRING"),
    bigquery.SchemaField("Name", "STRING"),
    bigquery.SchemaField("PublicVisibilityType", "STRING"), 
    bigquery.SchemaField("QuoteReplyReference", "STRING"),
    bigquery.SchemaField("QuoteTimestamp", "STRING"),
    bigquery.SchemaField("ReferencePrefix", "STRING"),
    bigquery.SchemaField("Revenue", "STRING"),
    bigquery.SchemaField("SecondReference", "STRING"),
    bigquery.SchemaField("Shipper", "STRING")

]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)



#Currencies 

TABLE = "Currencies"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Code", "STRING"),
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Enterprise", "STRING"), 
    bigquery.SchemaField("Modified_Date", "DATETIME"),       
    bigquery.SchemaField("Name", "STRING"),    
    bigquery.SchemaField("_id", "STRING")    
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


# Name,Projects,_id,active

TABLE = "Customers"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Currency", "STRING"), 
    bigquery.SchemaField("Enterprise", "STRING"),     
    bigquery.SchemaField("Modified_Date", "DATETIME"), 
    bigquery.SchemaField("Name", "STRING"),   
    bigquery.SchemaField("Projects", "STRING"),  
    bigquery.SchemaField("_id", "STRING"),
    bigquery.SchemaField("active", "STRING"),
    bigquery.SchemaField("Email", "STRING")     
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

#ExchangeRates

TABLE = "ExchangeRates"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("EffectiveDateEnd", "STRING"), 
    bigquery.SchemaField("EffectiveDateStart", "STRING"),       
    bigquery.SchemaField("Enterprise", "STRING"),    
    bigquery.SchemaField("Modified_Date", "DATETIME"), 
    bigquery.SchemaField("Name", "STRING"),   
    bigquery.SchemaField("Rate", "STRING"),  
    bigquery.SchemaField("_id", "STRING")
  
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)



#Files  #"Cost","Forms",  "References","Revenue","Timestamps",

TABLE = "Files"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("AssignedUser", "STRING"),
    bigquery.SchemaField("Created_By", "STRING"), 
    bigquery.SchemaField("Created_Date", "DATETIME"),       
    bigquery.SchemaField("Customer", "STRING"),    
    bigquery.SchemaField("Enterprise", "STRING"),   
    bigquery.SchemaField("ExchangeDate", "STRING"),  
    bigquery.SchemaField("FileStatus", "STRING"),  
    bigquery.SchemaField("FixExchangeDate", "STRING"),  
    bigquery.SchemaField("InternalRef", "STRING"),
    bigquery.SchemaField("Invoiced", "INTEGER"),
    bigquery.SchemaField("Modified_Date", "STRING"),
    bigquery.SchemaField("ReferenceNumber", "STRING"),
    bigquery.SchemaField("ShipDate", "STRING"),
    bigquery.SchemaField("Type", "STRING"),
    bigquery.SchemaField("_id", "STRING")
    
  
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#FileStatuses

TABLE = "FileStatuses"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Enterprise", "STRING"), 
    bigquery.SchemaField("Modified_Date", "DATETIME"),       
    bigquery.SchemaField("Name", "STRING"),    
    bigquery.SchemaField("_id", "STRING"), 
    bigquery.SchemaField("active", "STRING") 
  
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


# FileTypes
TABLE = "FileTypes"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Enterprise", "STRING"), 
    bigquery.SchemaField("Modified_Date", "DATETIME"),       
    bigquery.SchemaField("Name", "STRING"),    
    bigquery.SchemaField("_id", "STRING"),
    bigquery.SchemaField("active", "STRING")
  
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#Financials


TABLE = "Financials"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Charge", "STRING"),
    bigquery.SchemaField("ChargeType", "STRING"),
    bigquery.SchemaField("Created_By", "STRING"), 
    bigquery.SchemaField("Created_Date", "DATETIME"),       
    bigquery.SchemaField("Currency", "STRING"),    
    bigquery.SchemaField("Description", "STRING"),
    bigquery.SchemaField("ExchangeRate", "STRING"), 
    bigquery.SchemaField("Invoiced", "STRING"),
    bigquery.SchemaField("Modified_Date", "DATETIME"),
    bigquery.SchemaField("Normalized", "STRING"),
    bigquery.SchemaField("Owner", "STRING"),
    bigquery.SchemaField("_id", "STRING")
  
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#Forms

TABLE = "Forms"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("FormName", "STRING"), 
    bigquery.SchemaField("FormTemplate", "STRING"), 
    bigquery.SchemaField("Modified_Date", "DATETIME"), 
    bigquery.SchemaField("Owner", "STRING"),   
    bigquery.SchemaField("Visibility", "STRING"),
    bigquery.SchemaField("_id", "STRING")
  
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)



#FormTemplate


TABLE = "FormTemplate"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Enterprise", "STRING"), 
    bigquery.SchemaField("Modified_Date", "DATETIME"),  
    bigquery.SchemaField("DefaultVisibility", "STRING"),
    bigquery.SchemaField("Name", "STRING"),
    bigquery.SchemaField("_id", "STRING") 
  
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#FormValue


TABLE = "FormValue"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("DateValue", "STRING"), 
    bigquery.SchemaField("Modified_Date", "DATETIME"),  
    bigquery.SchemaField("FormValueType", "STRING"),
    bigquery.SchemaField("Owner", "STRING"),
    bigquery.SchemaField("TextValue", "STRING"),
    bigquery.SchemaField("_id", "STRING") 
  
]


table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)



# FormValueTypes

TABLE = "FormValueTypes"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Enterprise", "STRING"), 
    bigquery.SchemaField("FormValueType", "STRING"),       
    bigquery.SchemaField("Modified_Date", "DATETIME"),    
    bigquery.SchemaField("Options", "STRING"),
    bigquery.SchemaField("_id", "STRING"), 
    bigquery.SchemaField("active", "INTEGER") 
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#References

TABLE = "References"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "TIMESTAMP"),
    bigquery.SchemaField("Modified_Date", "TIMESTAMP"), 
    bigquery.SchemaField("Owner", "STRING"),       
    bigquery.SchemaField("Type", "STRING"),    
    bigquery.SchemaField("Value", "STRING"),
    bigquery.SchemaField("Visibility", "STRING"), 
    bigquery.SchemaField("_id", "STRING") 
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#Created By,Created Date,DefaultVisibility,Enterprise,Modified Date,Name,Options,_id,active
#ReferenceTypes


TABLE = "ReferenceTypes"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("DefaultVisibility", "STRING"), 
    bigquery.SchemaField("Enterprise", "STRING"),       
    bigquery.SchemaField("Modified_Date", "DATETIME"),    
    bigquery.SchemaField("Name", "STRING"),
    bigquery.SchemaField("Options", "STRING"), 
    bigquery.SchemaField("_id", "STRING"),
    bigquery.SchemaField("active", "STRING") 
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


TABLE = "Roles"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Modified_Date", "DATETIME"), 
    bigquery.SchemaField("_id", "STRING"),       
    bigquery.SchemaField("Name", "STRING")   
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#Timestamps


TABLE = "Timestamps"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Carrier", "STRING"),
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Image", "STRING"), 
    bigquery.SchemaField("Location", "STRING"),       
    bigquery.SchemaField("Modified_Date", "DATETIME"),   
    bigquery.SchemaField("Owner", "STRING"),   
    bigquery.SchemaField("Type", "STRING"),   
    bigquery.SchemaField("Value", "STRING"),  
    bigquery.SchemaField("Visibility", "STRING"),  
    bigquery.SchemaField("_id", "STRING") 
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#TimestampTypes

TABLE = "TimestampTypes"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("DefaultVisibility", "STRING"),
    bigquery.SchemaField("Enterprise", "STRING"), 
    bigquery.SchemaField("FileStatus", "STRING"),       
    bigquery.SchemaField("Modified_Date", "DATETIME"),   
    bigquery.SchemaField("Name", "STRING"),   
    bigquery.SchemaField("_id", "STRING"),   
    bigquery.SchemaField("active", "STRING") 

]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

#User

TABLE = "User"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Customer", "STRING"),      
    bigquery.SchemaField("Enterprise", "STRING"),   
    bigquery.SchemaField("Modified_Date", "DATETIME"),  
    bigquery.SchemaField("Name", "STRING"),  
    bigquery.SchemaField("Role", "STRING"), 
    bigquery.SchemaField("_id", "STRING"),
    bigquery.SchemaField("active", "STRING"),
    bigquery.SchemaField("authentication", "STRING"),
    bigquery.SchemaField("lang", "STRING"),
    bigquery.SchemaField("user_signed_up", "STRING")   


]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#VisibilityTypes


TABLE = "VisibilityTypes"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("Enterprise", "STRING"),
    bigquery.SchemaField("Modified_Date", "DATETIME"), 
    bigquery.SchemaField("Name", "STRING"),       
    bigquery.SchemaField("_id", "STRING")   
 
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

#Deletion

TABLE = "Deletion"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Created_By", "STRING"),
    bigquery.SchemaField("Created_Date", "DATETIME"),
    bigquery.SchemaField("ID", "STRING"),
    bigquery.SchemaField("Modified_Date", "DATETIME"), 
    bigquery.SchemaField("Object", "STRING"),       
    bigquery.SchemaField("_id", "STRING")   
 
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)



# CREATING REFERENCE TABLES
#Cost: List of Financials  --) Rel_Files_Cost


TABLE = "Rel_Files_Cost"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Cost_id", "STRING"),
    bigquery.SchemaField("Files_id", "STRING")    
 
]
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

#Forms: List of Forms --) Rel_Files_Forms

TABLE = "Rel_Files_Forms"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Form_id", "STRING"),
    bigquery.SchemaField("Files_id", "STRING")    
 
]
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

#References: List of References  --) Rel_Files_References

TABLE = "Rel_Files_References"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("References_id", "STRING"),
    bigquery.SchemaField("Files_id", "STRING")    
 
]
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

#Revenue: List of Financials --) Rel_Files_Revenues

TABLE = "Rel_Files_Revenue"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Revenue_id", "STRING"),
    bigquery.SchemaField("Files_id", "STRING")    
 
]
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

#Timestamps: List of Timestamps --) Rel_Files_Timestamps
TABLE = "Rel_Files_Timestamps"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Timestamps_id", "STRING"),
    bigquery.SchemaField("Files_id", "STRING")    
 
]
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)



#SubForms: List of Forms --) stored in Rel_Forms_Forms

TABLE = "Rel_Forms_Forms"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("SubForms_id", "STRING"),
    bigquery.SchemaField("Forms_id", "STRING")    
 
]
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#Values: List of FormValues --) stored in Rel_Forms_FormValues

TABLE = "Rel_Forms_FormValues"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("FormValues_id", "STRING"),
    bigquery.SchemaField("Forms_id", "STRING")    
 
]
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)




#Customer,OriginLat,OriginLng,OriginAddress,DestinationLat,DestinationLng,DestinationAddress

TABLE = "files_location"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("Customer", "STRING"),
    bigquery.SchemaField("OriginLat", "STRING"),   
    bigquery.SchemaField("OriginLng", "STRING"), 
    bigquery.SchemaField("OriginAddress", "STRING"), 
    bigquery.SchemaField("DestinationLat", "STRING"), 
    bigquery.SchemaField("DestinationLng", "STRING"), 
    bigquery.SchemaField("DestinationAddress", "STRING")
 
]
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)


#_id,LocationLat,LocationLng,LocationAddress

TABLE = "timestamp_location"
table_id = "{}.{}.{}".format(PROJECT,DATASET,TABLE)
QUERY = (
    'DROP TABLE IF EXISTS {}'.format(table_id))
query_job = client.query(QUERY)
schema = [
    bigquery.SchemaField("_id", "STRING"),
    bigquery.SchemaField("LocationLat", "STRING"),   
    bigquery.SchemaField("LocationLng", "STRING"), 
    bigquery.SchemaField("LocationAddress", "STRING")
 
]
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

