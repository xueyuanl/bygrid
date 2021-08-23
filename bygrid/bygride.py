from bygrid.gride import GridOrder
from bygrid.client import client
import json
def main():
    # Post a new order
    params = {
        'symbol': 'MATICUSDT',
        'side': 'BUY',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': 100,
        'price': 0.2
    }

    response = client.exchange_info('MATICUSDT')
    print(json.dumps(response))
    # response = client.coin_info()
    # response = client.ticker_price('DOGEUSDT')

    # print(json.dumps(response))

    grid_params = {
        'symbol': 'MATICUSDT',
        'upper_price': 5,
        'lower_price': 1,
        'grid_quantity': 5,
        'investment': 40
    }
    #grid_order = GridOrder(**grid_params)
    #grid_order.post_grid_order()

if __name__ == '__main__':
    main()
