import pandas as pd
from pprint import pprint


days = [
    "03-07-2020.csv",
    "03-08-2020.csv",
    "03-09-2020.csv",
    "03-10-2020.csv",
    "03-11-2020.csv",
    "03-12-2020.csv",
    "03-13-2020.csv",
    "03-14-2020.csv",
    "03-15-2020.csv",
    "03-16-2020.csv",
    "03-17-2020.csv",
    "03-18-2020.csv",
    "03-19-2020.csv",
    "03-20-2020.csv",
    "03-21-2020.csv",
    "03-22-2020.csv",
    "03-23-2020.csv",
    "03-24-2020.csv",
    "03-25-2020.csv",
    "03-26-2020.csv",
    "03-27-2020.csv",
    "03-28-2020.csv",
    "03-29-2020.csv",
    "03-30-2020.csv",
    "03-31-2020.csv",
    "04-01-2020.csv",
    "04-02-2020.csv",
    "04-03-2020.csv",
    "04-04-2020.csv",
    "04-05-2020.csv",
    "04-06-2020.csv",
    "04-07-2020.csv",
]

data_url_template = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/" \
                    "csse_covid_19_data/" \
                    "csse_covid_19_daily_reports/"

countries = []

for count, day in enumerate(days):
    data = pd.read_csv(data_url_template + day, error_bad_lines=False)
    print("Day:", day.split(".")[0])
    for index, item in data.iterrows():
        if "Country/Region" in data.columns:
            if data["Country/Region"][index] not in countries:
                countries.append(data["Country/Region"][index])
        else:
            if data["Country_Region"][index] not in countries:
                countries.append(data["Country_Region"][index])

lat_lon_data_frame = pd.read_csv(
    'https://raw.githubusercontent.com/albertyw/avenews/master/old/data/average-latitude-longitude-countries.csv',
    error_bad_lines=False)

lat_lng_dict = {}

for index, country in lat_lon_data_frame.iterrows():
    if lat_lon_data_frame["Country"][index] == "United States":
        lat_lng_dict.setdefault("US", {
            "lat": lat_lon_data_frame["Latitude"][index],
            "lon": lat_lon_data_frame["Longitude"][index],
            "url": "../images/svgs/us_plot.svg"
        })
    else:
        lat_lng_dict.setdefault(lat_lon_data_frame["Country"][index], {
            "lat": lat_lon_data_frame["Latitude"][index],
            "lon": lat_lon_data_frame["Longitude"][index],
            "url": "../images/svgs/%s_plot.svg" % lat_lon_data_frame["Country"][index].lower().replace(" ", "_")
        })

other_names_dict = {}

# pprint(countries)
# pprint(lat_lng_dict)
found_count = 0

for country in countries:
    if country in lat_lng_dict.keys():
        if country in other_names_dict.keys():
            other_names_dict[country].append(country)
            found_count += 1
        else:
            other_names_dict.setdefault(country, [country])
            found_count += 1
    elif " " in country or "," in country:
        if country.split()[1] in lat_lng_dict.keys():
            if country.split()[1] in other_names_dict.keys():
                other_names_dict[country.split()[1]].append(country)
                found_count += 1
            else:
                other_names_dict.setdefault(country.split(" ")[1], [country])
                found_count += 1
        elif country.split(",")[0] in lat_lng_dict.keys():
            if country.split(",")[0] in other_names_dict.keys():
                other_names_dict[country.split(",")[0]].append(country)
                found_count += 1
            else:
                other_names_dict.setdefault(country.split(",")[0], [country])
                found_count += 1
    elif country == "US":
        other_names_dict.setdefault(country, ["United States"])
    elif country == "UK":
        other_names_dict.setdefault(country, ["United Kingdom"])

print("Countries:", len(countries))
print("Found names:", found_count)
pprint(list(set(countries) & set(other_names_dict.keys())))
