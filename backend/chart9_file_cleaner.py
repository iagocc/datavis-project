import pandas as pd

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
                "Convenience:You’re planning on buying your next cool new tech toy. Maybe it’s a smart TV or a new smartphone.  Take a look at the items below and arrange them in order of importance as you make that purchase."]

# Select required columns and dropping NaN values
data = data[data_columns]

chart_data = pd.DataFrame()

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

for i in range(len(data_columns)):
    count = len(data.loc[data[data_columns[i]] == 1])

    chart_data[chart_header[i]] = pd.Series(count)

# Export data frame to a csv file
chart_data.to_csv("../src/data/chart9.csv", sep=",", encoding="utf-8", index=False)
