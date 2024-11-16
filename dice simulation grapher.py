import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

# Read the data from the Excel file
df = pd.read_excel('dicesimulation.xlsx', sheet_name='Simulation Data')

# Define the exponential function for fitting
def exponential_func(x, a, b):
    return a * np.exp(b * x)

# Fit the exponential function to the data
popt, pcov = curve_fit(exponential_func, df['Time Elapsed'], df['Nuclei Remaining'])

# Extract the parameters a and b
a, b = popt

# Calculate the R² value
y_pred = exponential_func(df['Time Elapsed'], *popt)
residuals = df['Nuclei Remaining'] - y_pred
ss_res = np.sum(residuals**2)
ss_tot = np.sum((df['Nuclei Remaining'] - np.mean(df['Nuclei Remaining']))**2)
r_squared = 1 - (ss_res / ss_tot)

# Generate x values for the smoother trendline
x_vals = np.linspace(0, 50, 1000)  # Extend to 50 as per the x-axis limit

# Plot the data
ax = df.plot(kind='scatter', x='Time Elapsed', y='Nuclei Remaining', color='blue')  # No label for scatter

# Plot the exponential trendline in red
ax.plot(x_vals, exponential_func(x_vals, *popt), color='red')  # No label for trendline

# Enable both major and minor gridlines on the same plot
ax.grid(True, which='both')  # Enable both major and minor gridlines
ax.minorticks_on()  # Enable minor ticks

# Display the R² value on the plot
r_squared_text = f"R² = {r_squared:.4f}"
ax.text(0.1, 0.9, r_squared_text, transform=ax.transAxes, color='red', fontsize=12, verticalalignment='top')

# Set x-axis bounds from 0 to 50
ax.set_xlim(0, 30)

# Add title and labels
ax.set_title('Rate of decay of a radioactive substance over time')
ax.set_ylabel('Number of undecayed nuclei remaining')
ax.set_xlabel('Time elapsed in minutes')

# Show the plot (without the legend)
plt.show()
