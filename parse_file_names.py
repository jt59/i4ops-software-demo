import os
import pandas as pd

# Define the directory
directory = "data"

# Initialize an empty list to store parsed filenames
data = []

# Iterate over files in the directory
for filename in os.listdir(directory):
    # Replace "_colon_" with ":"
    modified_filename = filename.replace("_colon_", ":")
    modified_filename = modified_filename.replace("_slash_", "/")

    # Parse the filename on commas
    parsed_data = modified_filename.split(",")

    # Append the parsed data to the list
    data.append(parsed_data)

# Determine the maximum number of columns
max_columns = max(len(row) for row in data)

# Pad rows with empty strings if they have fewer columns than the maximum
data = [row + [""] * (max_columns - len(row)) for row in data]

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df.head())

# Optionally, save the DataFrame to a CSV file
df.to_csv("customer_copy.csv", index=False)
