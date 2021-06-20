import requests


class FHub(object):
    def __init__(self, api_key):
        self.base_url = "https://finnhub.io/api/v1"
        self.api_key = api_key

    def request(self):
        return FHubRequestBuilder()

    def execute(self, request_array):
        result = []
        for request in request_array:
            request.base(self.base_url).api_key(self.api_key)
            response = get_one_symbol_candles(request)
            category = request.category_name
            symbol = request.symbol_name
            r = (category, symbol, response)
            result.append(r)
        return result


class FHubRequestBuilder(object):
    def __init__(self):
        self.resolutions = dict(DAY="D", HOUR="60", MINUTE="1")
        self.category_name = ""
        self.resolution_name = ""
        self.start_date = ""
        self.end_date = ""
        self.symbol_name = ""
        self.base_url = ""
        self.x_api_key = ""

    def category(self, category_name):
        self.category_name = category_name
        return self

    def resolution(self, resolution_name):
        self.resolution_name = self.resolutions[resolution_name]
        return self

    def start(self, start_date):
        self.start_date = start_date
        return self

    def end(self, end_date):
        self.end_date = end_date
        return self

    def symbol(self, symbol_name):
        self.symbol_name = symbol_name
        return self

    def base(self, base_url):
        self.base_url = base_url;
        return  self

    def api_key(self, api_key_string):
        self.x_api_key = api_key_string;
        return self


def get_one_symbol_candles(req):
    symbol_query = symbol_query_factory(req.symbol_name, req.start_date, req.end_date, req.resolution_name)
    symbol_url = "{}/{}/candle{}".format(req.base_url, req.category_name, symbol_query)
    signed_url = sign_fhub_url(symbol_url, req.x_api_key)
    stock_request = requests.get(signed_url)
    response = stock_request.json()
    return response


def sign_fhub_url(url, api_key):
    return url + "&token=" + api_key


def symbol_query_factory(symbol, start_date, end_date, resolution):
    query = "?"
    query += "symbol=" + symbol
    query += "&resolution=" + resolution
    query += "&from=" + f'{int(start_date.timestamp())}'
    query += "&to=" + f'{int(end_date.timestamp())}'
    return query
