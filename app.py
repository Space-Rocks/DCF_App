# Import app modules
from flask import Flask, render_template
import data
import db
import matplotlib.pyplot as plt


# Create flask app and web route
app = Flask(__name__)
@app.route('/')

def index():
    return(render_template('index.html'))



# # Placeholders
# ticker = 'CVX'
# years_forward = 5
# method = 1

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

#     # Plot data for visualization
#     plt.figure(1)
#     plt.plot(years, free_cash_flow, 'ok', label='Historical')
#     plt.plot(fit_years, fit_data, '-k', label='Fit')
#     plt.plot(projected_years, projected_free_cash_flow, '-r', label='Projection')
#     plt.title(ticker)
#     plt.xlabel('Year')
#     plt.ylabel('Free Cash Flow ($)')
#     plt.legend()
#     plt.show()

# Execute app
if __name__ == "__main__":
    # main()
    app.run(debug=True)

# Placeholder for testing 
foo = 0
