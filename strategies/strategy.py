from log import Log
from indicators import Analysis
from paper_transact import Transaction
# from analysis import *

# API_KEY : "238eb5145d2e401fa10abe61737046bf"
# API_SECRET : "2f7b3b46ec9d424ab0b69d34d8eb1b3d"

class BotStrategy(object):
    def __init__(self):
        self.output = Log()
        self.transact = Transaction('BTC-TRIG')
        self.candle_history = []
        self.trade_history = []

        self.btc = 1
        self.coin = 0
        # self.open_trades = []

        self.open_trades = 0
        self.max_open_trades = 1

        self.prev_rsi = None

        self.indicators = Analysis()

    def main(self, candle):
        self.candle_history.append(candle)
        self.strategy()
        # print self.transact.ledger.ledger

    def strategy(self):
        



# Add profit tracking
# only allow one order, ie if the last order was a buy the next must be a sell
# restructure analysis, maybe move stuff there to a new indicators method
# fix logging
#