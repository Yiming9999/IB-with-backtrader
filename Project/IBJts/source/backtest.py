import backtrader as bt

from atreyu_backtrader_api import IBData
from atreyu_backtrader_api import IBStore

from test_printer import TestPrinter
from test_strategy import TestStrategy

import datetime as dt
from datetime import datetime, date, time

cerebro = bt.Cerebro()

# Initial try with TestPrinter
# data = IBData(host='127.0.0.1', port = 7497, clientId=35,
#               name="GOOG",        # Data name
#               dataname='GOOG',    # Symbol name
#               secType='STK',      # SecurityType is STOCK
#               exchange='SMART',   # Trading exchange IB's SMART exchange
#               currency="USD",     # Currency of SecurityType
#               historical=True,
#               what='BID_ASK')     # Update this parameter to select data type

# cerebro.adddata(data)

# # Add the printer as a strategy
# cerebro.addstrategy(TestPrinter)

# cerebro.run()


# Try to run with a specific date range
# data = IBData(host='127.0.0.1', port = 7497, clientId=35,
#               name="GOOG",        # Data name
#               dataname='GOOG',    # Symbol name
#               secType='STK',      # SecurityType is STOCK
#               exchange='SMART',   # Trading exchange IB's SMART exchange
#               currency="USD",     # Currency of SecurityType
#               fromdate=dt.datetime(2016, 1, 1),
#               todate=dt.datetime(2018, 1, 1),
#               historical=True,
#               what='TRADES')    

# cerebro.adddata(data)

# # Add the printer as a strategy
# cerebro.addstrategy(TestPrinter)

# cerebro.run()


# Try to run a strategy
# goog_data = IBData(host='127.0.0.1', port = 7497, clientId=35,
#               name="GOOG_TRADES", # Data name
#               dataname='GOOG',    # Symbol name
#               secType='STK',      # SecurityType is STOCK
#               exchange='SMART',   # Trading exchange IB's SMART exchange
#               currency="USD",     # Currency of SecurityType
#               fromdate=dt.datetime(2016, 1, 1),
#               todate=dt.datetime(2018, 1, 1),
#               historical=True,
#               what='TRADES')

# cerebro.adddata(goog_data)

# apple_data = IBData(host='127.0.0.1', port = 7497, clientId=35,
#               name="AAPL_MIDPOINT", # Data name
#               dataname='AAPL',      # Symbol name
#               secType='STK',        # SecurityType is STOCK
#               exchange='SMART',     # Trading exchange IB's SMART exchange
#               currency="USD",       # Currency of SecurityType
#               fromdate=dt.datetime(2016, 1, 1),
#               todate=dt.datetime(2018, 1, 1),
#               historical=True,
#               what='MIDPOINT')

# cerebro.adddata(apple_data)

# # Add the test strategy
# cerebro.addstrategy(TestStrategy)

# # Set our desired cash start
# cerebro.broker.setcash(100000.0)

# cerebro.run()

# print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())


# Try to get the current data
data = IBData(host='127.0.0.1', port = 7497, clientId=35,
              name="AAPL",        # Data name
              dataname='AAPL',    # Symbol name
              secType='STK',      # SecurityType is STOCK
              exchange='SMART',   # Trading exchange IB's SMART exchange
              currency="USD",     # Currency of SecurityType
              fromdate=dt.datetime(2023, 8, 1),
              todate=dt.datetime(2024, 8, 1),
              historical=True)

cerebro.adddata(data)

# Set our desired cash start
cerebro.broker.setcash(100000.0)

# Add the test strategy
cerebro.addstrategy(TestStrategy)

# Add a fixedSize sizer according to the stake
cerebro.addsizer(bt.sizers.FixedSize, stake=10)

cerebro.run()

# Print out the final result
print(f'Final Portfolio Value: {cerebro.broker.getvalue():.2f}')


# # Now do the paper trading
# ibstore = IBStore(host='127.0.0.1',
#                   port=7497,
#                   clientId=1)

# data = ibstore.getdata(name="AAPL",        # Data name
#                        dataname='AAPL',    # Symbol name
#                        secType='STK',      # SecurityType is STOCK
#                        exchange='SMART',   # Trading exchange IB's SMART exchange
#                        currency="USD",     # Currency of SecurityType
#                        )

# cerebro.adddata(data)

# broker = ibstore.getbroker()

# # Set the broker
# cerebro.setbroker(broker)

# # Add the test strategy
# cerebro.addstrategy(TestStrategy)

# # Add a FixedSize sizer according to the stake
# cerebro.addsizer(bt.sizers.FixedSize, stake=10)

# cerebro.run()