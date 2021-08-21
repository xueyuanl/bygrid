class Order(object):
    def __init__(self, symbol, price, quantity, side):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
        self.side = side  # buy or sell

        self.order_id = None
        self.status = None
        self.transact_time = None
