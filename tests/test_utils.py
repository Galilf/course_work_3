from src.utils import get_sorted_operations, get_executed_operations, executed_operations_for_view


def test_get_sorted_operations(operations_fixture_1):
    assert get_sorted_operations(operations_fixture_1) == [
        {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
         'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689',
         'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588',
         'to': 'Счет 14211924144426031657'},
        {'id': 716496732, 'state': 'EXECUTED', 'date': '2018-04-04T17:33:34.701093',
         'operationAmount': {'amount': '40701.91', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Visa Gold 5999414228426353', 'to': 'Счет 72731966109147704472'}
    ]


def test_get_executed_operations(operations_fixture_1):
    assert get_executed_operations(operations_fixture_1) == [
        {'id': 716496732, 'state': 'EXECUTED', 'date': '2018-04-04T17:33:34.701093',
         'operationAmount': {'amount': '40701.91', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Visa Gold 5999414228426353', 'to': 'Счет 72731966109147704472'},
        {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
         'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}
    ]


def test_executed_operations_for_view(operations_fixture_2):
    assert executed_operations_for_view(operations_fixture_2) == '04.04.2018 Перевод организации\n' \
                                                                      'Visa Gold 5999 41** **** 6353 -> Счет **4472\n' \
                                                                      '40701.91 USD\n'