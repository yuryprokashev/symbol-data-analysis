import fhub

import prices

import mean_reversion

import datetime

import score

from_date = datetime.datetime(2021, 1, 1, 0, 0, 0, 0)
to_date = datetime.datetime(2021, 6, 20, 0, 0, 0, 0)
resolution = "HOUR"

symbol_tuples = [
    ("stock", "MSFT"),
    # ("stock", "BB"),
    # ("stock", "CHKP"),
    # ("stock", "CSCO"),
    # ("stock", "CTXS"),
    # ("stock", "CYBR"),
    # ("stock", "FEYE"),
    # ("stock", "FSCN1V"),
    # ("crypto", "BINANCE:BNBEUR"),
    # ("crypto", "BINANCE:HOTBNB"),
    # ("crypto", "BINANCE:DOTEUR"),
    # ("crypto", "BINANCE:RUNEBNB"),
    # ("crypto", "BINANCE:DOGEEUR")
]

# Getting data section
api_key = "borr5uvrh5rbk6e6nfr0"
api = fhub.FHub(api_key)

api_request_array = []
for s in symbol_tuples:
    category = s[0]
    symbol = s[1]
    r = api.request().category(category).symbol(symbol).start(from_date).end(to_date).resolution(resolution)
    api_request_array.append(r)
symbol_candle_tuples = api.execute(api_request_array)

print("PRICES")
symbol_price_tuples = []
strategy = prices.median
for response in symbol_candle_tuples:
    p_tuple = prices.price_tuple(strategy, response)
    symbol_price_tuples.append(p_tuple)
print(len(symbol_price_tuples[0][2]))
print(symbol_price_tuples)

print("ADFULLER")
symbol_adfuller_results = map(mean_reversion.adfuller, symbol_price_tuples)
symbol_adf = list(symbol_adfuller_results)
print(symbol_adf)
symbol_adf_scores = map(score.adf_score, symbol_adf)
symbol_adf_s = list(symbol_adf_scores)
print(symbol_adf_s)

print("HURST")
symbol_hurst_results = map(mean_reversion.hurst, symbol_price_tuples)
symbol_h = list(symbol_hurst_results)
symbol_hurst_score = map(score.hurst_score, symbol_h)
print(symbol_h)
print(list(symbol_hurst_score))

print("HALF LIFE")
symbol_half_life_results = map(mean_reversion.half_life, symbol_price_tuples)
print(list(symbol_half_life_results))
