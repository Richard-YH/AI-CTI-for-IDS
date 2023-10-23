import pandas as pd

df = pd.read_csv('netflow_label.csv')


ip_addresses = df[['source_address','destination_address']].stack().reset_index(drop=True)
unique_ips = ip_addresses.unique()

unique_ips_df = pd.DataFrame({'IoC': unique_ips, 'API_Call_Result': ''})
unique_ips_df.to_csv('IoC_API_Call.csv', index=False)
print(len(unique_ips))


