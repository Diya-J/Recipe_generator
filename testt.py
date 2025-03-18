import pandas as pd

# Load first 1000 rows to test
data = pd.read_csv(r"C:\Users\DELL\Desktop\Diya\Sem 8\Python\Recipe\archive\RecipeNLG_dataset.csv", nrows=1000)
print(data.head())
