import datetime
from typing import Optional
import pandas as pd
from dateutil.relativedelta import relativedelta

from src.read_excel import read_excel_file


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Функция выводит транзакции за последние 3 месяца из списка транзакций"""
    if date is None:
        date = datetime.datetime.now()
    else:
        date = datetime.datetime.strptime(date, "%d-%m-%Y %H:%M:%S")  # Форматирует дату по шаблону

    start_date = date - relativedelta(months=3)

    new_list = []  # Новый список отсортированный по дате
    for i in transactions:
        str_time = datetime.datetime.strptime(i["Дата операции"], "%d.%m.%Y %H:%M:%S")
        if start_date <= str_time <= date:
            new_list.append(i)

    return new_list


#transactions = read_excel_file("../data/operations.xlsx")
#print(spending_by_category(transactions, "Супермаркеты", "01-04-2019 10:20:49"))
