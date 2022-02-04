## ETL services

1. GA_to_RDBMS

This service is written in python and used to connect to a google analytics account using GA API for pulling data which is later transformed within the script and sent to a reporting database or data warehouse, This data is then consumed using Metabase BI. It can be automated to run daily using CRONTAB or AIRFLOW.

2. Location_service

This is a python data processing service written for an Australian client that given two data points is able to pull address, latitude and longitude for the provided payload. The data is later joined and the end result is stored in sqlite database. The service is running in batches for pulling the data using AWS EC2. There is a plan to move this to AWS Lambda as well as S3.

3. Loan_Processor service

This is an R and Python service. The server of this is written in R to pull specific data points from mobile money(MPESA) monthly transaction statements and generate a test data which will be sent back to a python client by calling the R end-point. The python client is used to send the pdf and also perform machine learning prediction of amount to loan based on the underlying trained algorithm.
Check here for complete replication : https://github.com/kochollas/Portfolio_view/tree/master/Model_deployment/loan_engine

