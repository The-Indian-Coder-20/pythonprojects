import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the data from the Excel file
df = pd.read_excel('dicesimulation.xlsx', sheet_name='Simulation Data')

# Fit a polynomial of degree 6 (higher order for better fit)
degree = 6
z = np.polyfit(df['Nuclei Remaining'], df['Time Elapsed'], degree)  # Degree 6 polynomial
p = np.poly1d(z)  # Create a polynomial function

# Calculate the R² value
# Calculate the residuals
y_pred = p(df['Nuclei Remaining'])
residuals = df['Time Elapsed'] - y_pred
ss_res = np.sum(residuals**2)
ss_tot = np.sum((df['Time Elapsed'] - np.mean(df['Time Elapsed']))**2)
r_squared = 1 - (ss_res / ss_tot)

# Generate x values for the smoother trendline (from 0 to 50)
x_vals = np.linspace(0, 30, 1000)

# Plot the data
ax = df.plot(kind='scatter', x='Time Elapsed', y='Nuclei Remaining', color='blue')  # No label for scatter

# Plot the smoother polynomial trendline in red
ax.plot(x_vals, p(x_vals), color='red')  # No label for trendline

# Enable both major and minor gridlines on the same plot
ax.grid(True, which='both')  # Enable both major and minor gridlines
ax.minorticks_on()  # Enable minor ticks

# Display the R² value on the plot
r_squared_text = f"R² = {r_squared:.4f}"
ax.text(0.1, 0.9, r_squared_text, transform=ax.transAxes, color='red', fontsize=12, verticalalignment='top')

# Set x-axis bounds from 0 to 50
ax.set_xlim(0, 50)

# Add title and labels
ax.set_title('Rate of decay of a radioactive substance over time')
ax.set_ylabel('Number of undecayed nuclei remaining')
ax.set_xlabel('Time elapsed in minutes')

# Show the plot (without the legend)
plt.show()
