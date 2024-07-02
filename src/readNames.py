import pandas as pd

# Read the CSV file
df = pd.read_csv('nomes.csv')

# Extract the 'first_name' column
first_names = df['first_name'].dropna().tolist()

# Print the list of names
print(first_names)