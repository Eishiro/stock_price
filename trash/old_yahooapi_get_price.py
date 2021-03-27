#https://www.datasciencelearner.com/yahoo-finance-api-python/

import pandas as pd
import yfinance as yf
#git
#https://github.com/ranaroussi/yfinance

#pipl
#https://pypi.org/project/yfinance/

msft = yf.Ticker("MSFT")
print(msft)

data = pdr.get_data_yahoo("SPY",
                          start="2017-01-01",
                          end="2017-04-30")
print(data)

fb_yahoo = yf.download('FB',
                        start='2020-09-15',
                        end='2020-11-15',
                        progress=True)
print(fb_yahoo)
