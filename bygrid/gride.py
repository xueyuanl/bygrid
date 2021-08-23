from bygrid.client import client
from bygrid.order import Order
from bygrid.symbol import Symbol
from bygrid.utils import get_decimal_precision,format_decimal

class GridOrder(object):
    """

    """

    def __init__(self, symbol_name, upper_price, lower_price, grid_quantity, investment, arithmetic=True):
        self.symbol = Symbol(symbol_name)
        self.upper_limit_prise = upper_price
        self.lower_limit_price = lower_price
        self.grid_quantity = grid_quantity
        self.total_investment = investment  # quote asset number

        self.arithmetic = arithmetic  # arithmetic or geometric
        self.txs = 0

        self._init_price = Symbol.symbol_price(self.symbol.name)
        self.price_interval = self._calculate_interval(upper_price, lower_price, grid_quantity)
        self._price_list = self._generate_price_list()

        self._each_grid_investment = self.total_investment / (self.grid_quantity - 1)
        self.buy_order_list = self._generate_buy_order_list()
        self.init_sell_order_number = self.grid_quantity - len(self.buy_order_list) - 1
        self.sel_order_list = None  # will be generated after buy initial base asset

        self._init_quote_investment = self._each_grid_investment * len(self.buy_order_list)
        self._init_base_investment = self.total_investment - self._init_quote_investment
        self._init_base_quantity = None

    def post_grid_order(self):
        # post buy order
        self._post_buy_order_list()

        # buy base asset
        response = self._buy_base_asset()
        self._init_base_quantity = float(response['executedQty'])
        self.sel_order_list = self._generate_sell_order_list()

        # post sell order
        self._post_sell_order_list()

    def _post_buy_order_list(self):
        print('post buy order list')
        for i in self.buy_order_list:
            params = {
                'symbol': self.symbol.name,
                'side': 'BUY',
                'type': 'LIMIT',
                'timeInForce': 'GTC',
                'quantity': i.quantity,
                'price': i.price
            }
            response = client.new_order(**params)
            print(response)
            i.order_id = response['orderId']
            i.client_order_id = response['clientOrderId']
            i.transact_time = response['transactTime']

    def _post_sell_order_list(self):
        print('post sell order list')
        for i in self.sel_order_list:
            params = {
                'symbol': self.symbol.name,
                'side': 'SELL',
                'type': 'LIMIT',
                'timeInForce': 'GTC',
                'quantity': i.quantity,
                'price': i.price
            }
            response = client.new_order(**params)
            print(response)
            i.order_id = response['orderId']
            i.client_order_id = response['clientOrderId']
            i.transact_time = response['transactTime']

    def cancel_grid_order(self):
        pass

    def _buy_base_asset(self):
        params = {
            'symbol': self.symbol.name,
            'side': 'BUY',
            'type': 'MARKET',
            'quoteOrderQty': self._init_base_investment
        }
        response = client.new_order(**params)
        print(response)
        return response

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

    def _generate_price_list(self):
        price_list = []
        price_list.append(self.lower_limit_price)
        for i in range(1, self.grid_quantity - 1):
            price_list.append(price_list[-1] + self.price_interval)
        price_list.append(self.upper_limit_prise)
        return price_list

    def _calculate_init_quote_quantity(self):
        quote_q = self.total_investment / (self.grid_quantity - 1) * len(self.buy_order_list)
        return quote_q

    def _calculate_init_base_quantity(self):
        pass

    def _generate_buy_order_list(self):

        order_list = []
        # create buy list
        for i in self._price_list:
            if i < self._init_price:
                order = Order(self.symbol.name, i, 'BUY', self._each_grid_investment / i)
                order_list.append(order)
            else:
                break
        return order_list

    def _generate_sell_order_list(self):

        def get_sell_quantity_list(iq, num, step):
            precision = get_decimal_precision(step)
            # "{:.{}f}".format(pi, precision)
            each_order_quantity = format_decimal(iq / num, precision)
            sell_list = []
            for j in range(1, num):
                sell_list.append(each_order_quantity)
                iq -= each_order_quantity
            sell_list.append(format_decimal(iq, precision))
            return sell_list

        sell_quantity_list = get_sell_quantity_list(self._init_base_quantity, self.init_sell_order_number,
                                                    self.symbol.step_size)
        # create sell list
        order_list = []
        for i in reversed(self._price_list[-self.init_sell_order_number:]):
            order = Order(self.symbol.name, i, 'SELL', sell_quantity_list.pop())
            order_list.append(order)
        return order_list
