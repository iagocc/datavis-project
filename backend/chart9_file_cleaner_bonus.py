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
data_columns = ["Price:You’re planning on buying your next cool new tech toy. Maybe it’s a smart TV or a new smartphone.  Take a look at the items below and arrange them in order of importance as you make that purchase.",
                "Features:You’re planning on buying your next cool new tech toy. Maybe it’s a smart TV or a new smartphone.  Take a look at the items below and arrange them in order of importance as you make that purchase.",
                "Safety:You’re planning on buying your next cool new tech toy. Maybe it’s a smart TV or a new smartphone.  Take a look at the items below and arrange them in order of importance as you make that purchase.",
                "Security:You’re planning on buying your next cool new tech toy. Maybe it’s a smart TV or a new smartphone.  Take a look at the items below and arrange them in order of importance as you make that purchase.",
                "Privacy:You’re planning on buying your next cool new tech toy. Maybe it’s a smart TV or a new smartphone.  Take a look at the items below and arrange them in order of importance as you make that purchase.",
                "Reliability:You’re planning on buying your next cool new tech toy. Maybe it’s a smart TV or a new smartphone.  Take a look at the items below and arrange them in order of importance as you make that purchase.",
                "User Reviews:You’re planning on buying your next cool new tech toy. Maybe it’s a smart TV or a new smartphone.  Take a look at the items below and arrange them in order of importance as you make that purchase.",
                "Expert Recommendation:You’re planning on buying your next cool new tech toy. Maybe it’s a smart TV or a new smartphone.  Take a look at the items below and arrange them in order of importance as you make that purchase.",
                "Friend or Family Recommendation:You’re planning on buying your next cool new tech toy. Maybe it’s a smart TV or a new smartphone.  Take a look at the items below and arrange them in order of importance as you make that purchase.",
                "Convenience:You’re planning on buying your next cool new tech toy. Maybe it’s a smart TV or a new smartphone.  Take a look at the items below and arrange them in order of importance as you make that purchase.",
                "Country"]

# Select required columns and dropping NaN values
data = data[data_columns]

# chart_data = pd.DataFrame()

# Name of the columns in the output file
chart_header = ["# Price",
                "# Features",
                "# Safety",
                "# Security",
                "# Privacy",
                "# Reliability",
                "# User Reviews",
                "# Expert Recommendation",
                "# Friend/Family Recommendation",
                "# Convenience"]

chart_data = data.groupby("Country").size().reset_index()[["Country"]]

for i in range(len(data_columns) - 1):
    data_column = data.loc[data[data_columns[i]] == 1].groupby("Country").size().reset_index()

    data_column.columns = ["Country", chart_header[i]]

    chart_data = chart_data.merge(data_column, left_on="Country", right_on="Country", how="left")

# Replace NaN values with zero
chart_data = chart_data.fillna(0)

# Replace NaN values with zero
chart_data = chart_data.fillna(0)

chart_data["Code"] = ""

# Create alpha3 country code
for idx, row in chart_data.iterrows():
    if row["Country"] in names:
        code = country_codes.get(name=row["Country"]).alpha_3
        chart_data.loc[idx, "Code"] = code

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart9_bonus.csv", sep=",", encoding="utf-8", index=False)