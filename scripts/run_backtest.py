import pandas as pd
import backtrader as bt
import matplotlib.pyplot as plt

class SmaCross(bt.Strategy):
    def __init__(self):
        sma1 = bt.indicators.SimpleMovingAverage(self.data.close, period=10)
        sma2 = bt.indicators.SimpleMovingAverage(self.data.close, period=30)
        self.crossover = bt.indicators.CrossOver(sma1, sma2)

    def next(self):
        if self.crossover > 0:
            self.buy()
        elif self.crossover < 0:
            self.sell()

# Load the data
data = pd.read_csv('data/CRM.csv', index_col='Date', parse_dates=True)

# Initialize the backtester
cerebro = bt.Cerebro()

# Convert the DataFrame to Backtrader's data feed format
data_feed = bt.feeds.PandasData(dataname=data)

# Add the data feed to the backtester
cerebro.adddata(data_feed)

# Add the trading strategy to the backtester
cerebro.addstrategy(SmaCross)

# Set the initial cash
cerebro.broker.setcash(10000.0)

# Set the commission (0.1% per trade)
cerebro.broker.setcommission(commission=0.001)

# Run the backtest
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Ensure the plot displays correctly
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['figure.dpi'] = 100

# Plot the results
cerebro.plot(iplot=False, volume=False)
