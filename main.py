import fhub

import prices

import mean_reversion

import datetime

from_date = datetime.datetime(2021, 1, 1, 0, 0, 0, 0)
to_date = datetime.datetime(2021, 6, 20, 0, 0, 0, 0)

symbol_tuples = [
    ("stock", "BB"),
    ("stock", "CHKP"),
    ("stock", "CSCO"),
    ("stock", "CTXS"),
    ("stock", "CYBR"),
    ("stock", "FEYE"),
    ("stock", "FSCN1V"),
    ("crypto", "BINANCE:BNBEUR"),
    ("crypto", "BINANCE:HOTBNB")
]

# Getting data section
api_key = "borr5uvrh5rbk6e6nfr0"
api = fhub.FHub(api_key)

api_request_array = []
for s in symbol_tuples:
    category = s[0]
    symbol = s[1]
    r = api.request().category(category).symbol(symbol).start(from_date).end(to_date).resolution("DAY")
    api_request_array.append(r)
symbol_candle_tuples = api.execute(api_request_array)

symbol_price_tuples = []
strategy = prices.weighted
for response in symbol_candle_tuples:
    p_tuple = prices.price_tuple(strategy, response)
    symbol_price_tuples.append(p_tuple)

print(symbol_price_tuples)

symbol_adfuller_results = []
for sp in symbol_price_tuples:
    s_adfuller = mean_reversion.adfuller(sp)
    symbol_adfuller_results.append(s_adfuller)

print(symbol_adfuller_results)

symbol_hurst_results = []
for sp in symbol_price_tuples:
    s_hurst = mean_reversion.hurst(sp)
    symbol_hurst_results.append(s_hurst)
print(symbol_hurst_results)