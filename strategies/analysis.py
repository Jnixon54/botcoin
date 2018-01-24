from indicators import Analysis
from paper_transact import Transaction


class 

def rsi_strat():
    current_rsi = self.indicators.RSI(self.candle_history)
    # print str(self.candle_history[-1].get('C')) + str(current_rsi) + ' ' + str(self.prev_rsi) 

    if current_rsi > self.prev_rsi and current_rsi <= 30:
        if self.open_trades < self.max_open_trades:
            self.transact.buy((self.btc / self.candle_history[-1].get('C')), self.candle_history[-1].get('C'))
            self.open_trades += 1
            # self.btc = 0
            self.coin = (self.btc / self.candle_history[-1].get('C'))
            self.btc = 0

    if current_rsi < self.prev_rsi and current_rsi >= 70:
        if self.open_trades > 0:
            self.transact.sell(self.coin, self.candle_history[-1].get('C'))
            self.open_trades = 0
            self.btc = (self.coin * self.candle_history[-1].get('C'))
            self.coin = 0


    print 'Coin | BTC: ' + str(self.coin) + ' ' + str(self.btc)
            # self.coin = 0



    self.prev_rsi = current_rsi

def detect_exp_strat():


