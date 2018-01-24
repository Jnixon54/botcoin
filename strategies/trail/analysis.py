Class Analysis(object):
    def __init__(self):
        pass

    def movingAverage(self, dataPoints, period):
        if len(data) > 1:
            return sum(dataPoints[-period:]) / float(len(dataPoints[-period:]))