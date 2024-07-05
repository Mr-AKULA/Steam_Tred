Steam Price Analyzer
===================

This tool analyzes the price history of items on the Steam marketplace and provides various statistics, such as minimum and maximum prices, average prices, and percentage differences. It also converts prices to Russian rubles using the latest exchange rate.

Usage
-----

To use the tool, run the `steam.py` script with the item name as a command-line argument. For example:
```
python steam.py "Dota 2"
```
The script will fetch the price history data for the specified item and display the following information:

* Minimum price in the last 6 months
* Maximum price in the last 6 months
* -10% lower maximum price
* +10% higher minimum price
* MM value (the difference between the maximum and minimum prices)
* Percentage difference between the maximum and minimum prices
* The average price of the item
* The average quantity of items sold

The prices will be displayed in USD and converted to Russian rubles using the latest exchange rate.

Note: The tool currently supports only Dota 2 items.

Requirements
------------

The tool requires the following Python libraries:

* requests
* pandas
* numpy
* statistics
* Selenium 

You can install these libraries using pip:
```
pip install requests pandas numpy statistics
```
License
-------

This tool is licensed under the MIT License. See the `LICENSE` file for details.

---

Steam Price Analyzer
===================

Этот инструмент анализирует историю цен товаров на торговой площадке Steam и предоставляет различную статистику, такую как минимальные и максимальные цены, средние цены и процентные разницы. Он также конвертирует цены в российские рубли по последнему курсу валют.

Использование
-----

Чтобы использовать инструмент, запустите скрипт `steam.py` с именем товара в качестве аргумента командной строки. Например:
```
python steam.py "Dota 2"
```
Скрипт извлечет данные историю цен для указанного товара и отобразит следующую информацию:

* Минимальная цена за последние 6 месяцев
* Максимальная цена за последние 6 месяцев
* -10% от максимальной цены
* +10% от минимальной цены
* Значение ММ (разница между максимальной и минимальной ценами)
* Процентная разница между максимальной и минимальной ценами
* Средняя цена товара
* Среднее количество проданных единиц товара

Цены будут отображаться в USD и конвертироваться в российские рубли по последнему курсу валют.

Обратите внимание: в настоящее время инструмент поддерживает только товары Dota 2.

Требования
------------

Инструменту требуются следующие библиотеки Python:

* requests
* pandas
* numpy
* statistics

Вы можете установить эти библиотеки с помощью pip:
```
pip install requests pandas numpy statistics
```
Лицензия
-------

Этот инструмент распространяется под лицензией MIT. Смотрите файл `LICENSE` для подробностей.
