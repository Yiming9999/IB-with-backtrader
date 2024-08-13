import backtrader as bt
import datetime as dt

class TestStrategy(bt.Strategy):
    params = (
        ('ma_period', 15),
        ('stop_loss', 0.02),  # 2% stop loss
        ('take_profit', 0.05),  # 5% take profit
        ('risk_per_trade', 0.01),  # 1% of the account per trade
    )

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None
        self.sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.ma_period)
        self.trade_count = 0
        self.winning_trades = 0
        self.losing_trades = 0
        self.total_pnl = 0

    def log(self, txt, ts=None):
        ''' Logging function for this strategy'''
        ts = ts or self.datas[0].datetime.datetime(0)
        print(f'{ts}, {txt}')

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, Price: {order.executed.price:.2f}, Size: {order.executed.size:.2f}')
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:   
                self.log(f'SELL EXECUTED, Price: {order.executed.price:.2f}, Size: {order.executed.size:.2f}')
            self.bar_executed = len(self)
            self.trade_count += 1

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log(f'OPERATION PROFIT, GROSS: {trade.pnl:.2f}, NET: {trade.pnlcomm:.2f}')
        self.total_pnl += trade.pnlcomm

        if trade.pnlcomm > 0:
            self.winning_trades += 1
        else:
            self.losing_trades += 1

    def next(self):
        self.log(f'Close, {self.dataclose[0]:.2f}')

        if self.order:
            return

        # Calculate position size based on risk management
        account_value = self.broker.getvalue()
        risk_amount = account_value * self.params.risk_per_trade
        stop_loss_price = self.dataclose[0] * (1.0 - self.params.stop_loss)
        position_size = risk_amount / (self.dataclose[0] - stop_loss_price)

        if not self.position:
            if self.dataclose[0] > self.sma[0]:
                self.log(f'BUY CREATE @ MKT: {self.dataclose[0]:.2f}')
                self.order = self.buy(size=position_size)
        else:
            if self.dataclose[0] < self.sma[0]:
                self.log(f'SELL CREATE @ MKT: {self.dataclose[0]:.2f}')
                self.order = self.sell(size=self.position.size)

    def stop(self):
        # Calculate Sharpe Ratio
        returns = self.total_pnl / self.broker.getvalue()
        sharpe_ratio = (returns - 0.02) / (self.total_pnl / self.trade_count) if self.trade_count > 0 else 0

        print(f'\nStrategy Results:')
        print(f'Total Trades: {self.trade_count}')
        print(f'Winning Trades: {self.winning_trades}')
        print(f'Losing Trades: {self.losing_trades}')
        print(f'Net Profit: {self.total_pnl:.2f}')
        print(f'Sharpe Ratio: {sharpe_ratio:.2f}')