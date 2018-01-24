from log import Log
from ledger import Ledger

class Transaction(object):

    def __init__(self, market, quantity = 0, rate = 0):
        self.log = Log()
        self.market = market
        self.quantity = quantity
        self.rate = rate
        self.ledger = Ledger(self.market)


    def buy(self, quantity, rate):
        self.ledger.record_transaction('BUY', quantity, rate)
        print('Purchased: ' + str(quantity) + self.market.split('-')[1] + 'at ' + str(rate))


    def sell(self, quantity, rate):
        self.ledger.record_transaction('SELL', quantity, rate)
        print('Sold: ' + str(quantity) + self.market.split('-')[1] + 'at ' + str(rate))

