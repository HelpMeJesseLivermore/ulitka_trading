from core.ulitka_connector import connector
import time

eth_window = []

while True:

    # получить eth kline (фьючерсы)
    eth_price = connector.get_eth()
    # получить btc kline (спот)
    btc_price = connector.get_btc()

    # получить изменение цены за последнюю минуту в eth
    eth_delta_price_value = eth_price[1] - eth_price[0]  # на сколько в долларах изменилась цена eth
    eth_delta_price_percent = (eth_delta_price_value / eth_price[1]) * 100  # на сколько в процентах изменилась цена eth
    # получить изменение цены за последнюю минуту в btc
    btc_delta_price_value = btc_price[1] - btc_price[0]  # на сколько в долларах изменилась цена btc
    btc_delta_price_percent = (btc_delta_price_value / btc_price[1]) * 100  # на сколько в процентах изменилась цена btc

    # если цена eth изменилась в ту же сторону, то
    if (eth_delta_price_percent != 0) and (btc_delta_price_percent != 0):
        # в какую сторону двигались
        if (eth_delta_price_percent > 0) and (btc_delta_price_percent > 0):
            eth_delta_price_percent -= btc_delta_price_percent
            eth_delta_price_value = (eth_price[1] / 100) * eth_delta_price_percent
            eth_price[1] -= abs(eth_delta_price_value)

        if (eth_delta_price_percent < 0) and (btc_delta_price_percent < 0):
            eth_delta_price_percent += abs(btc_delta_price_percent)
            eth_delta_price_value = (eth_price[1] / 100) * eth_delta_price_percent
            eth_price[1] += abs(eth_delta_price_value)

    eth_window.append(eth_price[1])
    # если окно больше часа то удаляем
    if len(eth_window) > 60:
        eth_window = eth_window[-60:]

    eth_window_delta_price_value = eth_window[0] - eth_window[-1]  # на сколько в долларах изменилась цена eth
    eth_window_delta_price_percent = (eth_window_delta_price_value / eth_window[-1]) * 100  # на сколько в процентах изменилась цена eth
    
    if abs(eth_window_delta_price_percent) > 1:
        print(f'Цена ETH Futures изменилась на {eth_window_delta_price_percent} процентов')

    time.sleep(60)






