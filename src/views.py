import pandas as pd
from typing import Any


def read_excel_file(filename: str) -> Any:
    """Считывает данные с EXCEL файла и переобразовыввает их в JSON-формат"""
    try:
        operations = pd.read_excel(filename)
        operations = operations.where(pd.notnull(operations), None)
        file_dict = operations.to_dict(orient="records")
        return file_dict
    except Exception as e:
        return f"Ошибка {e}. повторите попытку"


#print(read_excel_file("../data/operations.xlsx"))
