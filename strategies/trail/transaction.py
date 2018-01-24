import os
from bittrex.bittrex import Bittrex

API_KEY     = ['BITTREX_KEY']
API_SECRET  = ['BITTREX_SECRET']

class Transaction(object):

    def __init__(self, market, quantity = 0, rate = 0):
        self.client = Bittrex(API_KEY, API_SECRET)
        self.market = market
        self.quantity = quantity
        self.rate = rate


    def createBuyOrder(self):

        orderData = self.client.buy_limit(self.market, self.quantity, self.rate)
        self.uuid = self.orderData.get('result').get('uuid')


    def createSellOrder(self):

        orderData = self.client.sell_limit(self.market, self.quantity, self.rate)
        self.uuid = self.orderData.get('result').get('uuid')


    def cancelBuyOrder(self):
        self.client.cancel(self.uuid)


    def cancelSellOrder(self):
        self.client.cancel(self.uuid)


    def verifyOrderCompletion(self):
        if self.client.get_order(self.uuid).get('result').get('IsOpen') == False:
            return True
        else:
            return False


