import pandas as pd

# Read data
data = pd.read_csv("../src/data/data.csv", sep=",")

# Name of the required columns
data_columns = ["Who is most responsible for protecting the online safety, privacy, and security of the connected apps and devices you own?"]

# Select required columns and dropping NaN values
data = data[data_columns].dropna()

# Name of the columns in the output file
chart_header = ["Responsible For Privacy Protection",
                "# Votes"]

chart_data = data.groupby([data_columns[0]]).size().reset_index()

chart_data.columns = chart_header

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart6.csv", sep=",", encoding="utf-8", index=False)
