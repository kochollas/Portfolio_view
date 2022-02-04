## Google Analytics website users data to Relational database service
A service to pull GA metrics to a relational database

### Prerequisites
Python and RDBMS set-ups as well as google analytics account with programmatic access

### Project Structure
Resources

Libraries.py

● Loads necessary third party libraries and user defined functions. Changing ​ date_range()
within this file as ​ date_range(‘weekly’) ​ will produce weekly data points. It is daily by
default.

Credentials.py

● Setting up google analytics reporting API authentication is done within this file. If success
it will display “ACCESS ACQUIRED”
GAminer.py

● Imports both libraries and credentials files

● This is where the heavy lifting occurs, that is all data points needed from GA are
configured and request sent using​ get_report f ​ unction.

● If you need to add any data points this is where you will create a new ​ get_report () ​ and
configure it for either metrics, dimensions or segments.

● The functions will return json objects which will be passed for further processing
downstream by data_aggregator function.

● “ALL REQUIRED DATA PULLED SUCCESSFULLY” is displayed




Schema.py

● Run this file in your chosen database to generate empty tables that will hold the data
sets being pulled by the script daily or weekly.

★ N/B : Ensure to create the empty tables before running the main.py file.

Main.py


This section will need database access credentials set-up done on schema.py. Adjust
accordingly
It will check if a table is empty then add data to it. If it has data it will append and adjust
the id which is the primary key. The date variable will help to distinguish the data points
“DATABASE UPDATE SUCCESS” will be displayed to mark the end.


To run the service
```
python main.py
```
