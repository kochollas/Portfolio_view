Attachments = ["Created_By","Created_Date","Modified_Date","Name","Owner","Type","Value","Visibility","_id"]

AttachmentTypes = [
    "Created_By", 
    "Created_Date", 
    "DefaultVisibility", 
    "Enterprise", 
    "Modified_Date", 
    "Name", 
    "_id", 
    "active"
]


ChargeTypes = [
    "Created_By",
    "Created_Date", 
    "Enterprise",
    "Modified_Date",     
    "Name",    
    "_id"
]


Currencies = [
    "Code",
    "Created_By",
    "Created_Date",
    "Enterprise", 
    "Modified_Date",       
    "Name",    
    "_id"
]

Customers = [
    "Created_By", 
    "Created_Date",
    "Currency",  
    "Enterprise",      
    "Modified_Date", 
    "Name",    
    "Projects",   
    "_id", 
    "active", 
    "Email"  
]

FileStatuses = [
    "Created_By",
    "Created_Date", 
    "Enterprise", 
    "Modified_Date",        
    "Name",    
    "_id", 
    "active"
]

FileTypes = [
   "Created_By",
   "Created_Date",
   "Enterprise", 
   "Modified_Date",       
   "Name",    
   "_id",
   "active"
]

Financials = [
    "Charge", 
    "ChargeType", 
    "Created_By",  
    "Created_Date",       
    "Currency",     
    "Description", 
    "ExchangeRate",  
    "Invoiced", 
    "Modified_Date",
    "Normalized", 
    "Owner", 
    "_id"
]

ReferenceTypes =[
    "Created_By", 
    "Created_Date", 
    "DefaultVisibility",  
    "Enterprise",        
    "Modified_Date",     
    "Name", 
    "Options",  
    "_id", 
    "active"
]


References=["Created_By", 
    "Created_Date", 
    "Modified_Date",  
    "Owner",        
    "Type",     
    "Value", 
    "Visibility",  
    "_id"] 

AuditLogEntries=["Created_By", 
"Created_Date", 
"Modified_Date", 
"Object", 
"Owner", 
"Text", 
"_id"]

Roles =[
"Created_By", 
   "Created_Date", 
   "Modified_Date",  
   "_id",        
   "Name"] 

Timestamps = [
"Carrier", 
"Created_By", 
"Created_Date", 
"Image",  
"Location",        
"Modified_Date",    
"Owner",    
"Type",    
"Value",   
"Visibility",   
"_id"
]


TimestampTypes = [
"Created_By",
"Created_Date", 
"DefaultVisibility",
"Enterprise", 
"FileStatus",       
"Modified_Date",    
"Name",   
"_id",   
"active"
]

User =[
"Created_Date",
"Customer",       
"Enterprise",    
"Modified_Date",  
"Name",   
"Role",  
"_id", 
"active", 
"authentication", 
"lang", 
"user_signed_up"
]


Comments = [
"Created_By", 
"Created_Date",
"Modified_Date", 
"Owner",        
"Value",     
"Visibility", 
"_id"
]


Companies = [
"Created_By", 
"Created_Date", 
"Modified_Date", 
"_id",        
"active",     
"address", 
"CancelledStatus", 
"CompanyID",   
"Consignee",  
"ContactEmail",  
"ContactPhone",  
"Cost",  
"Currency",  
"CustomerProjectReference",  
"DriverReferenceType", 
"InitialStatus", 
"InvoiceTimestamp", 
"MainReference", 
"Name", 
"PublicVisibilityType",  
"QuoteReplyReference", 
"QuoteTimestamp", 
"ReferencePrefix", 
"Revenue", 
"SecondReference", 
"Shipper"
]


ExchangeRates = [

"Created_By", 
"Created_Date",
"EffectiveDateEnd", 
"EffectiveDateStart",       
"Enterprise",     
"Modified_Date", 
"Name",    
"Rate",   
"_id"
]

Files = [
"AssignedUser",
"Created_By", 
"Created_Date",      
"Customer",    
"Enterprise",   
"ExchangeDate", 
"FileStatus",  
"FixExchangeDate",  
"InternalRef",
"Invoiced",
"Modified_Date",
"ReferenceNumber",
"ShipDate",
"Type",
"_id"
]

#"Cost","Forms",  "References","Revenue","Timestamps",#"Destination", #"Origin",



Forms = [

 "Created_By",
 "Created_Date",
 "FormName", 
 "FormTemplate", 
 "Modified_Date",  
 "Owner",   
 "Visibility",
 "_id"
]
# "SubForms",   "Values", 

FormTemplate = [

"Created_By", 
"Created_Date",
"Enterprise",  
"Modified_Date",  
"DefaultVisibility", 
"Name", 
"_id"
]


FormValue =[
    "Created_By", 
    "Created_Date", 
    "DateValue",  
    "Modified_Date",   
    "FormValueType", 
    "Owner", 
    "TextValue", 
    "_id"
]

FormValueTypes =[
"Created_By", 
"Created_Date",
"Enterprise",  
"FormValueType",        
"Modified_Date",    
"Options", 
"_id",  
"active"
]

VisibilityTypes = [
    "Created_By",
    "Created_Date",
    "Enterprise",
    "Modified_Date", 
    "Name",       
    "_id"
]

Deletion = [
    "Created_By",
    "Created_Date", 
    "ID",
    "Modified_Date",  
    "Object",       
    "_id"  
]