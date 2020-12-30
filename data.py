from yahoofinancials import YahooFinancials

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



