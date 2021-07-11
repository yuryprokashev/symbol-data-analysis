import numpy as np
import statsmodels.tsa.stattools as stats
from hurst import compute_Hc
import statsmodels.api as sm


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
    if len(price_array) > 100:
        result = compute_Hc(price_array, kind="price", simplified=True)
    else:
        result = []
    return symbol_price_tuple[0], symbol_price_tuple[1], result


def half_life(symbol_price_tuple):
    """

    @param symbol_price_tuple:
    @return: a tuple where the first two elements are the same as in input tuple,
    while the third element is the half life and fourth element is Lambda
    """
    price_array = symbol_price_tuple[2]
    if len(price_array) == 0:
        return symbol_price_tuple[0], symbol_price_tuple[1], []
    dy = d_price(price_array)
    x = nd_array(range(0, len(price_array) - 1, 1))
    x_c = sm.add_constant(x)
    model = sm.OLS(dy, x_c)
    results = model.fit()
    # print(results.summary())
    # print(results.params)
    lam = results.params[1]
    hl = half_life_from_beta(lam)
    return symbol_price_tuple[0], symbol_price_tuple[1], hl, lam


def d_price(price_array):
    """
    @param price_array: normal 1-d list with prices of length N
    @return: 2D array of shape (N-1, 1) where values are deltas between adjacent prices
    """
    y = nd_array(price_array)
    y_lag = sm.tsa.add_lag(y, insert=False)
    y1 = y_lag[:, 0]
    y0 = y_lag[:, 1]
    dy = nd_array(np.subtract(y1, y0))
    return dy


def nd_array(array):
    a = np.array([array])
    return np.transpose(a)


def half_life_from_beta(beta):
    return - np.log(2) / beta
