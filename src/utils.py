import datetime
import json
import logging
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../info.log', "w")
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def hello() -> str:
    """Функция выводит приветствие в зависимости от настоящего времени"""
    logger.info("Начали обработку приветствия")
    time_now = datetime.datetime.now()
    if 5 < time_now.hour < 12:
        logger.info("Окончили обработку приветствия")
        return "Доброе утро"
    elif 12 < time_now.hour < 17:
        logger.info("Окончили обработку приветствия")
        return "Добрый день"
    if 17 < time_now.hour < 23:
        logger.info("Окончили обработку приветствия")
        return "Добрый вечер"
    else:
        logger.info("Окончили обработку приветствия")
        return "Доброй ночи"


def cards_filter(transaction: list) -> str | list[dict[str | Any, str | Any]]:
    """Функция выводит информацию по каждой карте"""
    logger.info("Начали сортировку информации по картам")
    cards = []
    for key in transaction:
        filters = {"Номер карты": key["Номер карты"],
                   "Сумма": abs(key["Сумма операции"]),
                   "Кэшбэк": round(abs(key["Сумма операции"]) / 100, 2)}
        for i, value in key.items():
            if value is None:
                filters[i] = "Нет информации"
        cards.append(filters)
    logger.info("Окончили сортировку информации по картам")
    return cards


print(cards_filter(""))


def top_transaction(transaction: list) -> list:
    """Функция выводит топ 5 транзакций"""
    logger.info("Начали обработку ТОП-5 транзакций")
    top_transaction = []
    for key in transaction:
        filters = {"Дата операции": key["Дата операции"][:10],
                   "Сумма": abs(key["Сумма операции"]),
                   "Категория": key["Категория"],
                   "Описание": key["Описание"]}
        for i, value in key.items():
            if value is None:
                filters[i] = "Нет информации"
        top_transaction.append(filters)
    logger.info("Окончили обработку информации ТОП-5 транзакций")
    return sorted(top_transaction, key=lambda x: x["Сумма"], reverse=True)[1:6]


def currency_rates() -> list:
    """Функция выводит курс валют для необходимой валюты из файла"""
    logger.info("Получаем информацию с файла о необходимой цены валюты")
    with open("../data/user_setings.json", "r") as file:
        reading = json.load(file)["user_currencies"]

    API_KEY = os.getenv("API_TOKEN")

    currency_rate = []
    logger.info("Производим запрос по API по небходимым валютам")
    for i in reading:
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={i}"

        headers = {"apikey": f"{API_KEY}"}

        response = requests.get(url, headers=headers)

        get_value = round(response.json()["rates"]["RUB"], 2)
        currency_rate.append(dict(Валюта=i, Цена=get_value))
        # status_code = response.status_code
    logger.info("Окончили сбор информации по валютам")
    return currency_rate


def cost_promotion() -> list:
    """Функция получает результаты по API цену акций"""
    logger.info("Получаем информацию с файла о необходимых цен на АКЦИИ")
    with open("../data/user_setings.json", "r") as file:
        reading = json.load(file)["user_stocks"]

        API_KEY = os.getenv("API_TOKEN_SP_SECOND")
        logger.info("Производим запрос по API")
        url = f"https://financialmodelingprep.com/api/v3/stock/list?apikey={API_KEY}"
        response = requests.get(url)

        data = response.json()
        stock_prices = []
        logger.info("Фильтруем список согласна необходимых данных")
        for i in data:
            for element in reading:
                if i["symbol"] == element:
                    stock_prices.append(dict(Акция=element, Цена=i["price"]))
        logger.info("Окончили сбор данных цен на АКЦИИ")
        return stock_prices
