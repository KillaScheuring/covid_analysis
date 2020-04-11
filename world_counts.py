import pandas as pd
from pprint import pprint

data_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/" \
           "csse_covid_19_data/" \
           "csse_covid_19_daily_reports/" \
           "04-10-2020.csv"
data = pd.read_csv(data_url, error_bad_lines=False)

region_code_url = "https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv"
region_code = pd.read_csv(region_code_url, error_bad_lines=False)

consolidated_data_dict = {}

consolidated_region_dict = {}
consolidated_sub_region_dict = {}

rows = "FIPS, Admin2, Province_State, Country_Region," \
       " Last_Update, " \
       "Lat, Long_, " \
       "Confirmed, Deaths, Recovered, Active, Combined_Key"
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

for index, item in data.iterrows():
    if data["Country_Region"][index] in names_dict.keys():
        if names_dict[data["Country_Region"][index]] in consolidated_data_dict.keys():
            consolidated_data_dict[names_dict[data["Country_Region"][index]]]["Confirmed"] += data["Confirmed"][index]
            consolidated_data_dict[names_dict[data["Country_Region"][index]]]["Deaths"] += data["Deaths"][index]
            consolidated_data_dict[names_dict[data["Country_Region"][index]]]["Recovered"] += data["Recovered"][index]
            consolidated_data_dict[names_dict[data["Country_Region"][index]]]["Active"] += data["Active"][index]
        else:
            consolidated_data_dict.setdefault(names_dict[data["Country_Region"][index]], {
                "Confirmed": data["Confirmed"][index],
                "Deaths": data["Deaths"][index],
                "Recovered": data["Recovered"][index],
                "Active": data["Active"][index]
            })

for country in consolidated_data_dict:
    not_active = consolidated_data_dict[country]["Deaths"] + consolidated_data_dict[country]["Recovered"]
    consolidated_data_dict[country].setdefault("Not Active", not_active)

for index, region in region_code.iterrows():
    if region_code["name"][index] in consolidated_data_dict.keys():
        if region_code["region"][index] in consolidated_region_dict.keys():
            consolidated_region_dict[region_code["region"][index]]["Confirmed"] += \
                consolidated_data_dict[region_code["name"][index]]["Confirmed"]
            consolidated_region_dict[region_code["region"][index]]["Deaths"] += \
                consolidated_data_dict[region_code["name"][index]]["Deaths"]
            consolidated_region_dict[region_code["region"][index]]["Recovered"] += \
                consolidated_data_dict[region_code["name"][index]]["Recovered"]
            consolidated_region_dict[region_code["region"][index]]["Active"] += \
                consolidated_data_dict[region_code["name"][index]]["Active"]
            consolidated_region_dict[region_code["region"][index]]["Not Active"] += \
                consolidated_data_dict[region_code["name"][index]]["Not Active"]
        else:
            consolidated_region_dict.setdefault(region_code["region"][index], {
                "Confirmed": consolidated_data_dict[region_code["name"][index]]["Confirmed"],
                "Deaths": consolidated_data_dict[region_code["name"][index]]["Deaths"],
                "Recovered": consolidated_data_dict[region_code["name"][index]]["Recovered"],
                "Active": consolidated_data_dict[region_code["name"][index]]["Active"],
                "Not Active": consolidated_data_dict[region_code["name"][index]]["Not Active"]
            })

        if region_code["sub-region"][index] in consolidated_region_dict.keys():
            consolidated_sub_region_dict[region_code["sub-region"][index]]["Confirmed"] += \
                consolidated_data_dict[region_code["name"][index]]["Confirmed"]
            consolidated_sub_region_dict[region_code["sub-region"][index]]["Deaths"] += \
                consolidated_data_dict[region_code["name"][index]]["Deaths"]
            consolidated_sub_region_dict[region_code["sub-region"][index]]["Recovered"] += \
                consolidated_data_dict[region_code["name"][index]]["Recovered"]
            consolidated_sub_region_dict[region_code["sub-region"][index]]["Active"] += \
                consolidated_data_dict[region_code["name"][index]]["Active"]
            consolidated_sub_region_dict[region_code["sub-region"][index]]["Not Active"] += \
                consolidated_data_dict[region_code["name"][index]]["Not Active"]
        else:
            consolidated_sub_region_dict.setdefault(region_code["sub-region"][index], {
                "Confirmed": consolidated_data_dict[region_code["name"][index]]["Confirmed"],
                "Deaths": consolidated_data_dict[region_code["name"][index]]["Deaths"],
                "Recovered": consolidated_data_dict[region_code["name"][index]]["Recovered"],
                "Active": consolidated_data_dict[region_code["name"][index]]["Active"],
                "Not Active": consolidated_data_dict[region_code["name"][index]]["Not Active"]
            })

collection_data_frame = pd.DataFrame.transpose(pd.DataFrame(consolidated_data_dict))
consolidated_region_frame = pd.DataFrame.transpose(pd.DataFrame(consolidated_region_dict))
consolidated_sub_region_frame = pd.DataFrame.transpose(pd.DataFrame(consolidated_sub_region_dict))

print(collection_data_frame)
print(consolidated_region_frame)
print(consolidated_sub_region_frame)

collection_data_frame.to_csv("consolidated_data.csv")
consolidated_region_frame.to_csv("consolidated_region.csv")
consolidated_sub_region_frame.to_csv("consolidated_sub_region.csv")
