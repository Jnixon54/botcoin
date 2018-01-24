class Analysis(object):
    def __init__(self):
        pass

    # def movingAverage(self, dataPoints, period):
    #     if len(data) > 1:
    #         return sum(dataPoints[-period:]) / float(len(dataPoints[-period:]))

    #Relative Strength Index  
    def RSI(self, candle_history, period=14):
        up = []
        down = []

        if len(candle_history) > period + 1:
            for candle in range(len(candle_history) - period, len(candle_history)):
                prev_close = candle_history[candle - 1].get('C')
                current_close = candle_history[candle].get('C')
                if current_close > prev_close:
                    up.append(current_close - prev_close)
                    down.append(0)
                if current_close < prev_close:
                    down.append(prev_close - current_close)
                    up.append(0)
                else:
                    up.append(0)
                    down.append(0)

            rs = (sum(up)/ period) / (sum(down) / period)
            rsi = 100 - (100 / (1 + rs))

            return rsi  
        