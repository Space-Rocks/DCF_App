from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt

# ticker = 'AAPL'
ticker = 'GOOGL'

yahoo_financials = YahooFinancials(ticker)

test = yahoo_financials.get_financial_stmts('annual', 'cash')
test_years = []
test_fcf = []

for item in test['cashflowStatementHistory'][ticker]:
    test_years.append(int(list(item.keys())[0][0:4]))
    test_fcf.append(item[list(item.keys())[0]]['totalCashFromOperatingActivities'] + item[list(item.keys())[0]]['capitalExpenditures'])

plt.figure(1)
plt.plot(test_years,test_fcf,'ok')
plt.xlabel('Year')
plt.ylabel('Free Cash Flow ($)')
plt.title(ticker)
plt.show()
