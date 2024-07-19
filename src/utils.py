import datetime
import os
import json
import certifi
import requests
from dotenv import load_dotenv

from src.read_excel import read_excel_file

load_dotenv()


def hello() -> str:
    """Функция выводит приветствие в зависимости от насточщего времени"""
    time_now = datetime.datetime.now()
    if 5 < time_now.hour < 12:
        return "Доброе утро"
    elif 12 < time_now.hour < 17:
        return "Добрый день"
    if 17 < time_now.hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def cards_filter(transaction: list) -> list:
    """Функция выводит информацию по каждой карте"""
    cards = []
    for key in transaction:
        filters = {"Номер карты": key["Номер карты"],
                   "Сумма": abs(key["Сумма операции"]),
                   "Кэшбэк": round(abs(key["Сумма операции"]) / 100, 2)}
        for i, value in key.items():
            if value == None:
                filters[i] = "Нет информации"
        cards.append(filters)
    return cards


def top_transaction(transaction: list) -> list:
    """Функция выводит топ 5 транзакций"""
    top_transaction = []
    for key in transaction:
        filters = {"Дата операции": key["Дата операции"][:10],
                   "Сумма": abs(key["Сумма операции"]),
                   "Категория": key["Категория"],
                   "Описание": key["Описание"]}
        for i, value in key.items():
            if value == None:
                filters[i] = "Нет информации"
        top_transaction.append(filters)
    return sorted(top_transaction, key=lambda x: x["Сумма"], reverse=True)[1:6]


def currency_rates() -> list:
    """Функция выводит курс валют для необходимой валюты из файла"""
    with open("../data/user_setings.json", "r") as file:
        reading = json.load(file)["user_currencies"]
    API_KEY = os.getenv("API_TOKEN")

    currency_rate = []

    for i in reading:
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={i}"

        headers = {"apikey": f"{API_KEY}"}

        response = requests.get(url, headers=headers)

        get_value = round(response.json()["rates"]["RUB"], 2)
        currency_rate.append(dict(Валюта=i, Цена=get_value))
        # status_code = response.status_code

    # {"base": "EUR","date": "2024-07-18","rates": {"RUB": 96.621474},"success": true,"timestamp": 1721291536}
    # [{'Валюта': 'USD', 'Цена': 87.45}, {'Валюта': 'EUR', 'Цена': 95.22}]
    return currency_rate


def cost_promotion() -> list:
    with open("../data/user_setings.json", "r") as file:
        reading = json.load(file)["user_stocks"]
        url = f"https://financialmodelingprep.com/api/v3/stock/list?apikey=6f2HzBpYjOsKrtToEw4ClUylkGcM0YdN"
        response = requests.get(url)
        data = response.json()
        stock_proces = []
        for i in data:
            for element in reading:
                if i["symbol"] == element:
                    stock_proces.append(dict(Акция=element, Цена=i["price"]))
        return stock_proces


# print(currency_rates())

# transaction = read_excel_file("../data/operations.xlsx")
# print(top_transaction(transaction))

# transaction = read_excel_file("../data/operations.xlsx")
# print(cards_filter(transaction))
