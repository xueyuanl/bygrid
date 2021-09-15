from bygrid.client import client


class Order(object):
    def __init__(self, symbol, price, side, quantity):
        self.symbol_name = symbol
        self.price = price
        self.side = side  # buy or sell

        self.quantity = quantity
        self.order_id = None
        self.client_order_id = None
        self.status = None
        self.transact_time = None

    def post_order(self):
        params = {
            'symbol': self.symbol_name,
            'side': self.side,
            'type': 'LIMIT',
            'timeInForce': 'GTC',
            'quantity': self.quantity,
            'price': self.price
        }
        response = client.new_order(**params)
        return response
