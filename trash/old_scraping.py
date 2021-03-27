
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

ticker = 1458

# URLを定義
base_url = "https://kabuoji3.com/stock/{}/"
url = base_url.format(ticker)

# headersの設定
headers = {"User-Agent": "ご自身で設定してください"}

# HTML取得
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")

# 株価データ抽出
rows = []

for tr in soup.findAll("tr"):
    # thあればコラム、なければ株価データ
    if tr.find("th"):
        columns = [x.getText().strip() for x in tr.findAll("th")]
    else:
        rows.append([x.getText().strip() for x in tr.findAll("td")])

# DataFrameに変換
df_latest = pd.DataFrame(rows, columns=columns)

# 日付をdatetimeに変換
df_latest["日付"] = df_latest["日付"].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"))

# 日付以外のデータをfloatに変換
for col in ["始値", "高値", "安値", "終値", "出来高", "終値調整"]:
    df_latest[col] = df_latest[col].astype(float)

# "終値調整"を削除
df_latest.drop("終値調整", axis=1)
