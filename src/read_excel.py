import logging
from typing import Any

import pandas as pd

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../info.log')
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_excel_file(filename: str) -> Any:
    """Считывает данные с EXCEL файла и переобразовыввает их в JSON-формат"""
    logger.info("Начали считывание информации с EXCEL-файла")
    try:
        operations = pd.read_excel(filename)
        operations = operations.where(pd.notnull(operations), None)
        file_dict = operations.to_dict(orient="records")
        logger.info("Окончили считывание информации с EXCEL-файла")
        return file_dict
    except Exception as e:
        logger.error(f"Произошла ошибка {e} при считывание информации с EXCEL-файла")
        return f"Ошибка {e}. повторите попытку"

# print(read_excel_file("../data/operations.xlsx"))
