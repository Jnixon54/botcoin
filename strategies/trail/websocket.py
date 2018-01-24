# import sys

# from twisted.python import log
# from twisted.internet import reactor
# log.startLogging(sys.stdout)

# from autobahn.twisted.websocket import WebSocketClientFactory
# factory = WebSocketClientFactory()
# factory.protocol = MyClientProtocol

# reactor.connectTCP("https://bittrex.com/Market/Index?MarketName=BTC-XVG", 80, factory)
# reactor.run()

import websocket
ws = websocket.WebSocket()
ws.connect("ws://bittrex.com/Market/Index?MarketName=BTC-XVG:80")