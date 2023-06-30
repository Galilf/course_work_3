import json


def get_operations(file_path):
    """
    Принимает файл для чтения и возвращает список банковских операции клиента
    :param file_path: путь к файлу для чтения
    :return: client_operations - список банковских операции клиента
    """
    with open(file_path, encoding='utf-8') as file:
        client_operations = json.loads(file.read())
    return client_operations


def get_sorted_operations(operations):
    """
    Сортирует список банковских операции по дате, от новых к старым.
    :param operations: банковские операции клиента
    :return: sorted_operations - отсортированный список операции
    """
    operations_with_date = [operation for operation in operations if operation.get("date")]
    sorted_operations = sorted(operations_with_date, key=lambda x: x['date'], reverse=True)
    return sorted_operations


def get_executed_operations(operations):
    """
    Возвращает список банковских операции со статусом EXECUTED
    :param operations: банковские операции клиента
    :return: executed_operations - список банковских операции со статусом EXECUTED
    """
    executed_operations = [operation for operation in operations if operation.get("state") == 'EXECUTED']
    return executed_operations


def executed_operations_for_view(operation):
    """
    Принимает одну банковскую операцию и возвращает ее в читабельном виде
    :param operation: банковская операция
    :return: result - операция в читабельном виде
    """
    date = '.'.join(operation['date'][:10].split('-')[::-1])

    description = operation['description']

    from_bill = ''
    if operation.get('from'):
        from_bill = operation['from'].split()
        if len(from_bill[-1]) == 16:
            from_bill[-1] = f'{from_bill[-1][:4]} {from_bill[-1][4:6]}** **** {from_bill[-1][12:]}'
        else:
            from_bill[-1] = f'**{from_bill[-1][-4:]}'
        from_bill = ' '.join(from_bill) + ' -> '

    to_bill = operation['to'].split()
    to_bill[-1] = f'**{to_bill[-1][-4:]}'
    to_bill = ' '.join(to_bill)

    operation_amount = operation['operationAmount']['amount']

    currency = operation['operationAmount']['currency']['name']

    result = f'{date} {description}\n' \
             f'{from_bill}{to_bill}\n' \
             f'{operation_amount} {currency}\n'
    return result
