import pandas as pd
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

# Days of reports to collect
days = [
    "03-09-2020",
    "03-10-2020",
    "03-11-2020",
    "03-12-2020",
    "03-13-2020",
    "03-14-2020",
    "03-15-2020",
    "03-16-2020",
    "03-17-2020",
    "03-18-2020",
    "03-19-2020",
    "03-20-2020",
    "03-21-2020",
    "03-22-2020",
    "03-23-2020",
    "03-24-2020",
    "03-25-2020",
    "03-26-2020",
    "03-27-2020",
    "03-28-2020",
    "03-29-2020",
    "03-30-2020",
    "03-31-2020",
    "04-01-2020",
    "04-02-2020",
    "04-03-2020",
    "04-04-2020",
    "04-05-2020",
    "04-06-2020",
    "04-07-2020",
    "04-08-2020",
    "04-09-2020",
]

data_url_template = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/" \
                    "csse_covid_19_data/" \
                    "csse_covid_19_daily_reports/"
# This dictionary is used to consolidate the data
# where the labels aren't consistent
names_dict = {
    'Mainland China': 'China',
    'China': 'China',
    'Macau': 'China',
    'South Korea': 'South Korea',
    'Korea, South': 'South Korea',
    'Republic of Korea': 'South Korea',
    'Italy': 'Italy',
    'Yemen': 'Yemen',
    'Iran': 'Iran',
    'Iran (Islamic Republic of)': 'Iran',
    'France': 'France',
    'Germany': 'Germany',
    'Spain': 'Spain',
    'Japan': 'Japan',
    'Switzerland': 'Switzerland',
    'UK': 'United Kingdom',
    'United Kingdom': 'United Kingdom',
    'Netherlands': 'Netherlands',
    'Belgium': 'Belgium',
    'Sweden': 'Sweden',
    'Norway': 'Norway',
    'Singapore': 'Singapore',
    'Hong Kong': 'Hong Kong',
    'Hong Kong SAR': 'Hong Kong',
    'Malaysia': 'Malaysia',
    'Bahrain': 'Bahrain',
    'Austria': 'Austria',
    'US': 'US',
    'Kuwait': 'Kuwait',
    'Iraq': 'Iraq',
    'Iceland': 'Iceland',
    'Thailand': 'Thailand',
    'Greece': 'Greece',
    'Taiwan': 'Taiwan',
    'Taiwan*': 'Taiwan',
    'Taipei and environs': 'Taiwan',
    'United Arab Emirates': 'United Arab Emirates',
    'India': 'India',
    'Australia': 'Australia',
    'Canada': 'Canada',
    'Denmark': 'Denmark',
    'San Marino': 'San Marino',
    'Lebanon': 'Lebanon',
    'Palestine': 'Palestine',
    'occupied Palestinian territory': 'Palestine',
    'West Bank and Gaza': 'Palestine',
    'Israel': 'Israel',
    'Portugal': 'Portugal',
    'Czech Republic': 'Czech Republic',
    'Ireland': 'Ireland',
    'Republic of Ireland': 'Ireland',
    'Vietnam': 'Vietnam',
    'Viet Nam': 'Vietnam',
    'Algeria': 'Algeria',
    'Oman': 'Oman',
    'Egypt': 'Egypt',
    'Finland': 'Finland',
    'Brazil': 'Brazil',
    'Ecuador': 'Ecuador',
    'Russia': 'Russia',
    'Russian Federation': 'Russia',
    'Croatia': 'Croatia',
    'Estonia': 'Estonia',
    'Azerbaijan': 'Azerbaijan',
    'Romania': 'Romania',
    'Argentina': 'Argentina',
    'Qatar': 'Qatar',
    'Slovenia': 'Slovenia',
    'Belarus': 'Belarus',
    'Mexico': 'Mexico',
    'Pakistan': 'Pakistan',
    'Philippines': 'Philippines',
    'French Guiana': 'French Guiana',
    'New Zealand': 'New Zealand',
    'Poland': 'Poland',
    'Saudi Arabia': 'Saudi Arabia',
    'Chile': 'Chile',
    'Georgia': 'Georgia',
    'Hungary': 'Hungary',
    'Indonesia': 'Indonesia',
    'Senegal': 'Senegal',
    'Bosnia and Herzegovina': 'Bosnia and Herzegovina',
    'Malta': 'Malta',
    'North Macedonia': 'Macedonia',
    'Saint Barthelemy': 'Saint Barthelemy',
    'Dominican Republic': 'Dominican Republic',
    'Luxembourg': 'Luxembourg',
    'Martinique': 'Martinique',
    'Morocco': 'Morocco',
    'Afghanistan': 'Afghanistan',
    'Andorra': 'Andorra',
    'Armenia': 'Armenia',
    'Bhutan': 'Bhutan',
    'Cambodia': 'Cambodia',
    'Cameroon': 'Cameroon',
    'Colombia': 'Colombia',
    'Costa Rica': 'Costa Rica',
    'Faroe Islands': 'Faroe Islands',
    'Gibraltar': 'Gibraltar',
    'Jordan': 'Jordan',
    'Latvia': 'Latvia',
    'Liechtenstein': 'Liechtenstein',
    'Lithuania': 'Lithuania',
    'Monaco': 'Monaco',
    'Nepal': 'Nepal',
    'Nigeria': 'Nigeria',
    'Peru': 'Peru',
    'Serbia': 'Serbia',
    'Slovakia': 'Slovakia',
    'South Africa': 'South Africa',
    'Sri Lanka': 'Sri Lanka',
    'Togo': 'Togo',
    'Tunisia': 'Tunisia',
    'Ukraine': 'Ukraine',
    'Vatican City': 'Vatican City',
    'Holy See': 'Vatican City',
    'Bulgaria': 'Bulgaria',
    'Maldives': 'Maldives',
    'Macao SAR': 'Macao',
    'Moldova': 'Moldova',
    'Republic of Moldova': 'Moldova',
    'St. Martin': 'Saint Martin',
    'Saint Martin': 'Saint Martin',
    'Bangladesh': 'Bangladesh',
    'Paraguay': 'Paraguay',
    'Albania': 'Albania',
    'Cyprus': 'Cyprus',
    'Brunei': 'Brunei',
    'Burkina Faso': 'Burkina Faso',
    'Mongolia': 'Mongolia',
    'Panama': 'Panama',
    'Czechia': 'Czech Republic',
    'Bolivia': 'Bolivia',
    'Honduras': 'Honduras',
    'Congo (Kinshasa)': 'Congo',
    'Republic of the Congo': 'Congo',
    'Congo (Brazzaville)': 'Congo',
    "Cote d'Ivoire": "Cote d'Ivoire",
    'Jamaica': 'Jamaica',
    'Reunion': 'Reunion',
    'Turkey': 'Turkey',
    'Cuba': 'Cuba',
    'Guyana': 'Guyana',
    'Kazakhstan': 'Kazakhstan',
    'Cayman Islands': 'Cayman Islands',
    'Guadeloupe': 'Guadeloupe',
    'Ethiopia': 'Ethiopia',
    'Sudan': 'Sudan',
    'Guinea': 'Guinea',
    'Antigua and Barbuda': 'Antigua and Barbuda',
    'Aruba': 'Aruba',
    'Kenya': 'Kenya',
    'Uruguay': 'Uruguay',
    'Ghana': 'Ghana',
    'Jersey': 'Channel Islands',
    'Channel Islands': 'Channel Islands',
    'Guernsey': 'Channel Islands',
    'Namibia': 'Namibia',
    'Seychelles': 'Seychelles',
    'Trinidad and Tobago': 'Trinidad and Tobago',
    'Venezuela': 'Venezuela',
    'Curacao': 'Curacao',
    'Eswatini': 'Eswatini',
    'Gabon': 'Gabon',
    'Guatemala': 'Guatemala',
    'Mauritania': 'Mauritania',
    'Rwanda': 'Rwanda',
    'Saint Lucia': 'Saint Lucia',
    'Saint Vincent and the Grenadines': 'Saint Vincent and the Grenadines',
    'Suriname': 'Suriname',
    'Kosovo': 'Kosovo',
    'Central African Republic': 'Central African Republic',
    'Equatorial Guinea': 'Equatorial Guinea',
    'Uzbekistan': 'Uzbekistan',
    'Guam': 'Guam',
    'Puerto Rico': 'Puerto Rico',
    'Benin': 'Benin',
    'Greenland': 'Greenland',
    'Liberia': 'Liberia',
    'Mayotte': 'Mayotte',
    'Somalia': 'Somalia',
    'Tanzania': 'Tanzania',
    'The Bahamas': 'Bahamas',
    'Bahamas, The': 'Bahamas',
    'Bahamas': 'Bahamas',
    'The Gambia': 'Gambia',
    'Gambia, The': 'Gambia',
    'Gambia': 'Gambia',
    'Western Sahara': 'Western Sahara',
    'Barbados': 'Barbados',
    'Montenegro': 'Montenegro',
    'Kyrgyzstan': 'Kyrgyzstan',
    'Mauritius': 'Mauritius',
    'Zambia': 'Zambia',
    'Djibouti': 'Djibouti',
    'Chad': 'Chad',
    'El Salvador': 'El Salvador',
    'Fiji': 'Fiji',
    'Nicaragua': 'Nicaragua',
    'Madagascar': 'Madagascar',
    'Haiti': 'Haiti',
    'Angola': 'Angola',
    'Cabo Verde': 'Cape Verde',
    'Cape Verde': 'Cape Verde',
    'Niger': 'Niger',
    'Papua New Guinea': 'Papua New Guinea',
    'Zimbabwe': 'Zimbabwe',
    'East Timor': 'Timor-Leste',
    'Timor-Leste': 'Timor-Leste',
    'Eritrea': 'Eritrea',
    'Uganda': 'Uganda',
    'Dominica': 'Dominica',
    'Grenada': 'Grenada',
    'Mozambique': 'Mozambique',
    'Syria': 'Syria',
    'Belize': 'Belize',
    'Laos': 'Laos',
    'Libya': 'Libya',
    'Guinea-Bissau': 'Guinea-Bissau',
    'Mali': 'Mali',
    'Saint Kitts and Nevis': 'Saint Kitts and Nevis',
    'Burma': 'Burma',
    'Botswana': 'Botswana',
    'Burundi': 'Burundi',
    'Sierra Leone': 'Sierra Leone',
    'Malawi': 'Malawi',
    'South Sudan': 'South Sudan',
    'Sao Tome and Principe': 'Sao Tome and Principe'
}

