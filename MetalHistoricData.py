# We just want to check if there are some correlations among different metals. 
# We are comparing commodity metals (e.g. Aluminium) against other metals which are usually considered an investing shelter during economical crisis (e.g. Gold). 
# In between, other metals like Tin, Copper or Silver to check any rising hypotesis from the analysis.
# Library imports

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

import pandas as pd
from pandas_profiling import ProfileReport

import datetime as dt

########################################################################
## 
## Function definitions
##
########################################################################

def metals_plot(df, met_list):
    """
    Plots a list of metal price evolutions.

    Args:
        df (dataframe): Dataframe with date and prices of many metals
        met_list (list of str): list of metals
    """
    # Figure sizing    
    fig, ax = plt.subplots(figsize=(15, 12))
    
    # Setting x-axis for dates
    # x-axis values generation from dates
    x = mdates.date2num(df['Month'])

    # Select format %y (two digits for year and locate them) for major x axis
    formatter = mdates.DateFormatter('%y')
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.YearLocator()
    ax.xaxis.set_major_locator(locator)

    # Set a tick for each month
    locator2 = mdates.MonthLocator()
    ax.xaxis.set_minor_locator(locator2)

    # Plotting the prices
    for metal in met_list:
        ax.plot(x, df[metal], linewidth=1.0, label=metal)
        
    # Setting legends, titles, etc.    
    plt.title('Normalized Metal Prices')
    plt.xlabel('Month')
    plt.ylabel('Price/Price(91-Feb)')
    plt.grid(True)
    plt.legend()
    
    plt.show()
    return
 
# 1. Data reading and some exploratory data analysis
file = '/metals.csv'

# Read the csv file and parse str to date
df = pd.read_csv(file, sep=';', decimal=',')
df['Month'] = [dt.datetime.strptime(aux, '%d/%m/%y') for aux in df['Month']]

# Generate data profile
profile = ProfileReport(df, title='Pandas Metals Report')
profile.to_widgets()

# 2. Data Massage. Let's make some data massage! To compare the different metals evolution, we are going to normalize each metal price by each Feb-1991 corresponding price.
# Price normalizing dividing Metal prices by Metal price(Feb 1991) 
metals = list(df.columns)[1:]
for metal in metals:
    df[metal] = df[metal]/df.loc[0, metal] # Divides by first price
    
metals_plot(df, metals)

# Now we can plot pairwise evolutions of metals
