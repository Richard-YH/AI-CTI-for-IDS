import pandas as pd
import json
import csv


df = pd.read_csv('CTI_lookup_result.csv')

IoC_values = df['IoC'].values
api_call_result_values = df['API_Call_Result'].values

# 因為 ram 太小，用 csv 寫效能較好
with open('CTI_lookup_result_with_new_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["IoC", "Country", "Reputation", "Harmless", "Malicious", "Suspicious", "Undetected", "Continent"])
    for i in range(api_call_result_values.shape[0]):
        print(i)
        api_call_result_values_json = json.loads(api_call_result_values[i])
        
        try:
            ioc = IoC_values[i]
            country = api_call_result_values_json['data']['attributes']['country']
            reputation = api_call_result_values_json['data']['attributes']['reputation']
            #last_analysis_date = api_call_result_values_json['data']['attributes']['last_analysis_date']
            harmless = api_call_result_values_json['data']['attributes']['last_analysis_stats']['harmless']
            malicious = api_call_result_values_json['data']['attributes']['last_analysis_stats']['malicious']
            suspicious = api_call_result_values_json['data']['attributes']['last_analysis_stats']['suspicious']
            undetected = api_call_result_values_json['data']['attributes']['last_analysis_stats']['undetected']
            continent = api_call_result_values_json['data']['attributes']['continent']
            

            writer.writerow([ioc, country, reputation, harmless, malicious, suspicious, undetected, continent])
        
        except Exception as e:
            print(f"Error on row {i}: {e}")
            continue