# initialize the dictionary to hold the data
# will have the countries as keys
# the values will be a list of dictionaries
# each element is a day of data for that country
data_dict = {}

# Loop through the days
for count, day in enumerate(days):
    # Get this day's data
    data = pd.read_csv(data_url_template + day + ".csv", error_bad_lines=False)

    print("Day:", day.split(".")[0])

    # Loop through the rows
    for index, item in data.iterrows():
        # Check if there is no data in this row
        if data["Confirmed"][index] == 0 and data["Deaths"][index] == 0 and data["Recovered"][index] == 0:
            continue

        # Check what the labeling style is
        if "Country/Region" in data.columns:
            # Check if this country in in the names dict
            if data["Country/Region"][index] in names_dict.keys():
                # If it is, check if it's in the data dict already
                if names_dict[data["Country/Region"][index]] in data_dict.keys():
                    # If it is, check if we're moved on to the next day yet
                    if len(data_dict[names_dict[data["Country/Region"][index]]]) == count + 1:
                        # if we're still on the same day, add the current results to the day
                        data_dict[names_dict[data["Country/Region"][index]]][count]["Confirmed"] += data["Confirmed"][
                            index]
                        data_dict[names_dict[data["Country/Region"][index]]][count]["Deaths"] += data["Deaths"][index]
                        data_dict[names_dict[data["Country/Region"][index]]][count]["Recovered"] += data["Recovered"][
                            index]
                    else:
                        # If we've moved on, add a new day to the countries list
                        data_dict[names_dict[data["Country/Region"][index]]].append({
                            "Confirmed": data["Confirmed"][index],
                            "Deaths": data["Deaths"][index],
                            "Recovered": data["Recovered"][index],
                            "Day": day
                        })
                else:
                    # If it isn't add this country to the data dict
                    data_dict.setdefault(names_dict[data["Country/Region"][index]], [{
                        "Confirmed": data["Confirmed"][index],
                        "Deaths": data["Deaths"][index],
                        "Recovered": data["Recovered"][index],
                        "Day": day
                    }])
        else:
            # Check if this country in in the names dict
            if data["Country_Region"][index] in names_dict.keys():
                # If it is, check if it's in the data dict already
                if names_dict[data["Country_Region"][index]] in data_dict.keys():
                    # If it is, check if we're moved on to the next day yet
                    if len(data_dict[names_dict[data["Country_Region"][index]]]) == count + 1:
                        # if we're still on the same day, add the current results to the day
                        data_dict[names_dict[data["Country_Region"][index]]][count]["Confirmed"] += data["Confirmed"][
                            index]
                        data_dict[names_dict[data["Country_Region"][index]]][count]["Deaths"] += data["Deaths"][index]
                        data_dict[names_dict[data["Country_Region"][index]]][count]["Recovered"] += data["Recovered"][
                            index]
                    else:
                        # If we've moved on, add a new day to the countries list
                        data_dict[names_dict[data["Country_Region"][index]]].append({
                            "Confirmed": data["Confirmed"][index],
                            "Deaths": data["Deaths"][index],
                            "Recovered": data["Recovered"][index],
                            "Day": day
                        })
                else:
                    # If it isn't add this country to the data dict
                    data_dict.setdefault(names_dict[data["Country_Region"][index]], [{
                        "Confirmed": data["Confirmed"][index],
                        "Deaths": data["Deaths"][index],
                        "Recovered": data["Recovered"][index],
                        "Day": day
                    }])

