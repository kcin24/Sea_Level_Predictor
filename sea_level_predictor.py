import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    scatter  = plt.scatter('Year','CSIRO Adjusted Sea Level', data = df)
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')


    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

# Generate new line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    x_new = np.arange(x.min(), 2051)

    y_new = slope * x_new + intercept

    fig, ax = plt.subplots()

    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    ax.set_xlabel('Year')
    ax.set_ylabel('CSIRO Adjusted Sea Level')


    ax.plot(x_new, y_new, color='red')

    print(f"The projected sea level rise in 2050 is: {y_new[-1]} units")

    plt.show()


    # Create second line of best fit

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']


    slope, intercept, r_value, p_value, std_err = linregress(x, y)


    x_new = np.arange(x.min(), 2051)

    
    y_new = slope * x_new + intercept


    df_2000 = df[df['Year'] >= 2000]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']

    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(x_2000, y_2000)
    x_new_2000 = np.arange(x_2000.min(), 2051)
    y_new_2000 = slope_2000 * x_new_2000 + intercept_2000


    fig, ax = plt.subplots()

        
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')


    ax.plot(x_new, y_new, color='red')


    ax.plot(x_new_2000, y_new_2000, color='green')

    print(f"The projected sea level rise in 2050 is: {y_new[-1]} units")
    print(f"The projected sea level rise in 2050 from 2000 onward is: {y_new_2000[-1]} units")

    plt.show()






    # Add labels and title
    ax.set_title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()