#https://python55.com/2020/10/13/python%e7%b0%a1%e5%8d%98%e3%81%ab%e6%a0%aa%e4%be%a1%e3%82%92%e5%8f%96%e5%be%97%e3%81%97%e3%81%a6%e5%8a%a0%e5%b7%a5%e3%81%99%e3%82%8b%e6%96%b9%e6%b3%95part1/
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime, timedelta, date
#import talib as ta

class StockData:
    def __init__(self, stock, start, end):
        self.stock_name = stock
        self.stock = web.DataReader(stock, 'stooq', start, end)#.reset_index()
        self.vola = False

    def add_vola(self):
        self.stock["Volatility"] = self.stock["High"] - self.stock["Low"]
        self.vola = True

    def print_data(self):
        print(self.stock_name)

    def get_data(self):
        return self.stock

    #def to_csv(self, data, name):
    #    date = date.today()
    #    data.to_csv('{name}_{date}.csv'.format(name,date),index=False)


def company(stock, start, end):
    sd = StockData(stock,start, end)
    sd.add_vola()
    data= sd.get_data()
    #sd.print_data()
    #print(data)
    ##save to csv
    data.to_csv("./data/"+stock+".csv")
    return data, stock


if __name__ == '__main__':
    start = "2021-03-01"#datetime(2020,8,26)
    end = date.today()

#to get one data
    #stock ='7203.JP' #toyota
    #data, name = company(stock, start, end)

        ##def in case not using def company
        #    toyota_df = StockData2(stock,start,end)
        #    df = toyota_df.get_data()
        #    print(df)
        #   df.to_csv("toyota.csv")

# to get several data together
    stock_dict = {'toyota':'7203.JP','softbank':'9984.JP'}
    data, name= [company(s,start,end) for s in stock_dict.values()]
    #the same as below
        #for s in stock_dict.values():
        #    company(s,start, end)
