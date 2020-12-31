# Import app modules
from data import get_cash_flow_data, project_free_cash_flow
import matplotlib.pyplot as plt
# from db import

# Placeholders
ticker = 'CVX'

# Execute app
if __name__ == "__main__":
    years,free_cash_flow = get_cash_flow_data(ticker)
    fit_years,fit_data,projected_years,projected_free_cash_flow = project_free_cash_flow(years,free_cash_flow,5,2)

    plt.figure(1)
    plt.plot(years, free_cash_flow, 'ok', label='Historical')
    plt.plot(fit_years, fit_data, '-k', label='Fit')
    plt.plot(projected_years, projected_free_cash_flow, '-r', label='Projection')
    plt.title(ticker)
    plt.xlabel('Year')
    plt.ylabel('Free Cash Flow ($)')
    plt.legend()
    plt.show()



