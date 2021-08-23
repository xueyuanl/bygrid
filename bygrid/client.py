import json
import os

from binance.spot import Spot

client = Spot()
print(client.time())

client = Spot(key=os.environ['KEY'], secret=os.environ['SECRET'])
print(id(client))


# print(json.dumps(client.account()))
def symbol_price(symbol):  # DOGEUSDT
    response = client.ticker_price(symbol)
    price = response['price']
    print('current price is ' + price)
    return float(price)


def post_new_order_by_quantity(symbol, side, quantity, price, type_='LIMIT', time_in_force='GTC'):
    params = {
        'symbol': symbol,
        'side': side,
        'type': type_,
        'timeInForce': time_in_force,
        'quantity': quantity,
        'price': price
    }
    response = client.new_order(**params)
    print(json.dumps(response))


def post_new_order_by_quote_order_qty(symbol, side, quote_order_qty, price=None, type_='LIMIT', time_in_force='GTC'):
    params = {
        'symbol': symbol,
        'side': side,
        'type': type_,
        'timeInForce': time_in_force,
        'quoteOrderQty': quote_order_qty,
        'price': price
    }
    response = client.new_order(**params)
    print(json.dumps(response))


def cancel_order():
    pass
