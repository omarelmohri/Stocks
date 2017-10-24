#!/Users/omarelmohri/.venvs/lpthw/bin/python

from sys import argv
from yahoo_finance import Share
from stocks.portfolio import Position
import os

def printLine(t1, t2, t3, t4, t5, t6, t7, t8):
    print(str(t1).center(10,' '), end='')
    print(str(t2).rjust(6,' '), end='')
    print(str(t3).rjust(10,' '), end='')
    print(str(t4).rjust(14,' '), end='')
    print(str(t5).rjust(10,' '), end='')
    print(str(t6).rjust(15,' '), end='')
    try:
        if float(t7)>0:
            print('\033[32m', end='')
            print(str(t7).rjust(12,' '), end='')
            print('\033[0m', end='')
        else:
            print('\033[31m', end='')
            print(str(t7).rjust(12,' '), end='')
            print('\033[0m', end='')
    except:
        print(str(t7).rjust(12,' '), end='')
    try:
        if float(t8.replace(',', ''))>0:
            print('\033[32m', end='')
            print(str(t8).rjust(14,' '), end='')
            print('\033[0m', end='')
        else:
            print('\033[31m', end='')
            print(str(t8).rjust(14,' '), end='')
            print('\033[0m', end='')
    except:
        print(str(t8).rjust(14,' '), end='')
    print('\n', end='')

#Loading data from the file
txt = open("data/portfolio.txt")
rawdata = txt.read()
txt.close()

#loading the portfolio
loadedPositons = []
seperate = rawdata.split('\n') #seperate each ligne into a list entry
for ligne in seperate:
    values = ligne.split(',') #take a ligne and read the values in it
    #print('...', end='')
    if len(values)==3:
        loadedPositons.append(Position(values[0],int(values[1]),float(values[2])))

#Framing
raws, col = os.popen('stty size', 'r').read().split()
col = int(col)
os.system('clear')
print('\033[93m='*col)
printLine('Stock', 'Qty', 'U. cost', 'Total cost', 'Price', 'Market Value',
                                                        'Day G/L', 'Gain/Loss')
print('='*(col-1), '\033[0m', end='')  #=\033[0m

#Printing the vales
totalC = 0
currentV = 0
dayG = 0
totalG = 0
for pt in loadedPositons:
    printLine(pt.ticker, pt.qty, '{:,.2f}'.format(pt.price),
    '{:,.2f}'.format(pt.totalCost()), '{:,.2f}'.format(pt.currentPrice()),
    '{:,.2f}'.format(pt.marketValue()), '{:+,.2f}'.format(pt.dayGain()),
    '{:+,.2f}'.format(pt.positionGain()))
    totalC += pt.totalCost()
    currentV += pt.marketValue()
    dayG += pt.dayGain()
    totalG += pt.positionGain()

print('\033[93m=\033[0m'*col)
printLine('Total', '', '', '{:,.2f}'.format(totalC), '',
'{:,.2f}'.format(currentV),'{:+,.2f}'.format(dayG),'{:+,.2f}'.format(totalG))
print('\033[93m=\033[0m'*col)
