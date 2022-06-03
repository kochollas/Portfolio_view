# Analysis requested 1.mongo db -- jupyter nbconvert --to html --template hidecode YourNotebook.ipynb
'''
{%- extends 'full.tpl' -%}

{% block input_group %}
    {%- if cell.metadata.get('nbconvert', {}).get('show_code', False) -%}
        ((( super() )))
    {%- endif -%}
{% endblock input_group %}

'''
from pymongo import MongoClient
import urllib.parse 

username = urllib.parse.quote_plus('xx')
password = urllib.parse.quote_plus("xxxx")
url = "mongodb://{}:{}@xxxx".format(username, password)
print(url)
client = MongoClient(url)
mydb = client["appsdata"]
print(mydb)

docs = mydb.__doc__
print(docs)

print("COLLECTIONS:")
for col in mydb.list_collection_names():
    print(col)

    
import pandas as pd
#leadmvp
my_query = {}
leadmvp_table = mydb["leadmvp"]
lmvp_dict = list(leadmvp_table.find())
lmvp_df = pd.DataFrame(lmvp_dict)
len(lmvp_df)

# quote_visits
quotes_table = mydb["quote_visits"]
quotes_dict = list(quotes_table.find())
quotes_df = pd.DataFrame(quotes_dict)
len(quotes_df)

#Venue finder
venue_table = mydb["venue_finder"]
venue_dict = list(venue_table.find())
venue_df = pd.DataFrame(venue_dict)
len(venue_df)

#first quote visit
fqv_table = mydb["first_quote_visit"]
fqv_dict = list(fqv_table.find())
fqv_df = pd.DataFrame(fqv_dict)
len(fqv_df)
