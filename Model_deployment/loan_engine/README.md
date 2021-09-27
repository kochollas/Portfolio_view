## ML-Model-Flask-App
How to deploy a simple ML model to prod using Flask API

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :
1. model.py - This contains code fot our Machine Learning model to predict amount loanable to a client
2. app.py - This contains Flask APIs that MPESA PDF statement details through GUI or API calls, computes the precited value based on our model and returns it.

3. templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.

### Running the project

1. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

You should be able to view the homepage as below :
![alt text](https://github.com/[kochollas]/[Portfolio_view/Model_deployment/loan_engine/]/blob/[main]/loan_prediction_app.jpg?raw=true)



