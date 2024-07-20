import datetime
import logging
import re
from functools import wraps
from typing import Optional, Any

import pandas as pd
from dateutil.relativedelta import relativedelta

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../info.log', "w")
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def log(filename: Any = None) -> Any:
    """Декоратор логирует вызов функций-обработчиков и результаты их работы"""

    def my_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "w") as file:
                        file.write(str(result))
                return result
            except Exception as e:
                if filename is not None:
                    with open(filename, "w") as file:
                        file.write(f"Произошла ошибка {e}")

            return func(*args, **kwargs)

        return wrapper

    return my_decorator


@log("mylog.json")
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Функция выводит транзакции за последние 3 месяца из списка транзакций"""
    if date is None:
        date = datetime.datetime.now()
    else:
        date = datetime.datetime.strptime(date, "%d-%m-%Y %H:%M:%S")  # Форматирует дату по шаблону

    logger.info(f"Начали сортировку транзакций по категории: {category} за последние 3 месяца, начиная с {date}")

    start_date = date - relativedelta(months=3)

    new_list = []  # Новый список отсортированный по дате
    for i in transactions:
        str_time = datetime.datetime.strptime(i["Дата операции"], "%d.%m.%Y %H:%M:%S")

        # Сортируем список по заданной дате и категории
        if start_date <= str_time <= date and re.search(category, i["Категория"], flags=re.IGNORECASE):
            new_list.append(i)
        logger.info("Окончили сортировку транзакциям по категориям за последние 3 месяца")
        return new_list

#
# transaction = read_excel_file("../data/operations.xlsx")
# print(spending_by_category(transaction,"Супермаркеты", "31-03-2022 16:43:00"))
