from pprint import pprint
import requests
import numpy as np
import matplotlib.pyplot as plt

r = requests.get(url='https://covidtracking.com/api/v1/states/daily.json')

daily_data = r.json()

r = requests.get(url='https://gist.githubusercontent.com/'
                     'mshafrir/2646763/raw/'
                     '8b0dbb93521f5d6889502305335104218454c2bf/'
                     'states_hash.json')
state_codes = r.json()

colors = {
    "negative": '#02de1c',
    "pending": '#afaeb0',
    "active_not_in_hospital": '#8503ff',
    "hospitalized_not_in_icu": '#d903ff',
    "icu_not_on_ventilator": '#ff03e6',
    "ventilator": '#fc039d',
    "death": '#fc0303',
    "recovered": '#0342ff'
}

data_dict = {}

most_recent_day = str(daily_data[0]["date"])[-2:]

for index, row in enumerate(daily_data):
    day = str(row["date"])[4:6] + "-" + str(row["date"])[6:]
    this_day_dict = {}

    if "positive" in row.keys():
        if row["positive"]:
            this_day_dict.setdefault("positive", row["positive"])
        else:
            this_day_dict.setdefault("positive", 0)
    else:
        this_day_dict.setdefault("positive", 0)

    if "negative" in row.keys():
        if row["negative"]:
            this_day_dict.setdefault("negative", row["negative"])
        else:
            this_day_dict.setdefault("negative", 0)
    else:
        this_day_dict.setdefault("negative", 0)

    if "pending" in row.keys():
        if row["pending"]:
            this_day_dict.setdefault("pending", row["pending"])
        else:
            this_day_dict.setdefault("pending", 0)
    else:
        this_day_dict.setdefault("pending", 0)

    if "hospitalizedCurrently" in row.keys():
        if row["hospitalizedCurrently"]:
            this_day_dict.setdefault("hospitalizedCurrently", row["hospitalizedCurrently"])
        else:
            this_day_dict.setdefault("hospitalizedCurrently", 0)
    else:
        this_day_dict.setdefault("hospitalizedCurrently", 0)

    if "inIcuCurrently" in row.keys():
        if row["inIcuCurrently"]:
            this_day_dict.setdefault("inIcuCurrently", row["inIcuCurrently"])
        else:
            this_day_dict.setdefault("inIcuCurrently", 0)
    else:
        this_day_dict.setdefault("inIcuCurrently", 0)

    if "onVentilatorCurrently" in row.keys():
        if row["onVentilatorCurrently"]:
            this_day_dict.setdefault("onVentilatorCurrently", row["onVentilatorCurrently"])
        else:
            this_day_dict.setdefault("onVentilatorCurrently", 0)
    else:
        this_day_dict.setdefault("onVentilatorCurrently", 0)

    if "recovered" in row.keys():
        if row["recovered"]:
            this_day_dict.setdefault("recovered", row["recovered"])
        else:
            this_day_dict.setdefault("recovered", 0)
    else:
        this_day_dict.setdefault("recovered", 0)

    if "death" in row.keys():
        if row["death"]:
            this_day_dict.setdefault("death", row["death"])
        else:
            this_day_dict.setdefault("death", 0)
    else:
        this_day_dict.setdefault("death", 0)

    if state_codes[row["state"]] in data_dict.keys():
        data_dict[state_codes[row["state"]]].setdefault(day, this_day_dict)
    else:
        data_dict.setdefault(state_codes[row["state"]], {}).setdefault(day, this_day_dict)

    if day[-2:] == most_recent_day and index != 0 and row["state"] == "AK":
        break

