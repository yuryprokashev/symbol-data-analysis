def price_tuple(strategy, symbol_candle_tuple):
    candle = symbol_candle_tuple[2]
    if candle["s"] != "ok":
        return symbol_candle_tuple[0], symbol_candle_tuple[1], []
    opn = candle["o"]
    close = candle["c"]
    high = candle["h"]
    low = candle["l"]
    return symbol_candle_tuple[0], symbol_candle_tuple[1], strategy(opn, close, low, high)


def median(open_array, close_array, low_array, high_array):
    result = []
    for i in range(len(low_array)):
        price = (low_array[i] + high_array[i]) / 2
        result.append(price)
    return result


def typical(open_array, close_array, low_array, high_array):
    result = []
    for i in range(len(low_array)):
        price = (low_array[i] + high_array[i] + close_array[i]) / 3
        result.append(price)
    return result


def weighted(open_array, close_array, low_array, high_array):
    result = []
    for i in range(len(low_array)):
        price = (low_array[i] + high_array[i] + open_array[i] + close_array[i]) / 4
        result.append(price)
    return result

