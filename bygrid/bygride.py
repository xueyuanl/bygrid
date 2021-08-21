import json

from bygrid.client import client


def main():
    # Post a new order
    params = {
        'symbol': 'DOGEUSDT',
        'side': 'BUY',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': 100,
        'price': 0.2
    }

    # response = client.new_order(**params)
    # response = client.coin_info()
    response = client.ticker_price('DOGEUSDT')
    print(json.dumps(response))


if __name__ == '__main__':
    main()
