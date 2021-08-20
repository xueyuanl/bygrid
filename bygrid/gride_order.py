class GridOrder(object):
    """

    """

    def __init__(self, upper_price, lower_price, grid_quantity, investment, arithmetic=True):
        self.upper_limit_prise = upper_price
        self.lower_limit_price = lower_price
        self.grid_quantity = grid_quantity
        self.investment = investment  # quote asset number
        self.arithmetic = arithmetic  # arithmetic or geometric

    def preview_profit_per_grid(self):
        pass

    def get_total_profit(self):
        pass

    def get_grid_profit(self):
        pass
