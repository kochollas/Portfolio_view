## ETL services

1. GA_to_RDBMS

This service is written in python and used to connect to a google analytics account using GA API for pulling data which is later transformed within the script and sent to a reporting database or data warehouse, This data is then consumed using Metabase BI. It can be automated to run daily using CRONTAB or AIRFLOW.

2. Location_service

This is a python data processing service written for an Australian client that given two data points is able to pull address, latitude and longitude for the provided payload. The data is later joined and the end result is stored in sqlite database. The service is running in batches for pulling the data using AWS EC2. There is a plan to move this to AWS Lambda as well as S3.

3. Loan_Processor service

This is an R and Python service. The server of this is written in R to pull specific data points from mobile money(MPESA) monthly transaction statements and generate a test data which will be sent back to a python client by calling the R end-point. The python client is used to send the pdf and also perform machine learning prediction of amount to loan based on the underlying trained algorithm.
Check here for complete replication : https://github.com/kochollas/Portfolio_view/tree/master/Model_deployment/loan_engine

4. Processing raw text using REGEX and NLP

This is a python script wrote for a client to help in processing raw text and generate the output csv with the right columns using Regular expressions and NLP. From the input raw text i was able to generate the final csv with the following columsn (text,bid_amount,type,pet_name,quality) Check it out.

5. Stock_api_service

This is a python service written to pull US stock data using polygon and process the same. It involved pullling historical data from 2007 to 2022 which made it generate millions of stock daily hourly and minute data. It also had a bit of threading to reduce processing time from 10min to a few seconds for a single stock detail in a year. It was managed in EC2 with 8 cores for faster processing. Error handling and Logging were implemented



