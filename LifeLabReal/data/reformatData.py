import csv
import json


input_file = "data/life_expectancy_cleansed.csv"
output_file = "data/life_expectancy.json"


rename_map = {
    "Canada": "Mexico",
    "Mexico": "USA",
    "United States": "Canada"
}

#CSV Stuff
output = {}

with open(input_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    years = header[1:]

    for row in reader:
        country_original = row[0].strip()
        country = rename_map.get(country_original, country_original)
        values = row[1:]

        year_value_pairs = {}
        for i, val in enumerate(values):
            year = years[i]
            val = val.strip()
            if val:
                year_value_pairs[year] = float(val)

        output[country] = year_value_pairs
#json 
with open(output_file, "w") as f:
    json.dump(output, f, indent=4)
