import pandas as pd

# Read a CSV file
data = pd.read_csv('data.csv')

# Display basic statistics
print("Summary Statistics:")
print(data.describe())

# Plot a histogram
data['column_name'].hist()
plt.title('Histogram of Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
