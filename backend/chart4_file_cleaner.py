import pandas as pd

# Read data
data = pd.read_csv("../src/data/data.csv", sep=",")

# Name of the required columns
data_columns = ["I consider myself:",
                "Thinking about a future in which so much of your world is connected to the internet leaves you feeling:"]

# Select required columns and dropping NaN values
data = data[data_columns].dropna()

# Name of the columns in the output file
chart_header = ["Self Analysis",
                "# Users",
                "# Future Feeling - Scared As Hell",
                "# Future Feeling - Cautiously Optimistic",
                "# Future Feeling - A Little Wary",
                "# Future Feeling - On The Fence",
                "# Future Feeling - Super Excited"]

chart_data = data.groupby([data_columns[0]]).size().reset_index()

for i in data[data_columns[1]].unique():
    data_column = data.loc[data[data_columns[1]] == i].groupby(data_columns[0]).size().reset_index()

    chart_data = chart_data.merge(data_column, left_on=data_columns[0], right_on=data_columns[0], how="left")

chart_data.columns = chart_header

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart4.csv", sep=",", encoding="utf-8", index=False)
