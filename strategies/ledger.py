import os

class Ledger(object):
    def __init__(self, market):
        self.market = market
        self.ledger = []

    def record_transaction(self, t_type, quantity, rate):
        self.ledger.append({'t_type' : t_type, 'quantity' : quantity, 'rate' : rate})
        print len(self.ledger)

    def calc_return(self):
        initial_value = float(self.ledger[1].get('rate')) * float(self.ledger[1].get('quantity'))
        final_value = float(self.ledger[-1].get('rate')) * float(self.ledger[-1].get('quantity'))

        profit = (final_value / initial_value) * 100

        return [profit, initial_value, final_value]



