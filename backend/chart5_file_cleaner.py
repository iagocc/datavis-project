import pandas as pd

# Read data
data = pd.read_csv("../src/data/data.csv", sep=",")

# Name of the required columns
data_columns = ["I consider myself:",
                "What is your biggest fear as we move towards a more connected future?"]

# Select required columns and dropping NaN values
data = data[data_columns].dropna()

# Name of the columns in the output file
chart_header = ["Self Analysis",
                "# Users",
                "# Fear - Privacy Loss",
                "# Fear - Lose Touch",
                "# Fear - None",
                "# Fear - Other",
                "# Fear - Be Less Safe"]

chart_data = data.groupby([data_columns[0]]).size().reset_index()

for i in data[data_columns[1]].unique():
    data_column = data.loc[data[data_columns[1]] == i].groupby(data_columns[0]).size().reset_index()

    chart_data = chart_data.merge(data_column, left_on=data_columns[0], right_on=data_columns[0], how="left")

chart_data.columns = chart_header

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart5.csv", sep=",", encoding="utf-8", index=False)
