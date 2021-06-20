import statsmodels.tsa.stattools as stats
from hurst import compute_Hc


def adfuller(symbol_price_tuple):
    """
    @param symbol_price_tuple: a tuple, where first element is symbol category,
    second element is the symbol itself, third element is the price array of the symbol
    @return: a tuple where the first two elements are the same as in input tuple,
    while the third element is the result of the adfuller function
    """
    price_array = symbol_price_tuple[2]
    if len(price_array) > 0:
        result = stats.adfuller(price_array)
    else:
        result = []
    return symbol_price_tuple[0], symbol_price_tuple[1], result


def hurst(symbol_price_tuple):
    """
    @param symbol_price_tuple: a tuple, where first element is symbol category,
    second element is the symbol itself, third element is the price array of the symbol
    @return: a tuple where the first two elements are the same as in input tuple,
    while the third element is the result of the hurst function
    """
    price_array = symbol_price_tuple[2]
    if len(price_array) > 0:
        result = compute_Hc(price_array, kind="price", simplified=True)
    else:
        result = []
    return symbol_price_tuple[0], symbol_price_tuple[1], result
