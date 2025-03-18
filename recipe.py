import pandas as pd

# Load the training CSV file
train_file_path = r"C:\Users\DELL\Desktop\Diya\Sem 8\Python\Recipe\train_set.csv"  # Update with your training file path
train_df = pd.read_csv(train_file_path)

# Load the test CSV file
test_file_path = r"C:\Users\DELL\Desktop\Diya\Sem 8\Python\Recipe\test_set.csv"  # Update with your test file path
test_df = pd.read_csv(test_file_path)

# Display the first few rows of the training DataFrame
print("Training Data:")
print(train_df.head())

# Display the first few rows of the test DataFrame
print("\nTest Data:")
print(test_df.head())

# Optionally, you can save the DataFrames to new CSV files if needed
train_output_path = r"C:\Users\DELL\Desktop\Diya\Sem 8\Python\Recipe\output_train.csv"
test_output_path = r"C:\Users\DELL\Desktop\Diya\Sem 8\Python\Recipe\output_test.csv"

train_df.to_csv(train_output_path, index=False)
test_df.to_csv(test_output_path, index=False)

print(f"\nTraining data saved as {train_output_path}")
print(f"Test data saved as {test_output_path}")