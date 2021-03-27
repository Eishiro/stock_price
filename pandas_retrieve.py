import os
from datetime import datetime

import pandas_datareader.data as web
#https://pandas-datareader.readthedocs.io/en/latest/readers/index.html
'''
pandas_datareader.data.DataReader
(name=,	ティッカーシンボルを指定
data_source = fred, google や yahoo など
start = datetime 型で指定
end)
'''
#ダウ平均を取得する
df = web.DataReader("^DJI","yahoo",start="2021-03-01", end="2021-03-20")
print('ダウ平均価格')
print(df)

def get_toyota():
#TOYOTA株　トヨタの証券コードは7203
    symbol = '7203.JP'
    df_toyota = web.DataReader(symbol, 'stooq',start="2021-03-01", end="2021-03-20")
    print('TOYOTA株')
    df_toyota.head()

if __name__ == '__main__':
    df_toyota=get_toyota()
    df_toyota.to_csv("toyota.csv",)

from matplotlib import pyplot as plt
df_toyota.drop(['Volume','Adj Close'],axis=1).plot()
plt.tight_layout()
