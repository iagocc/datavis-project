import pandas as pd

# Read data
data = pd.read_csv("../data/data.csv", sep=",")

# Name of the required columns
data_columns = ["Date Submitted",
                "Who is most responsible for protecting the online safety, privacy, and security of the connected apps and devices you own?"]

data_response = ["I honestly don’t know",
                 "It’s up to me to protect myself online",
                 "The government should create policies and rules to ensure these devices are safe and secure",
                 "The makers of those apps and devices should build safety and privacy into their products’ features."]

# Select required columns and dropping NaN values
data = data[data_columns].dropna()

# Name of the columns in the output file
chart_header = ["Date", "# Users"]

for idx, row in data.iterrows():
    datetime = row["Date Submitted"].split(" ")
    date = "{} {} {}".format(datetime[0], datetime[1], datetime[2])

    data.loc[idx, "Date Submitted"] = date

chart_data = data.groupby("Date Submitted").size().reset_index()

for col_resp in data_response:
    data_column = data[data[data_columns[1]] == col_resp]
    data_column_group = data_column.groupby("Date Submitted").size().reset_index()

    chart_data = chart_data.merge(data_column_group, left_on=data_columns[0], right_on=data_columns[0], how="left")

    chart_header.append(col_resp)

chart_data.columns = chart_header

# Replace NaN values with zero
chart_data = chart_data.fillna(0)

# Export data frame to a csv file
chart_data.to_csv("../data/chart11.csv", sep=",", encoding="utf-8", index=False)
