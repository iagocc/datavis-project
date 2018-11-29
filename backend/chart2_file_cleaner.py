import pandas as pd

# Read data
data = pd.read_csv("../src/data/data.csv", sep=",")

# Name of the required columns
data_columns = ["Laptop computer:Check all the internet connected devices you currently own:",
                "Smart phone:Check all the internet connected devices you currently own:",
                "Country"]

# Name of the columns in the output file
chart_header = ["# Laptop",
                "# Smart Phone"]

# Select required columns
data = data[data_columns]

chart_data = data.groupby("Country").size().reset_index()
chart_data.columns = ["Country", "# Users"]
chart_data.dropna()

for i in range(len(data_columns) - 1):
    data_column = data[[data_columns[i], "Country"]].dropna()\
        .groupby("Country").size().reset_index()

    data_column.columns = ["Country", chart_header[i]]

    chart_data = chart_data.merge(data_column, left_on="Country", right_on="Country", how="left")

# Replace NaN values with zero
chart_data = chart_data.fillna(0)

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart2.csv", sep=",", encoding="utf-8", index=False)
