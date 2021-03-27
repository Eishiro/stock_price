import sys
import json
#https://pypi.org/project/yahoo-finance-api2/
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

from datetime import datetime
#old_time = datetime.utcfromtimestamp(old_date/1000)
#now_time = datetime.utcfromtimestamp(now_date/1000)

symbol = "MSFT"
my_share = share.Share(symbol)
symbol_data = None
# outputformat Dictionary
# {
#   'timestamp': [...],
#   'open': [...],
#   'high': [...],
#   'low': [...],
#   'close': [...],
#   'volume': [...]
# }

try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY, #retrieve DAY
                                          10,                           #
                                          share.FREQUENCY_TYPE_DAY,
                                          1)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)

print(symbol_data.keys())
#print("print historical price for "+ symbol)
#print(symbol_data)
print("-" *20)

print(symbol_data['timestamp'])
timestamp = datetime.utcfromtimestamp(symbol_data['timestamp']/1000)
print(timestamp)
