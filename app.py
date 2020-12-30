# Import app modules
from data import get_cash_flow_data
import matplotlib.pyplot as plt
# from db import

# Placeholders
ticker = 'AAPL'

# Execute app
if __name__ == "__main__":
    years,fcf = get_cash_flow_data(ticker)

    plt.figure(1)
    plt.plot(years, fcf, 'ok')
    plt.title(ticker)
    plt.xlabel('Year')
    plt.ylabel('Free Cash Flow ($)')
    plt.show()



