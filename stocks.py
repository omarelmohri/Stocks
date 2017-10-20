from sys import argv
from yahoo_finance import Share
from stocks.portfolio import Position
import os

os.system('clear')
print('\033[93m='*100)
print('%8s %5s %10s %10s %10s %10s %10s' % ('Stock'  , 'Qty' ,  'Unit cost'  , 'Total cost' ,  'Price'  ,  'Market Value'   ,  'Gain/Loss'))
#Stock   Qty   Unit cost   Total cost   Price    Value     Gain/Loss')
print('='*100, '\033[0m')  #=\033[0m

filename = "data/portfolio.txt"
txt = open(filename)
#print(type(txt))
rawdata = txt.read()

#loading the portfolio
loadedPositons = []
seperate = rawdata.split('\n') #seperate each ligne into a list entry
for ligne in seperate:
    values = ligne.split(',') #take a ligne and read the values in it
    if len(values)==3:
        loadedPositons.append(Position(values[0],int(values[1]),float(values[2])))
#        total_cost = float(values[1]) * float(values[2])
#        ticker = str(values[0])
#USE MULTIPLE ASSIGNEMENTS FOR LISTS
#        stk = Share(ticker)
#        price = float(stk.get_price())
#        total_value = price * float(values[1])
#        pcent_change = str(stk.get_percent_change())
#        print('%8s %5i %10.2f %10.2f %10.2f %10.2f \033[32m%8s\033[0m' % (str(values[0]), int(values[1]), float(values[2]), total_cost, price, total_value, pcent_change))
#print('\033[93m=\033[0m'*100)


#Printing the vales
for pt in loadedPositons:
    #print ('%8s %5i %10.2f %10.2f %10.2f %10.2f %8f' % pt.ticker, pt.qty, pt.price, pt.totalCost(), pt.currentPrice(), pt.marketValue(), pt.positionGain())
    print ('%8s %5i %10.2f %10.2f %10.2f %10.2f \033[32m%10.2f\033[0m' % (pt.ticker, pt.qty , pt.price, pt.totalCost(), pt.currentPrice(), pt.marketValue(), pt.positionGain()))

print('\033[93m=\033[0m'*100)

txt.close()



def printLine():
    pass
