from bittrex.bittrex import Bitrrex
import transaction

API_KEY     = ['BITTREX_KEY']
API_SECRET  = ['BITTREX_SECRET']

client = Bittrex(API_KEY, API_SECRET)

market = ''
uuid = ''

def getOrderData(uuid):
    
    data = client.get_order(uuid)

    if data.get('success') == True:
        return data.get('result')

    else:
        return None

