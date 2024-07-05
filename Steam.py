from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import json
import re
import pandas as pd

import requests

from RUB import get_currency_rates

import statistics
#url = "https://steamcommunity.com/market/listings/570/Dead%20Reckoning%20Chest"
url = 'https://steamcommunity.com/market/listings/570/Inscribed%20Demon%20Eater'



driver = webdriver.Edge()
driver.get(url)
time.sleep(5)

rs = requests.get(url)

m = re.search(r'var line1=(.+);', rs.text)

data_str = m.group(1)

data = json.loads(data_str)
#for i in data:
#    print(i)


def first_way(data):
    df = pd.DataFrame(data, columns=['date', 'price', 'volume'])
    
    # Preprocess the data
    df['date'] = df['date'].str.replace(': +0', '')
    df['date'] = pd.to_datetime(df['date'], format='%b %d %Y %H')
    df = df.set_index('date')
    
    # Calculate minimum and maximum prices for the last 6 months
    n_periods = 1000  # Number of days in 6 months
    min_price = df['price'][-n_periods:].min()
    max_price = df['price'][-n_periods:].max()
    
    
    mp = min_price + (min_price * 0.10)
    mx = max_price - (max_price * 0.10)
    print(f'Minimum price in the last 6 months: {min_price} USD')
    print(f'Maximum price in the last 6 months: {max_price} USD')
    print(f'-10% lower maximum price: {mx} USD')
    print(f'+10% lower minimum price: {mp} USD')
    
    mm = (mx - (mx * 0.13)) - mp
    print(f'mm value: {mm} USD')
    
    new_value = mp + mm
    
    percentage_difference = ((new_value - mp) / mp) * 100
    
    print(f'Percentage difference: {percentage_difference:.2f}%')
    
    currency_rates = get_currency_rates('USD',mm)
    price = currency_rates['RUB']
    print(f'Перевели: {mm} USD в',price,'RUB')
    
    pricess = [float(x[1]) for x in data]

    # вычисляем среднее значение цены
    avg_price = statistics.mean(pricess[-120:])

    print(f'Средняя цена:  {avg_price:.2f} USD ')

    # извлекаем количество проданных единиц товара из данных
    quantities = [float(x[2]) for x in data]

    # вычисляем среднее количество проданных единиц товара
    avg_quantity = statistics.mean(quantities)

    print(f'Среднее количество проданных единиц товара: {avg_quantity:.2f} USD ')
    
    
first_way(data)