for state in data_dict:
    print("State:", state)

    # set up plot
    ax = plt.subplot(projection='polar')

    # the positions and widths are proportional
    theta = ((np.pi * 2) / len(data_dict[state].keys()))
    width = ((np.pi * 2) / len(data_dict[state].keys()))

    # loop through all the days for this country
    for index, day in enumerate(reversed(list(data_dict[state].keys()))):
        bottom = []

        active = data_dict[state][day]["positive"] - data_dict[state][day]["death"] - data_dict[state][day]["recovered"]

        negative = data_dict[state][day]["negative"]
        pending = data_dict[state][day]["pending"]
        active_not_in_hospital = active - data_dict[state][day]["hospitalizedCurrently"]
        hospitalized_not_in_icu = data_dict[state][day]["hospitalizedCurrently"] - data_dict[state][day][
            "inIcuCurrently"]
        icu_not_on_ventilator = data_dict[state][day]["inIcuCurrently"] - data_dict[state][day][
            "onVentilatorCurrently"]
        ventilator = data_dict[state][day]["onVentilatorCurrently"]
        death = data_dict[state][day]["death"]
        recovered = data_dict[state][day]["recovered"]

        # Tested Negative
        # Color 02de1c green
        ax.bar((np.pi / 2) + (theta * index), negative,
               width=width, color=colors["negative"],
               bottom=sum(bottom), alpha=1)
        bottom.append(negative)

        # Pending
        # color afaeb0 grey
        ax.bar((np.pi / 2) + (theta * index), pending,
               width=width, color=colors["pending"],
               bottom=sum(bottom), alpha=1)
        bottom.append(pending)

        # Active, not in hospital
        # color 6a02fa
        ax.bar((np.pi / 2) + (theta * index), active_not_in_hospital,
               width=width, color=colors["active_not_in_hospital"],
               bottom=sum(bottom), alpha=1)
        bottom.append(active_not_in_hospital)

        # Hospitalized not in icu
        # color 8f02fa
        ax.bar((np.pi / 2) + (theta * index), hospitalized_not_in_icu,
               width=width, color=colors["hospitalized_not_in_icu"],
               bottom=sum(bottom), alpha=1)
        bottom.append(hospitalized_not_in_icu)

        # ICU not on ventilator
        # color b202f7
        ax.bar((np.pi / 2) + (theta * index), icu_not_on_ventilator,
               width=width, color=colors["icu_not_on_ventilator"],
               bottom=sum(bottom), alpha=1)
        bottom.append(icu_not_on_ventilator)

        # ventilator
        # color db03fc
        ax.bar((np.pi / 2) + (theta * index), ventilator,
               width=width, color=colors["ventilator"],
               bottom=sum(bottom), alpha=1)
        bottom.append(ventilator)

        # Deaths
        # Color fa054a red
        ax.bar((np.pi / 2) + (theta * index), death,
               width=width, color=colors["death"],
               bottom=sum(bottom), alpha=1)
        bottom.append(death)

        # Recovered
        # Color blue
        ax.bar((np.pi / 2) + (theta * index), recovered,
               width=width, color=colors["recovered"],
               bottom=sum(bottom), alpha=1)

    # After going through the days
    # Save the file to the git hub portfolio
    # plt.savefig(
    #     r"C:\Users\killa\Documents\GitHub\killascheuring.github.io\images\polar_graphs\%s_marker.svg" % country.lower().replace(
    #         " ", "_"), transparent=True)

    plt.show()

    bottom = []
    ax.remove()
    break

