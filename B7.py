import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv('batsmen.csv')

# Set batsman names as index
data.set_index('Batsman', inplace=True)

# Plot bar graph
data.plot(kind='bar', figsize=(10,6))

# Labels and title
plt.title('Runs scored by Batsmen (2017-2020)')
plt.xlabel('Batsmen')
plt.ylabel('Runs')

# Show legend
plt.legend(title='Year')

# Display graph
plt.tight_layout()
plt.show()