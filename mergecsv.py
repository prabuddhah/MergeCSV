#!/usr/bin/env python3

#import the pandas library
import pandas as pd

# Define the filenames with full file paths
filenames = [
    r'C:PROJECTS\logfile01.csv',
    r'C:PROJECTS\logfile02.csv',
    r'C:PROJECTS\logfile03.csv',
    r'C:PROJECTS\logfile04.csv',
    r'C:PROJECTS\logfile05.csv',
    r'C:PROJECTS\logfile06.csv',
    r'C:PROJECTS\logfile07.csv',
]

# Create an empty list to store the DataFrames
print("Creating an empty list to store the DataFrames....")
dfs = []

# Read each CSV file into a DataFrame and append it to the list
print("Reading each CSV file and appending....")
for filename in filenames:
    df = pd.read_csv(filename)
    dfs.append(df)

# Merge the DataFrames into a single DataFrame
print("Merging the DataFrames....")
merged_df = pd.concat(dfs)

# Write the merged DataFrame to a new CSV file
print("Saving updated DataFrame to output CSV file...")
merged_df.to_csv(r'C:PROJECTS\Merged_Logs.csv', index=False)

print("Script completed.")
