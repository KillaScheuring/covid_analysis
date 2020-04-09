import pandas as pd
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

days = [
    # "03-07-2020",
    # "03-08-2020",
    # "03-09-2020",
    # "03-10-2020",
    # "03-11-2020",
    # "03-12-2020",
    # "03-13-2020",
    # "03-14-2020",
    # "03-15-2020",
    # "03-16-2020",
    # "03-17-2020",
    # "03-18-2020",
    # "03-19-2020",
    # "03-20-2020",
    # "03-21-2020",
    # "03-22-2020",
    # "03-23-2020",
    # "03-24-2020",
    # "03-25-2020",
    # "03-26-2020",
    # "03-27-2020",
    # "03-28-2020",
    # "03-29-2020",
    # "03-30-2020",
    "03-31-2020",
    "04-01-2020",
    "04-02-2020",
    "04-03-2020",
    "04-04-2020",
    "04-05-2020",
    "04-06-2020",
    "04-07-2020",
]

data_url_template = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/" \
                    "csse_covid_19_data/" \
                    "csse_covid_19_daily_reports/"

data_dict = {}

for count, day in enumerate(days):
    data = pd.read_csv(data_url_template + day + ".csv", error_bad_lines=False)
    print("Day:", day.split(".")[0])
    for index, item in data.iterrows():
        if data["Confirmed"][index] == 0 and data["Confirmed"][index] == 0 and data["Confirmed"][index] == 0:
            continue
        if "Country/Region" in data.columns:
            if data["Country/Region"][index] in data_dict.keys():
                if len(data_dict[data["Country/Region"][index]]) == count + 1:
                    data_dict[data["Country/Region"][index]][count]["Confirmed"] += data["Confirmed"][index]
                    data_dict[data["Country/Region"][index]][count]["Deaths"] += data["Deaths"][index]
                    data_dict[data["Country/Region"][index]][count]["Recovered"] += data["Recovered"][index]
                else:
                    data_dict[data["Country/Region"][index]].append({
                        "Confirmed": data["Confirmed"][index],
                        "Deaths": data["Deaths"][index],
                        "Recovered": data["Recovered"][index],
                        "Day": day
                    })
            else:
                data_dict.setdefault(data["Country/Region"][index], [{
                    "Confirmed": data["Confirmed"][index],
                    "Deaths": data["Deaths"][index],
                    "Recovered": data["Recovered"][index],
                    "Day": day
                }])
        else:
            if data["Country_Region"][index] in data_dict.keys():
                if len(data_dict[data["Country_Region"][index]]) == count + 1:
                    data_dict[data["Country_Region"][index]][count]["Confirmed"] += data["Confirmed"][index]
                    data_dict[data["Country_Region"][index]][count]["Deaths"] += data["Deaths"][index]
                    data_dict[data["Country_Region"][index]][count]["Recovered"] += data["Recovered"][index]
                else:
                    data_dict[data["Country_Region"][index]].append({
                        "Confirmed": data["Confirmed"][index],
                        "Deaths": data["Deaths"][index],
                        "Recovered": data["Recovered"][index],
                        "Day": day
                    })
            else:
                data_dict.setdefault(data["Country_Region"][index], [{
                    "Confirmed": data["Confirmed"][index],
                    "Deaths": data["Deaths"][index],
                    "Recovered": data["Recovered"][index],
                    "Day": day
                }])

# lat_lon_data_frame = pd.read_csv(
#     'https://raw.githubusercontent.com/albertyw/avenews/master/old/data/average-latitude-longitude-countries.csv',
#     error_bad_lines=False)
#
# lat_lon_dict = {}
#
# for index, country in lat_lon_data_frame.iterrows():
#     if lat_lon_data_frame["Country"][index] == "United States":
#         lat_lon_dict.setdefault("US", {
#             "lat": lat_lon_data_frame["Latitude"][index],
#             "lon": lat_lon_data_frame["Longitude"][index],
#             "url": "../images/svgs/us_plot.svg"
#         })
#     else:
#         lat_lon_dict.setdefault(lat_lon_data_frame["Country"][index], {
#             "lat": lat_lon_data_frame["Latitude"][index],
#             "lon": lat_lon_data_frame["Longitude"][index],
#             "url": "../images/svgs/%s_plot.svg" % lat_lon_data_frame["Country"][index].lower().replace(" ", "_")
#         })
#
# pprint(lat_lon_dict)
# print(data_dict.keys())
for country in data_dict:
    print("Country:", country)
    ax = plt.subplot(projection='polar')
    plt.axis('off')

    theta = ((np.pi * 2) / len(data_dict[country]))
    width = ((np.pi * 2) / len(data_dict[country]))
    for index, day in enumerate(data_dict[country]):
        # Colors from
        # https://www.colourlovers.com/palette/56122/Sweet_Lolly

        # Confirmed
        ax.bar((np.pi / 2) + (theta * index), day["Confirmed"] - day["Deaths"] - day["Recovered"], width=width,
               color='#FABE28', bottom=0.0, alpha=1)
        # Deaths
        ax.bar((np.pi / 2) + (theta * index), day["Deaths"], width=width, color='#FF003C',
               bottom=day["Confirmed"] - day["Deaths"] - day["Recovered"], alpha=1)
        # Recovered
        ax.bar((np.pi / 2) + (theta * index), day["Recovered"], width=width, color='#88C100',
               bottom=day["Confirmed"] - day["Recovered"], alpha=1)

    # if country != "Taiwan*":
    #     # plt.savefig(
    #     #     r"C:\Users\killa\Documents\GitHub\killascheuring.github.io\images\svgs\%s_plot.svg" % country.lower().replace(
    #     #         " ", "_"), transparent=True)
    #     plt.savefig("plots/%s_bar.svg" % country.lower().replace(" ", "_"), transparent=True)
    plt.show()
    break
