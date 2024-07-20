from src.read_excel import read_excel_file


def test_read_file():
    assert read_excel_file("../data/operations.xlsx")[-1] == {'Дата операции': '01.01.2018 12:49:53',
                                                              'Дата платежа': '01.01.2018',
                                                              'Номер карты': 'Отсутствует', 'Статус': 'OK',
                                                              'Сумма операции': -3000.0, 'Валюта операции': 'RUB',
                                                              'Сумма платежа': -3000.0, 'Валюта платежа': 'RUB',
                                                              'Кэшбэк': 'Отсутствует', 'Категория': 'Переводы',
                                                              'MCC': 'Отсутствует', 'Описание': 'Линзомат ТЦ Юность',
                                                              'Бонусы (включая кэшбэк)': 0,
                                                              'Округление на инвесткопилку': 0,
                                                              'Сумма операции с округлением': 3000.0}

    assert read_excel_file("") == "Ошибка [Errno 2] No such file or directory: ''. повторите попытку"
    assert read_excel_file(True) == "Ошибка Invalid file path or buffer object type: <class 'bool'>. повторите попытку"
