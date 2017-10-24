from yahoo_finance import Share
import json


class Position(object):

    def __init__(self,ticker,qty,price,fee = 0):
        self.ticker = ticker
        self.qty = int(qty)
        self.price = float(price)
        self.fee = float(fee)
        self.yPointer = Share(self.ticker)
        self.name = self.yPointer.get_name()
        try:
            self.info = self.yPointer.get_info()
        except:
            self.info = ""

    def totalCost(self):
        tc = float(self.qty) * float(self.price)
        return tc

    def currentPrice(self):
        return float(self.yPointer.get_price())

    def marketValue(self):
        mV = (self.qty * float(self.yPointer.get_price())) + self.fee
        return mV

    def positionGain(self):
        diff = self.marketValue() - self.totalCost()
        return diff

    def dayGain(self):
        try:
            dg = self.qty * float(self.yPointer.get_change())
        except:
            dg = 0
        return dg

    def positionGainPercent(self):
        return (1 - self.totalCost()/self.marketValue())



#Get price from Yahoo
#stk = Share(ticker)
#price = float(stk.get_price())
#pcent_change = str(stk.get_percent_change())
