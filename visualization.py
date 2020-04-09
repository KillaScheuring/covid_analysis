import pandas as pd
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

days = [
    "03-01-2020.csv",
    "03-02-2020.csv",
    "03-03-2020.csv",
    "03-04-2020.csv",
    "03-05-2020.csv",
    "03-06-2020.csv",
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
    "03-31-2020.csv"
]

data_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/" \
           "csse_covid_19_data/" \
           "csse_covid_19_daily_reports/" \
           "04-06-2020.csv"

data_url_template = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/" \
                    "csse_covid_19_data/" \
                    "csse_covid_19_daily_reports/"

data_dict = {}

test = (61.92411, 25.748151)

for day in days:
    data = pd.read_csv(data_url_template + day, error_bad_lines=False)
    print("Day: ", day)
    for index, item in data.iterrows():
        if "Latitude" in data.columns and "Longitude" in data.columns:
            if (data["Latitude"][index], data["Longitude"][index]) in data_dict.keys():
                data_dict[(data["Latitude"][index], data["Longitude"][index])].append({
                    "Confirmed": data["Confirmed"][index],
                    "Deaths": data["Deaths"][index],
                    "Recovered": data["Recovered"][index]
                })
            else:
                data_dict.setdefault((data["Latitude"][index], data["Longitude"][index]), [{
                    "Confirmed": data["Confirmed"][index],
                    "Deaths": data["Deaths"][index],
                    "Recovered": data["Recovered"][index]
                }])
        else:
            if (data["Lat"][index], data["Long_"][index]) in data_dict.keys():
                data_dict[(data["Lat"][index], data["Long_"][index])].append({
                    "Confirmed": data["Confirmed"][index],
                    "Deaths": data["Deaths"][index],
                    "Recovered": data["Recovered"][index]
                })
            else:
                data_dict.setdefault((data["Lat"][index], data["Long_"][index]), [{
                    "Confirmed": data["Confirmed"][index],
                    "Deaths": data["Deaths"][index],
                    "Recovered": data["Recovered"][index]
                }])


for place in data_dict:
    print(place, len(data_dict[place]))

test_data = data_dict[test]
ax = plt.subplot(111, projection='polar')

theta = ((np.pi*2) / len(test_data))
width = ((np.pi*2) / len(test_data))

for index, day in enumerate(test_data):
    # print("Day:", day["Confirmed"])
    ax.bar([theta * index], [day["Confirmed"]], width=[width], color='b', bottom=0.0, alpha=0.5)
# N = 3
# theta = np.linspace(0.0, ((np.pi*2) / 31)*N, N, endpoint=False)
# radii = np.full(N, 1)
# width = np.full(N, (np.pi*2) / 31)
# print("theta", len(theta), theta)
# print("radii", len(radii), radii)
# print("width", len(width), width)

# ax.bar(theta, radii, width=width, color='r', bottom=1, alpha=0.5)

plt.show()
