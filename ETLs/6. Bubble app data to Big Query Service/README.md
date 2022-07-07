# Bubble to BigQuery Python Service

## Overview

The module contains below components:
    a)Schemas : This is where we define the bigquery schema and also update the same, database_tables.py helps to mirror the bigquery schema to the codebase
    b) Utils : This section contains the utility code comprising of functions used through the codebase for api calls data processing etc.
    c) Data : We do write csv files here temporarily before compying to bq
    d) ops : This section is for various components like inserts, deletions or updates. The code can be extended easily from here
    e) The main directory containing data_etl and bigquery events. The first is for one of all updates and the latter is for periodic updates time to time
    f) auth and Logs folders for keeping logfiles and authentication files.Will not be viewable here but exists within production server.

## Installation
1. Create bigQuery resources (project, dataset, tables)
2. Copy the contents of the folder to prefered production or local enviroment.
3. Create enviroment variables within the codebase to hold:
    a) Big Query Project, Dataset, path to service key, path to Data folder.
    b) Set this on schemas.schema.py, utils.libraries.py and data_etl.py
4. Run the data_etl and monitor the logs as well as bigQuery tables

## Troubleshooting

1. Ensure all software dependencies are installed i.e check libraries file
2. Ensure you have permission to the data source and destination
3. Check the logs for any clues.