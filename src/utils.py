import datetime
import os

import requests
from dotenv import load_dotenv

from src.views import read_excel_file

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
                   "Сумма": key["Сумма операции"],
                   "Кэшбэк": key["Кэшбэк"]}
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
                   "Сумма": key["Сумма операции"],
                   "Категория": key["Категория"],
                   "Описание": key["Описание"]}
        for i, value in key.items():
            if value == None:
                filters[i] = "Нет информации"
        top_transaction.append(filters)
    return top_transaction


def currency_rates() ->list:
    """Функция выводит курс валют"""
    API_KEY = os.getenv("API_TOKEN")
    url_USD = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base=USD"
    url_EUR = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base=EUR"

    headers = {"apikey": f"{API_KEY}"}

    response_USD = {'success': True, 'timestamp': 1720199764, 'base': 'USD',
                                               'date': '2024-07-05',
                                               'rates': {'RUB': 89}}
    response_EUR = {'success': True, 'timestamp': 1720199764, 'base': 'USD',
                    'date': '2024-07-05',
                    'rates': {'RUB': 100}}

    #response = requests.get(url_USD, headers=headers)
    # status_code = response.status_code

    return round(response_USD["rates"]["RUB"]), round(response_EUR["rates"]["RUB"])

#### ОСТАНОВИЛСЯ НА ПОЛУЧЕНИЕ АПИ И СП500



print(currency_rates())
# transaction = read_excel_file("../data/operations.xlsx")
# print(top_transaction(transaction))

# transaction = read_excel_file("../data/operations.xlsx")
# print(cards_filter(transaction))
