from unittest.mock import patch
import datetime

from src.read_excel import read_excel_file
from src.reports import spending_by_category

transactions = read_excel_file("../data/operations.xlsx")


@patch("src.reports.datetime")
def test_spending_by_category(mock_get):
    mock_get.return_value = datetime.datetime(2024, 7, 20, 17, 54, 1, 982338)
    assert spending_by_category(transactions, "Супермаркеты") == []


def test_spending_by_category_second():
    assert spending_by_category(transactions, "Супермаркеты", "10-12-2019 19:00:00")[0] == {
        'Дата операции': '10.12.2019 18:08:14', 'Дата платежа': '14.12.2019', 'Номер карты': '*4556', 'Статус': 'OK',
        'Сумма операции': -273.74, 'Валюта операции': 'RUB', 'Сумма платежа': -273.74, 'Валюта платежа': 'RUB',
        'Кэшбэк': 13.0, 'Категория': 'Супермаркеты', 'MCC': 5499.0, 'Описание': 'Колхоз',
        'Бонусы (включая кэшбэк)': 13, 'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 273.74}
