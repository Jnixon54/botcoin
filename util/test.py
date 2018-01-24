import os
from bittrex.bittrex import Bittrex

API_KEY     = os.environ['BITTREX_KEY']
API_SECRET  = os.environ['BITTREX_SECRET']

print API_KEY
print API_SECRET

client = Bittrex(API_KEY, API_SECRET)
print client.get_markets()
