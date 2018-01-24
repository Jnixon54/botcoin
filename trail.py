import os
from bittrex.bittrex import Bittrex
import threading

API_KEY     = os.environ['BITTREX_KEY']
API_SECRET  = os.environ['BITTREX_SECRET']

marketPair = 'BTC-SWIFT'
# 1 = 100%
riskPercent = .05

class Trail(object):

    def __init__(self, marketPair, riskPercent):
        self.client = Bittrex(API_KEY, API_SECRET)
        self.riskPercent = riskPercent
        self.tickerData = self.client.get_ticker(marketPair)
        self.currentPrice = self.tickerData.get('result').get('Last')
        self.highPrice = self.currentPrice
        self.priceDifference = 0
        self.limitPrice = self.currentPrice * (1 - self.riskPercent)


    def updateTickerData(self):
        client = Bittrex(API_KEY, API_SECRET)
        return client.get_ticker(marketPair)


    def updatePrice(self):
        self.currentPrice = self.updateTickerData().get('result').get('Last')
        
        if self.currentPrice > self.highPrice:
            self.highPrice = self.currentPrice
            self.limitPrice = self.currentPrice * (1 - self.riskPercent)
            print "New High"

        return self.currentPrice


    def updatePriceDifference(self):
        self.updatePrice()
        
        self.priceDifference = float((self.currentPrice/float(self.highPrice) - 1) * 100)

        return self.priceDifference
    

    def createSellOrder(self):
        self.balance = client.get_balance(marketPair.split('-')[1]).get('result').get('Available')
        self.client.sell_limit(marketPair, self.balance, self.limitPrice)


    def runTrail(self):
        self.updatePriceDifference()

        print "Current : " + str(self.currentPrice) + ' | ' + str(self.highPrice) + " :High"
        print "Change in price: " + str(self.priceDifference)
        print "Limit Price: " + str(self.limitPrice) + " | " + str(float((self.priceDifference * 100)/float((self.riskPercent) * 100)) * 100) + "%"


        if self.currentPrice <= self.limitPrice:
            self.createSellOrder()
            print "Sell!!! Sell!!! Sell!!!"
            exit()
            

order = Trail(marketPair, riskPercent)

def runCode():
    threading.Timer(5.0, runCode).start()
    order.runTrail()

runCode()
# print float(client.get_ticker('BTC-XRP').get('result').get('Last'))




