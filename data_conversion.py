import pandas as pd

# Load the CSV file correctly
data = pd.read_csv(r"C:\Users\DELL\Desktop\Diya\Sem 8\Python\Recipe\recipe_data.csv")

# Print available columns
print(data.columns)

# Use the correct column names
data = data[['Title', 'Ingredients', 'Instructions']]

data.dropna(inplace=True)
# Save the filtered data to a new CSV if needed
data.to_csv(r"C:\Users\DELL\Desktop\Diya\Sem 8\Python\Recipe\archive\cleaned_data.csv", index=False)

print("Data successfully filtered and saved!")
