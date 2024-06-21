import os
import pandas as pd
import csv

# Define the directory
directory = "data"

# Initialize an empty list to store parsed filenames
data = []

# Iterate over files in the directory
for filename in os.listdir(directory):
    # Replace "_colon_" with ":"
    modified_filename = filename.replace("_colon_", ":")
    modified_filename = modified_filename.replace("_slash_", "/")

    # Use csv.reader to parse the modified filename
    parsed_data = next(csv.reader([modified_filename], skipinitialspace=True))

    # Append the parsed data to the list
    data.append(parsed_data)

# Define the column names
column_names = [
    "Pandas ID",
    "Index",
    "Organization Id",
    "Name",
    "Website",
    "Country",
    "Description",
    "Founded",
    "Industry",
    "Number of employees",
]

# Determine the maximum number of columns
max_columns = len(column_names)

# Pad rows with empty strings if they have fewer columns than the maximum
data = [row + [""] * (max_columns - len(row)) for row in data]

# Create a DataFrame with the specified column names
df = pd.DataFrame(data, columns=column_names)

# Convert the 'Index' column to numeric type for proper sorting
df["Pandas ID"] = pd.to_numeric(df["Pandas ID"], errors="coerce")

# Order by the 'Index' column in ascending order
df = df.sort_values(by="Pandas ID").reset_index(drop=True)

# Print the DataFrame
print(df.head())

# Optionally, save the DataFrame to a CSV file
df.to_csv("customer_copy.csv", index=False)