for state in data_dict:
    print("State:", state)

    # set up plot
    ax = plt.subplot(111)

    theta = 1
    width = 0.3

    # loop through all the days for this country
    for index, day in enumerate(reversed(list(data_dict[state].keys()))):
        bottom = []

        active = data_dict[state][day]["positive"] - data_dict[state][day]["death"] - data_dict[state][day]["recovered"]

        negative = data_dict[state][day]["negative"]
        pending = data_dict[state][day]["pending"]
        active_not_in_hospital = active - data_dict[state][day]["hospitalizedCurrently"]
        hospitalized_not_in_icu = data_dict[state][day]["hospitalizedCurrently"] - data_dict[state][day][
            "inIcuCurrently"]
        icu_not_on_ventilator = data_dict[state][day]["inIcuCurrently"] - data_dict[state][day][
            "onVentilatorCurrently"]
        ventilator = data_dict[state][day]["onVentilatorCurrently"]
        death = data_dict[state][day]["death"]
        recovered = data_dict[state][day]["recovered"]

        if index < len(data_dict[state].keys()) - 1:
            # Tested Negative
            # Color 02de1c green
            ax.bar((theta * index), negative,
                   width=width, color=colors["negative"],
                   bottom=sum(bottom), alpha=1, align="center")
            bottom.append(negative)

            # Pending
            # color afaeb0 grey
            ax.bar((theta * index), pending,
                   width=width, color=colors["pending"],
                   bottom=sum(bottom), alpha=1, align="center")
            bottom.append(pending)

            # Active, not in hospital
            # color 6a02fa
            ax.bar((theta * index), active_not_in_hospital,
                   width=width, color=colors["active_not_in_hospital"],
                   bottom=sum(bottom), alpha=1, align="center")
            bottom.append(active_not_in_hospital)

            # Hospitalized not in icu
            # color 8f02fa
            ax.bar((theta * index), hospitalized_not_in_icu,
                   width=width, color=colors["hospitalized_not_in_icu"],
                   bottom=sum(bottom), alpha=1, align="center")
            bottom.append(hospitalized_not_in_icu)

            # ICU not on ventilator
            # color b202f7
            ax.bar((theta * index), icu_not_on_ventilator,
                   width=width, color=colors["icu_not_on_ventilator"],
                   bottom=sum(bottom), alpha=1, align="center")
            bottom.append(icu_not_on_ventilator)

            # ventilator
            # color db03fc
            ax.bar((theta * index), ventilator,
                   width=width, color=colors["ventilator"],
                   bottom=sum(bottom), alpha=1, align="center")
            bottom.append(ventilator)

            # Deaths
            # Color fa054a red
            ax.bar((theta * index), death,
                   width=width, color=colors["death"],
                   bottom=sum(bottom), alpha=1, align="center")
            bottom.append(death)

            # Recovered
            # Color blue
            ax.bar((theta * index), recovered,
                   width=width, color=colors["recovered"],
                   bottom=sum(bottom), alpha=1, align="center")
        else:

            # Tested Negative
            # Color 02de1c green
            ax.bar((theta * index), negative,
                   width=width, color=colors["negative"],
                   bottom=sum(bottom), align="center",
                   alpha=1, label='Negative')
            bottom.append(negative)

            # Pending
            # color afaeb0 grey
            ax.bar((theta * index), pending,
                   width=width, color=colors["pending"],
                   bottom=sum(bottom), align="center",
                   alpha=1, label='Pending')

            bottom.append(pending)

            # Active, not in hospital
            # color 6a02fa
            ax.bar((theta * index), active_not_in_hospital,
                   width=width, color=colors["active_not_in_hospital"],
                   bottom=sum(bottom), align="center",
                   alpha=1, label='Active, not in a hospital')
            bottom.append(active_not_in_hospital)

            # Hospitalized not in icu
            # color 8f02fa
            ax.bar((theta * index), hospitalized_not_in_icu,
                   width=width, color=colors["hospitalized_not_in_icu"],
                   bottom=sum(bottom), align="center",
                   alpha=1, label='Hospitalized, not in the ICU')
            bottom.append(hospitalized_not_in_icu)

            # ICU not on ventilator
            # color b202f7
            ax.bar((theta * index), icu_not_on_ventilator,
                   width=width, color=colors["icu_not_on_ventilator"],
                   bottom=sum(bottom), align="center",
                   alpha=1, label='In ICU, not on a ventilator')
            bottom.append(icu_not_on_ventilator)

            # ventilator
            # color db03fc
            ax.bar((theta * index), ventilator,
                   width=width, color=colors["ventilator"],
                   bottom=sum(bottom), align="center",
                   alpha=1, label='Ventilator')
            bottom.append(ventilator)

            # Deaths
            # Color fa054a red
            ax.bar((theta * index), death,
                   width=width, color=colors["death"],
                   bottom=sum(bottom), align="center",
                   alpha=1, label='Deaths')
            bottom.append(death)

            # Recovered
            # Color blue
            ax.bar((theta * index), recovered,
                   width=width, color=colors["recovered"],
                   bottom=sum(bottom), align="center",
                   alpha=1, label='Recovered')

    plt.xticks(fontsize=8)
    plt.xlabel("Days")
    plt.ylabel("Number of Cases")
    ax.set_xticks(np.arange(len(data_dict[state].keys())))
    ax.set_xticklabels((reversed(list(data_dict[state].keys()))), rotation=45)
    ax.set_title(state)
    ax.legend(loc=0)

    # After going through the days
    # Save the file to the git hub portfolio
    # plt.savefig(
    #     r"C:\Users\killa\Documents\GitHub\killascheuring.github.io\images\polar_graphs\%s_marker.svg" % country.lower().replace(
    #         " ", "_"), transparent=True)

    plt.show()

    bottom = []
    ax.remove()
    break