# Time to make the graphs!

# Polar stacked bar graphs for Google Maps Marker
# Loop through the countries
for country in data_dict:
    print("Country:", country)

    # set up plot
    ax = plt.subplot(projection='polar')

    # the positions and widths are proportional
    theta = ((np.pi * 2) / len(data_dict[country]))
    width = ((np.pi * 2) / len(data_dict[country]))

    # loop through all the days for this country
    for index, day in enumerate(data_dict[country]):
        # Colors from
        # https://www.colourlovers.com/palette/56122/Sweet_Lolly

        # Active
        # Active is the total confirmed cases minus the deaths and the recovered
        ax.bar((np.pi / 2) + (theta * index), day["Confirmed"] - day["Deaths"] - day["Recovered"], width=width,
               color='#FABE28', bottom=0.0, alpha=1)

        # Deaths
        # Deaths start on top of the actives
        ax.bar((np.pi / 2) + (theta * index), day["Deaths"], width=width, color='#FF003C',
               bottom=day["Confirmed"] - day["Deaths"] - day["Recovered"], alpha=1)

        # Recovered
        # Recovered starts on top of the deaths
        ax.bar((np.pi / 2) + (theta * index), day["Recovered"], width=width, color='#88C100',
               bottom=day["Confirmed"] - day["Recovered"], alpha=1)

    # After going through the days
    # Save the file to the git hub portfolio
    # plt.savefig(
    #     r"C:\Users\killa\Documents\GitHub\killascheuring.github.io\images\polar_graphs\%s_marker.svg" % country.lower().replace(
    #         " ", "_"), transparent=True)

    plt.savefig(
        "plots/%s_plot_axis.svg" % country.lower().replace(
            " ", "_"), transparent=True)
    # Since these will be used as google maps markers
    # The axes are removed
    plt.axis('off')

    plt.savefig(
        "plots/%s_plot_no_axis.svg" % country.lower().replace(
            " ", "_"), transparent=True)

    # plt.show()
    # Clear the plot for the next country
    ax.remove()
    break

