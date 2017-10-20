from nose.tools import *
from stocks.portfolio import *
from stocks.portfolio import Position




def test_total():
    tkr = Position('YHOO',1,1)
    assert_equal(tkr.ticker,'YHOO')
    assert_equal(tkr.qty,1)
    assert_equal(tkr.price,1)
    assert_equal(tkr.total_cost(),float(1))
