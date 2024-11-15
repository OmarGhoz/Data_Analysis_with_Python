import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def create_sea_level_plot():
    # 1. Import data
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create a scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 3. Create the first line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)  # Extend years to 2050
    line_fit = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, line_fit, label='Best Fit Line (1880 - 2050)', color='red')

    # 4. Create a second line of best fit using data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    line_fit_recent = [slope_recent * year + intercept_recent for year in years_extended]
    plt.plot(years_extended, line_fit_recent, label='Best Fit Line (2000 - 2050)', color='green')

    # 5. Set titles and labels
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # 6. Add legend
    plt.legend()

    # 7. Save the plot and show it
    plt.savefig('sea_level_plot.png')
    plt.show()
