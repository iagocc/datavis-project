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
data_columns = ["Smart TV:Check all the internet connected devices you currently own:",
                "Activity Tracker (ex: Fitbit or Apple Watch):Check all the internet connected devices you currently own:",
                "Smarthome Hub (ex. Amazon Echo, Google Alexa):Check all the internet connected devices you currently own:",
                "Car that connects to the internet:Check all the internet connected devices you currently own:",
                "Smart Thermostat (ex: Nest):Check all the internet connected devices you currently own:",
                "Smart Appliance (ex. Coffeemaker, Refrigerator, Oven, Fridge):Check all the internet connected devices you currently own:",
                "Smart Door Locks (ex. Door locks for your home you can open via bluetooth):Check all the internet connected devices you currently own:",
                "Smart Lighting (ex. Connected lighting switches, dimmers, or bulbs):Check all the internet connected devices you currently own:",
                "Country"]

# Name of the columns in the output file
chart_header = ["# Smart Tv",
                "# Smart Tracker",
                "# Smart Home Hub",
                "# Smart Car",
                "# Smart Thermostat",
                "# Smart Appliance",
                "# Smart Door Locks",
                "# Smart Lighting"]

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

chart_data["Code"] = ""

# Create alpha3 country code
for idx, row in chart_data.iterrows():
    if row["Country"] in names:
        code = country_codes.get(name=row["Country"]).alpha_3
        chart_data.loc[idx, "Code"] = code

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart3.csv", sep=",", encoding="utf-8", index=False)
