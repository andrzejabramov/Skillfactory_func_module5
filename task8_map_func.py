prices_in_usd = [10, 20, 30, 40, 50]
exchange_rate = 0.85

prices_in_euro = list(map(lambda x: x * exchange_rate, prices_in_usd))


print(prices_in_euro)