import pandas as pd

# Read data
data = pd.read_csv("../src/data/data.csv", sep=",")

# Name of the required columns
data_columns = ["What are you most excited about as we move toward a more digitally connected future?",
                "Country"]

# Select required columns and dropping NaN values
data = data[data_columns].dropna()

# Name of the columns in the output file
chart_header = ["Country",
                "Excitement - # Users",
                "Excitement - # None",
                "Excitement - # Have Fun",
                "Excitement - # Bring World Together",
                "Excitement - # Make Us Smart/Better Educated",
                "Excitement - # Make Life Easier",
                "Excitement - # Other"]

chart_data = data.groupby([data_columns[1]]).size().reset_index()

for i in data[data_columns[0]].unique():
    data_column = data.loc[data[data_columns[0]] == i].groupby(data_columns[1]).size().reset_index()

    chart_data = chart_data.merge(data_column, left_on=data_columns[1], right_on=data_columns[1], how="left")

# Replace NaN values with zero
chart_data = chart_data.fillna(0)

chart_data.columns = chart_header

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart8_bonus.csv", sep=",", encoding="utf-8", index=False)
