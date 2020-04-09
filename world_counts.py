import pandas as pd
from pprint import pprint

data_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/" \
           "csse_covid_19_data/" \
           "csse_covid_19_daily_reports/" \
           "04-07-2020.csv"
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

for index, item in data.iterrows():
    if data["Country_Region"][index] in consolidated_data_dict.keys():
        consolidated_data_dict[data["Country_Region"][index]]["Confirmed"] += data["Confirmed"][index]
        consolidated_data_dict[data["Country_Region"][index]]["Deaths"] += data["Deaths"][index]
        consolidated_data_dict[data["Country_Region"][index]]["Recovered"] += data["Recovered"][index]
        consolidated_data_dict[data["Country_Region"][index]]["Active"] += data["Active"][index]
    else:
        consolidated_data_dict.setdefault(data["Country_Region"][index], {
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
