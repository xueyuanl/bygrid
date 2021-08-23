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