# Cartesian stacked bar graph for Google Maps Info Windows
# loop through all the countries
for country in data_dict:
    print("Country:", country)
    ax = plt.subplot(111)

    # distance between the bars is consistent
    theta = 1
    width = 0.30

    # Empty list for the dates as labels
    labels = []
    # loop though the days
    for index, day in enumerate(data_dict[country]):
        # Colors from
        # https://www.colourlovers.com/palette/56122/Sweet_Lolly

        # Check if it's the last day
        if index < len(data_dict[country]) - 1:
            # If not don't add labels to the colors

            # Confirmed
            # Active is the total confirmed cases minus the deaths and the recovered
            ax.bar((theta * index), day["Confirmed"] - day["Deaths"] - day["Recovered"], width=width,
                   color='#FABE28', bottom=0.0, alpha=1)
            # Deaths
            # Deaths start on top of the actives
            ax.bar((theta * index), day["Deaths"], width=width, color='#FF003C',
                   bottom=day["Confirmed"] - day["Deaths"] - day["Recovered"], alpha=1)
            # Recovered
            # Recovered starts on top of the deaths
            ax.bar((theta * index), day["Recovered"], width=width, color='#88C100',
                   bottom=day["Confirmed"] - day["Recovered"], alpha=1)

            # Add this date to the label
            labels.append(day["Day"].split("-")[0] + "-" + day["Day"].split("-")[1])
        else:
            # If it is the last day add the labels to each color

            # Confirmed
            # Active is the total confirmed cases minus the deaths and the recovered
            ax.bar((theta * index), day["Confirmed"] - day["Deaths"] - day["Recovered"], width=width,
                   color='#FABE28', bottom=0.0, alpha=1, label='Active')
            # Deaths
            # Deaths start on top of the actives
            ax.bar((theta * index), day["Deaths"], width=width, color='#FF003C',
                   bottom=day["Confirmed"] - day["Deaths"] - day["Recovered"], alpha=1, label='Deaths')
            # Recovered
            # Recovered starts on top of the deaths
            ax.bar((theta * index), day["Recovered"], width=width, color='#88C100',
                   bottom=day["Confirmed"] - day["Recovered"], alpha=1, label='Recovered')

            # Add this date to the label
            labels.append(day["Day"].split("-")[0] + "-" + day["Day"].split("-")[1])

    # Style the plot
    plt.xticks(fontsize=8)
    plt.xlabel("Days")
    plt.ylabel("Number of Cases")
    ax.set_xticks(np.arange(len(data_dict[country])))
    ax.set_xticklabels(labels, rotation=45)
    ax.set_title(country)
    ax.legend(loc=1)

    # After going through the days
    # Save the file to the git hub portfolio
    # plt.savefig(
    #     r"C:\Users\killa\Documents\GitHub\killascheuring.github.io\images\bar_graphs\%s_plot.png" % country.lower().replace(
    #         " ", "_"), transparent=True)
    plt.show()

    # Clear the plot for the next country
    ax.remove()
    break
