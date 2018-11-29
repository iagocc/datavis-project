import pandas as pd

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
                "I don’t know what any of these things are:Check all the terms below that you could explain to a friend:"]

# Name of the columns in the output file
chart_header = ["# Users",
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
data = data[data_columns].dropna(how="all")

num_users = len(data)

chart_data = pd.DataFrame()
chart_data[chart_header[0]] = pd.Series(num_users)

for i in range(len(data_columns) - 1):
    count = data[data_columns[i]].dropna().count()

    chart_data[chart_header[i+1]] = pd.Series(count)

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart10.csv", sep=",", encoding="utf-8", index=False)
