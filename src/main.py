import datetime
import logging

from src.read_excel import read_excel_file
from src.utils import cards_filter, cost_promotion, currency_rates, hello, top_transaction

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../info.log', "w")
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def main(date: str) -> dict:
    """Функция сортирует транзакции за период и выводит словарь:
    Привествие, транзации, топ-5 операция, курс валют, стоимость акций"""
    logger.info("Начали обработку информации страницы Главная в JSON-формат")
    date_obj = datetime.datetime.strptime(date, "%d-%m-%Y %H:%M:%S")  # Форматирует дату по шаблону
    start_date = date_obj.replace(day=1, hour=0, minute=0, second=1)  # Задаем начальное значение фильтра

    read_file = read_excel_file("../data/operations.xlsx")  # Считываем данные с файла

    new_list = []  # Новый список отсортированный по дате
    for i in read_file:
        str_time = datetime.datetime.strptime(i["Дата операции"], "%d.%m.%Y %H:%M:%S")
        if start_date <= str_time <= date_obj:
            new_list.append(i)

    call_currency_rates = currency_rates()
    price_rub = currency_rates()[0]["Цена"]  # Отбираем цену рубля

    call_cost_promotion = cost_promotion()  # Переводим цену акций в рубли
    for key in call_cost_promotion:
        key["Цена"] = key.get("Цена") * price_rub

    answer_dict = {"Приветствие": hello(),
                   "Транзакции": cards_filter(new_list),
                   "Топ-5 операций:": top_transaction(new_list),
                   "Курс валют:": call_currency_rates,
                   "Стоимость акций:": call_cost_promotion}
    logger.info("Окончили обработку информации страницы Главная в JSON-формат")
    return answer_dict


# print(main("20-05-2020 22:20:32"))