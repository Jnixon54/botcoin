import json
import urllib

from indicators import Analysis
from strategy import BotStrategy

def load_backtest_from_url(market, period):
    url = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=' + market + '&tickInterval=' + period + '&_=1499127220008'
    print url
    response = urllib.urlopen(url)
    hist_data = json.load(response)
    return hist_data

def load_backtest_from_file(filename):
    with open(filename) as data_file:
        hist_data = json.load(data_file)
    return hist_data

# print(hist_data)
def run_test(json_data):

    bot = BotStrategy()

    for candle in json_data.get('result'):
        # print "Open: " + str(candle.get('O')) + " Close: " + str(candle.get('C'))
        bot.main(candle)
    print bot.transact.ledger.ledger
    print bot.transact.ledger.calc_return()


run_test(load_backtest_from_file('BTC-TRIG-Thirty.json'))
# run_test(load_backtest_from_url('BTC-TRIG', 'fiveMin'))