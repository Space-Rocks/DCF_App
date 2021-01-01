# Import libraries and packages
import datetime
import pymongo
from pymongo import MongoClient

# Assign client, database, and collection
if __name__ == "db":
        client = MongoClient() #Client
        db = client.CashFlowAppDB #Database
        Stocks = db.Stocks #Collection

# Create document
def create_document(ticker,years,free_cash_flow):
        Stock = {"ticker": ticker, 
                "year": years, 
                "free_cash_flow": free_cash_flow}
        return(Stock)

# Insert one document
def insert_one(stock):
        stock_id = Stocks.insert_one(stock).inserted_id
        return(stock_id)

# Update stock data
def update_stock(ticker,year,free_cash_flow):
        stock = {"ticker": ticker}
        updates = {"$set": {"year": year, "free_cash_flow": free_cash_flow}}
        Stocks.update_one(stock, updates)

# Append new stock data
def append_stock(ticker,year,free_cash_flow):
        stock = {"ticker": ticker}
        pushes = {"$push": {"year": year, "free_cash_flow": free_cash_flow}}
        Stocks.update_one(stock, pushes)

# Retrieve one document
def retrieve_one(ticker):
        data = Stocks.find_one({'ticker': ticker})
        return(data)

# Retrieve all documents
def retrieve_all(ticker):
        data = Stocks.find({'ticker': ticker})
        output = []
        for row in data:
                output.append(row)
        return(output)








