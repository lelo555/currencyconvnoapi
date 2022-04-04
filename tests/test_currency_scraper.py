"""
This script is used to test methods
"""

from scrapper.currency_scrapper import currency_calculate,get_currency_rate

def test_currency_calculate():
    """This method is used to check type of output for currency_calculate method"""
    method_out=currency_calculate(rate_of_currency=14,amount_of_money=10)
    assert type(method_out)==float


def test_get_currency_rate():
    """This method is used to check type of output for get_currency_rate method"""
    method_out=get_currency_rate(currency_from='USD',currency_to='TRY')
    assert type(method_out)==float
