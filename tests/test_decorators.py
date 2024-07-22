import os

from src.read_excel import read_excel_file
from src.reports import spending_by_category


def test_1():
    transaction = read_excel_file("../data/operations.xlsx")
    spending_by_category(transaction, "Супермаркеты", "31-03-2022 16:43:00")
    log_file = os.path.join(os.path.dirname(__file__), "mylog.json")
    with open(log_file, "r") as file:
        log_test = file.read()
        assert log_test == (
            "[{'Дата операции': '31.12.2021 16:44:00', 'Дата платежа': '31.12.2021', 'Номер карты': '*7197', "
            "'Статус': 'OK', 'Сумма операции': -160.89, 'Валюта операции': 'RUB', 'Сумма платежа': -160.89, "
            "'Валюта платежа': 'RUB', 'Кэшбэк': 'Отсутствует', 'Категория': 'Супермаркеты', 'MCC': 5411.0, "
            "'Описание': 'Колхоз', 'Бонусы (включая кэшбэк)': 3, 'Округление на инвесткопилку': 0, "
            "'Сумма операции с округлением': 160.89}]")

#
# def test_in_file():
#     """Тест декоратора log"""
#     transaction = read_excel_file("../data/operations.xlsx")
#     with pytest.raises(ValueError):
#         spending_by_category(transaction, "Супермаркеты", "31/03-2022 16:43:00")
#     log_file = os.path.join(os.path.dirname(__file__), "mylog.json")
#     with open(log_file, "r") as file:
#         log_test = file.read()
#         assert log_test == "Произошла ошибка time data '31.03-2022 16:43:00'
#         does not match format '%d-%m-%Y %H:%M:%S'"
