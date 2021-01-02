# Import app modules
from flask import Flask, render_template, url_for, request, redirect
import json
from flask_pymongo import PyMongo
import data

# Define app and database configuration
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'CashFlowAppDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/CashFlowAppDB'
mongo = PyMongo(app)

# Declare global variables
ticker = ""
years = []
free_cash_flow = []
test1 = []
test2 = []
test3 = []

# Define app 
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        global ticker, years, free_cash_flow, test1,test2,test3
        try:
          ticker = str(request.form['ticker'])
          years_forward = int(request.form['years_forward'])
        except:
          pass
        if get_one_stock(ticker) == None:
          add_stock(ticker)
          years,free_cash_flow = data.get_cash_flow_data(ticker)
        else:
          #years,free_cash_flow = data.get_cash_flow_data(ticker)
          test1,test2,test3 = get_one_stock(ticker)
        return(redirect('/'))
    else:
        return(render_template('index.html', ticker=test1, years=test2, free_cash_flow=test3))

# Define database CRUD operations
@app.route('/', methods=['POST'])
def add_stock(ticker):
  ticker = ticker
  years,free_cash_flow = data.get_cash_flow_data(ticker)
  Stocks = mongo.db.Stocks
  stock_id = Stocks.insert({'ticker': ticker, 'years': years, 'free_cash_flow': free_cash_flow})

@app.route('/', methods=['GET'])
def get_one_stock(ticker):
  ticker = ticker
  Stocks = mongo.db.Stocks
  s = Stocks.find_one({'ticker' : ticker})
  if s:
    return(s['ticker'],s['years'],s['free_cash_flow'])
  else:
    return(None)

# Execute app
if __name__ == "__main__":
    app.run(debug=True)

# Placeholder for testing 
foo = 0

















# # Define main app function
# def main():
#     """
#     Main app function
#     """

#     # If data not in databse fetch and insert
#     if db.retrieve_one(ticker) == None:

#         # Retrieve data from web using data module
#         years,free_cash_flow = data.get_cash_flow_data(ticker)

#         # Create document and insert into NoSQL database
#         document = db.create_document(ticker,years,free_cash_flow)
#         db.insert_one(document)

#     # Else retrieve from database
#     else:
        
#         # Retrieve data from NoSQL database
#         db_data = db.retrieve_all(ticker)
#         years = db_data[0]['years']
#         free_cash_flow = db_data[0]['free_cash_flow']
    
#     # Fit historical data with desired method and project forward given number of years
#     fit_years,fit_data,projected_years,projected_free_cash_flow = data.project_free_cash_flow(years,free_cash_flow,years_forward,method) 






