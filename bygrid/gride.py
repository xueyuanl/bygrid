from bygrid.client import symbol_price


class GridOrder(object):
    """

    """

    def __init__(self, symbol, upper_price, lower_price, grid_quantity, investment, arithmetic=True):
        self.symbol = symbol
        self.upper_limit_prise = upper_price
        self.lower_limit_price = lower_price
        self.grid_quantity = grid_quantity
        self.investment = investment  # quote asset number
        self.arithmetic = arithmetic  # arithmetic or geometric
        self.interval = self._calculate_interval(upper_price, lower_price, grid_quantity)
        self.txs = 0

        self.order_list = None

    def preview_profit_per_grid(self):
        pass

    def get_total_profit(self):
        pass

    def get_grid_profit(self):
        pass

    @staticmethod
    def _calculate_interval(up, low, num):
        interval = (up - low) / (num - 1)
        return interval

    def _generate_order_list(self):
        price = symbol_price(self.symbol)
