import os

from binance.spot import Spot

client = Spot()
print(client.time())

client = Spot(key=os.environ['KEY'], secret=os.environ['SECRET'])
print(id(client))


# print(json.dumps(client.account()))
def symbol_price(symbol):  # DOGEUSDT
    response = client.ticker_price(symbol)
    return response['price']
