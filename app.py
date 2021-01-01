# Import app modules
from flask import Flask, render_template, url_for, jsonify, request, redirect
from flask_pymongo import PyMongo
import data

# Define app and database configuration
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'CashFlowAppDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/CashFlowAppDB'
mongo = PyMongo(app)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        ticker = str(request.form['content'])
        add_stock(ticker)
        return(redirect('/'))
    else:
        return(render_template('index.html'))

# Define database CRUD operations
@app.route('/', methods=['POST'])
def add_stock(ticker):
  ticker = ticker
  years,free_cash_flow = data.get_cash_flow_data(ticker)
  Stocks = mongo.db.Stocks
  stock_id = Stocks.insert({'ticker': ticker, 'years': years, 'free_cash_flow': free_cash_flow})
  new_stock = Stocks.find_one({'_id': stock_id })
  output = {'ticker' : new_stock['ticker'], 'years' : new_stock['years'], 'free_cash_flow': new_stock['free_cash_flow']}
  return jsonify({'result' : output})

@app.route('/', methods=['GET'])
def get_one_stock(ticker):
  ticker = ticker
  Stocks = mongo.db.Stocks
  s = stocks.find_one({'ticker' : ticker})
  if s:
    output = {'ticker' : s['ticker'], 'years' : s['years'], 'free_cash_flow': s['free_cash_flow']}
  else:
    output = "No such ticker"
  return jsonify({'result' : output})

# Placeholders
ticker = 'AAPL'
years_forward = 5
method = 1

# Execute app
if __name__ == "__main__":

    years,free_cash_flow = data.get_cash_flow_data(ticker)
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






