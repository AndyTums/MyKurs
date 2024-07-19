import re

from src.read_excel import read_excel_file


def filter_numbers(transaction: list) -> list:
    """Функция фильтрует список по номеру телефона в описании"""
    new_list_filter = []
    for i in transaction:
        if "Описание" in i and re.findall(r"((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}", i["Описание"],
                                          flags=re.IGNORECASE):
            new_list_filter.append(i)
    return new_list_filter
