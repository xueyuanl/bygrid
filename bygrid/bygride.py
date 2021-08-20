import json
import os

from binance.spot import Spot


def main():
    client = Spot()
    print(client.time())

    client = Spot(key=os.environ['KEY'], secret=os.environ['SECRET'])

    # Get account information
    print(json.dumps(client.account()))

    # Post a new order
    params = {
        'symbol': 'DOGEUSDT',
        'side': 'BUY',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': 100,
        'price': 0.2
    }

    response = client.new_order(**params)
    #response = client.coin_info()
    print(json.dumps(response))


if __name__ == '__main__':
    main()
