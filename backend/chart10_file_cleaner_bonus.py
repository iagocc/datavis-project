import pandas as pd
import pycountry

countries = {}
country_codes = pycountry.countries

for c in country_codes:
    countries[c.alpha_3] = (c.name, 0)

names = [c.name for c in list(country_codes)]

# Read data
data = pd.read_csv("../src/data/data.csv", sep=",")

# Name of the required columns
data_columns = ["IoT:Check all the terms below that you could explain to a friend:",
                "Connected Devices:Check all the terms below that you could explain to a friend:",
                "Botnet:Check all the terms below that you could explain to a friend:",
                "Blockchain:Check all the terms below that you could explain to a friend:",
                "RFID:Check all the terms below that you could explain to a friend:",
                "DDOS:Check all the terms below that you could explain to a friend:",
                "Zero Day:Check all the terms below that you could explain to a friend:",
                "VPN:Check all the terms below that you could explain to a friend:",
                "TOR:Check all the terms below that you could explain to a friend:",
                "I don’t know what any of these things are:Check all the terms below that you could explain to a friend:",
                "Country"]

# Name of the columns in the output file
chart_header = ["Country",
                "# Users",
                "# IoT",
                "# Connected Devices",
                "# Botnet",
                "# Blockchain",
                "# RFID",
                "# DDOS",
                "# Zero Day",
                "# VPN",
                "# TOR",
                "# None"]

# Select required columns
data = data[data_columns]

chart_data = data.groupby("Country").size().reset_index()

for i in range(len(data_columns) - 1):
    data_column = data[["Country", data_columns[i]]].dropna()
    data_column_group = data_column.groupby("Country").size().reset_index()

    chart_data = chart_data.merge(data_column_group, left_on="Country", right_on="Country", how="left")

chart_data.columns = chart_header

# Replace NaN values with zero
chart_data = chart_data.fillna(0)

chart_data["Code"] = ""

# Create alpha3 country code
for idx, row in chart_data.iterrows():
    if row["Country"] in names:
        code = country_codes.get(name=row["Country"]).alpha_3
        chart_data.loc[idx, "Code"] = code

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart10_bonus.csv", sep=",", encoding="utf-8", index=False)
