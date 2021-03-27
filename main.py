import get_stock
import pandas as pd
from xlsxwriter import Workbook
from datetime import datetime,date

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

def main():

    start = datetime(2021,3,1)
    end = date.today()
    stock = '7203.JP'
    stock_data = get_stock.company(stock, start,end)
    #print(stock_data,name)

    #export to excel
    export_excel(stock_data,stock)

    #export to excel
    stock_graph(stock_data,stock)

def stock_graph(data,name):
    sns.set() #  コレ
    fig, ax = plt.subplots(figsize = (10,5))
    ax.plot(data['Date'],data['Open'])
    ax.set(xlabel ='Date',ylabel='Open',\
        ylim=(0,max(data['Open'])*1.2))

    from matplotlib import ticker
    ax.xaxis.set_major_locator(ticker.MultipleLocator(3))
    ax.xaxis.set_major_formatter(DateFormatter('%m-%d'))
#    plt.show()
    plt.savefig('./graph/'+name+'.png')

def export_excel(data,name):
    with pd.ExcelWriter('./data/stock_data.xlsx') as writer:
        data.to_excel(writer,sheet_name=name)

if __name__ == "__main__":
    main()
