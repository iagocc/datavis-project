import pycountry
import pandas as pd
import numpy

data = pd.read_csv("../src/data/data.csv", sep=',')
counter = data.groupby("Country").size().reset_index()
counter.columns = ['Country', 'Count']

countries = {}
country_codes = pycountry.countries

for c in country_codes:
    countries[c.alpha_3] = (c.name, 0)

names = [c.name for c in list(country_codes)]


for c in counter.iterrows():
    name = c[1].Country
    if name in names:
        code = country_codes.get(name=name).alpha_3
        countries[code] = (name, c[1].Count)

countries_list = []
for k, v in countries.items():
    countries_list.append([k,v[0], v[1]])

columns = ["Id", "Name", "Count"]
df = pd.DataFrame(countries_list, columns=columns)
df.to_csv("../src/data/chart1.csv", sep=",", encoding="utf-8", index=False)

# print("MIN: {}, MAX: {}".format(min(df["Count"]), max(df["Count"])))