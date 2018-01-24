import os
from bittrex.bittrex import Bittrex
import threading

API_KEY     = os.environ['BITTREX_KEY']
API_SECRET  = os.environ['BITTREX_SECRET']

marketPair = 'BTC-TRST'
# 1 = 100%
riskPercent = .07

class Trail(object):

    def __init__(self, marketPair, riskPercent):
        self.client = Bittrex(API_KEY, API_SECRET)
        self.marketPair = marketPair
        self.riskPercent = riskPercent
        self.tickerData = self.client.get_ticker(marketPair)
        self.currentPrice = self.tickerData.get('result').get('Last')
        self.highPrice = self.currentPrice
        self.priceDifference = 0
        self.limitPrice = round((self.currentPrice * (1 - self.riskPercent)), 8)


    def updateTickerData(self):
        client = Bittrex(API_KEY, API_SECRET)
        return client.get_ticker(marketPair)


    def updatePrice(self):
        self.currentPrice = self.updateTickerData().get('result').get('Last')
        
        if self.currentPrice > self.highPrice:
            self.highPrice = self.currentPrice
            self.limitPrice = round((self.currentPrice * (1 - self.riskPercent)), 8)
            print "The price has reached a new high of: " + str(self.highPrice)

        return self.currentPrice


    def updatePriceDifference(self):
        self.updatePrice()
        
        self.priceDifference = float((self.currentPrice/float(self.highPrice) - 1) * 100)

        return self.priceDifference
    

    def createSellOrder(self):
        self.balance = self.client.get_balance(marketPair.split('-')[1]).get('result').get('Available')
        self.client.sell_limit(marketPair, ((self.balance)*.5), self.currentPrice)
        print "Order to sell " + str(self.balance) + self.marketPair.split('-')[1] + " at " + str(self.currentPrice) + " satoshi created."


    def runTrail(self):
        self.updatePriceDifference()

        if self.currentPrice <= self.limitPrice:
            self.createSellOrder()
            self.terminate()

    def readOut(self):
        print ""
        print "Monitoring: " + self.marketPair
        print "|  Current   |    High    | Limit Price | Change  |  Risk  |"
        print "| {0:10} | {1:10} | {2:10}  | {3:7s} |  {4:4}% |".format(str(self.currentPrice), str(self.highPrice), str(self.limitPrice), str(round(self.priceDifference, 2)) + "%", str(self.riskPercent*100))

    def terminate(self):
        os._exit(0)
            

def runCode():
    threading.Timer(5.0, runCode).start()

    order.runTrail()
    order.readOut()


order = Trail(marketPair, riskPercent)

runCode()




