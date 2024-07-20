import logging
import re

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../info.log')
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def filter_numbers(transaction: list) -> list:
    """Функция фильтрует список по номеру телефона в описании"""
    logger.info("Начали сортировку по номерам телефона")
    new_list_filter = []
    for i in transaction:
        if "Описание" in i and re.findall(r"((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}", i["Описание"],
                                          flags=re.IGNORECASE):
            new_list_filter.append(i)
    logger.info("Окончили сортировку по номерам телефона")
    return new_list_filter

# print(filter_numbers(read_excel_file("../data/operations.xlsx")))
