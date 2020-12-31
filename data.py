from yahoofinancials import YahooFinancials
import numpy as np

def get_cash_flow_data(ticker):

    """
    Fetch financial statement data for ticker and return lists of free cash flow and years.

    Keyword arguments:
    ticker -- string of ticker symbol
    """

    data = YahooFinancials(ticker).get_financial_stmts('annual', 'cash')
    years = []
    free_cash_flow = []

    for item in data['cashflowStatementHistory'][ticker]:
        years.append(int(list(item.keys())[0][0:4]))
        free_cash_flow.append(item[list(item.keys())[0]]['totalCashFromOperatingActivities'] + item[list(item.keys())[0]]['capitalExpenditures'])

    return(years,free_cash_flow)

def project_free_cash_flow(years,free_cash_flow,years_forward,method):

    """
    Project free cash flow data forward by given number of years following prescribed method.

    Keyword arguments:
    year -- input list of years for free cash flow data to project
    free_cash_flow -- list of free cash flow data on which to base projection
    years_forward -- the number of years to forward project free cash flow
    method -- the method by which to fit the input free cash flow data and project forward (polynomial degree)
    """

    # Create list of years over which to project free cash flow
    projected_years = np.linspace(max(years),max(years)+years_forward,years_forward*10)
    
    # Generate fit to input data and calculate projected free cash flow
    if type(method) == int:
        fit = np.polyfit(years,free_cash_flow,method)
        fit_function = np.poly1d(fit)
        fit_years = np.linspace(min(years),max(years),(max(years)-min(years))*10)
        fit_data = fit_function(fit_years)
        projected_free_cash_flow = fit_function(projected_years)
    
    return(fit_years,fit_data,projected_years,projected_free_cash_flow)
