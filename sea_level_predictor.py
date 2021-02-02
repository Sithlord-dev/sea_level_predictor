import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('files/epa-sea-level.csv', na_values = ['?'])


    # Create scatter plot
    fig, ax = plt.subplots(figsize=(13,8))
    df.plot.scatter(
      title = 'Scatter Plot sea level',
      x = 'Year',
      y = 'CSIRO Adjusted Sea Level',
      legend = True,
      ax=ax
    )


    # Create first line of best fit
    X = df['Year']
    Y = df['CSIRO Adjusted Sea Level']
    model = linregress(X, Y)

    (a, b) = (model.slope, model.intercept)
    X_1 = list(range(1880, 2050)) 
    Y_1 = [ a * x + b for x in X_1 ]
    
    plt.plot(X_1, Y_1, color='red', label='best fit line 1')

    # Create second line of best fit
    mask = (df['Year'] >= 2000)
    X_rec = df[mask]['Year']
    Y_rec = df[mask]['CSIRO Adjusted Sea Level']
    model_rec = linregress(X_rec, Y_rec)

    (a_rec, b_rec) = (model_rec.slope, model_rec.intercept)
    X_2 = list(range(2000, 2050)) 
    Y_2 = [ a_rec * x + b_rec for x in X_2]

    plt.plot(X_2, Y_2, color='green', label = 'best fit line 2')

    # Add labels and title
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()