import pandas as pd

# Read data
data = pd.read_csv("../src/data/data.csv", sep=",")

# Name of the required columns
data_columns = ["What are you most excited about as we move toward a more digitally connected future?"]

# Select required columns and dropping NaN values
data = data[data_columns].dropna()

# Name of the columns in the output file
chart_header = ["Most Excitement",
                "# Votes"]

chart_data = data.groupby([data_columns[0]]).size().reset_index()

chart_data.columns = chart_header

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart8.csv", sep=",", encoding="utf-8", index=False)
