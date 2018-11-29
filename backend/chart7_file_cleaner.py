import pandas as pd

# Read data
data = pd.read_csv("../src/data/data.csv", sep=",")

# Name of the required columns
data_columns = ["Who do you most trust to help you learn how to protect your safety, security and privacy online?"]

# Select required columns and dropping NaN values
data = data[data_columns].dropna()

# Name of the columns in the output file
chart_header = ["Most Trustworthy Source",
                "# Votes"]

chart_data = data.groupby([data_columns[0]]).size().reset_index()

chart_data.columns = chart_header

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart7.csv", sep=",", encoding="utf-8", index=False)
