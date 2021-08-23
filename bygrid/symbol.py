from bygrid.client import client


class Symbol(object):
    def __init__(self, name):
        self.name = name
        self.base_asset = None
        self.quote_asset = None
        self.tick_size = None  # minimum price precision in order
        self.step_size = None  # minimum quantity precision in order
        self.info = None

        self._query_info()

    def _query_info(self):
        response = client.exchange_info(self.name)
        self.info = response['symbols'][0]
        self.base_asset = self.info['baseAsset']
        self.quote_asset = self.info['quoteAsset']

        for i in self.info['filters']:
            if i['filterType'] == 'PRICE_FILTER':
                self.tick_size = float(i['tickSize'])
            if i['filterType'] == 'LOT_SIZE':
                self.step_size = float(i['stepSize'])

    @staticmethod
    def symbol_price(name):  # DOGEUSDT
        response = client.ticker_price(name)
        price = response['price']
        print('current price is ' + price)
        return float(price)
