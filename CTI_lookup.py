import pandas as pd
import requests
from get_ip_report import get_ip_report

file_name = "IoC_API_Call.csv"
# 讀取 CSV 檔案
df = pd.read_csv(file_name).head(10)


# 對每個 IoC 執行 API 查詢並更新 API_Call_Result 欄位
for index, row in df.iterrows():
    if pd.notnull(row['IoC']):
        ip = row['IoC']
        result = get_ip_report(ip)
        df.at[index, 'API_Call_Result'] = result
        df.to_csv(file_name, index=False)
