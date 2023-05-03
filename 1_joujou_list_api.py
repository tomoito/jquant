from get_tokens2 import get_tokens2
import requests
import pandas as pd
import jquantsapi
from datetime import datetime, timedelta
from requests import HTTPError
import json

id_token = get_tokens2()
print(id_token)
cli = jquantsapi.Client(refresh_token=id_token)


# J-Quants API から取得するデータの期間
start_dt: datetime = datetime(2021, 4, 29)
end_dt: datetime = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
start_dt_yyyymmdd = start_dt.strftime("%Y%m%d")
end_dt_yyyymmdd = end_dt.strftime("%Y%m%d")

# # 銘柄一覧
# stock_list_load: pd.DataFrame = cli.get_list()

# # 株価情報 開始から終了まで全て
# stock_price_load: pd.DataFrame = cli.get_price_range(start_dt=start_dt, end_dt=end_dt)

# # 株価情報 取引日指定Ver
# d = datetime.now() 
# df_quotes_bydate = cli.get_prices_daily_quotes(date_yyyymmdd=d.strftime(format="%Y%m%d"))

# # 株式銘柄コード指定Ver
# df_quotes_bycode = cli.get_prices_daily_quotes(code=8697)


# 財務情報全て
stock_fin_load: pd.DataFrame = cli.get_statements_range(start_dt=start_dt, end_dt=end_dt)

# LocalCodeが7777のデータを絞り込む
# filtered_data = stock_fin_load[stock_fin_load['LocalCode'] == 6616]

# カラムを絞る
selected_columns = [
    'DisclosedDate',
    'LocalCode',
    'TypeOfDocument',
    'TypeOfCurrentPeriod',
    'CurrentPeriodStartDate',
    'CurrentPeriodEndDate',
    'NetSales',
    'OperatingProfit',
    'ForecastNetSales',
    'ForecastOperatingProfit',
    'NextYearForecastNetSales',
    'NextYearForecastOperatingProfit'
]
filtered_data = stock_fin_load[selected_columns]


# 財務情報　code指定
df_fins = cli.get_fins_statements(code=8697)

# 信用取引週末残高を日付範囲を指定して取得
df_weekly_margin: pd.DataFrame=cli.get_weekly_margin_range(start_dt=start_dt, end_dt=end_dt)



# # 大容量データが返却された場合の再検索
# # データ量により複数ページ取得できる場合があるため、pagination_keyが含まれる限り、再検索を実施
# while "pagination_key" in r_get.json():
#     pagination_key = r_get.json()["pagination_key"]
#     r_get = requests.get(f"https://api.jquants.com/v1/method?query=param&pagination_key={pagination_key}", headers=headers)
#     data += r_get.json()["data"]
    

# print(data)