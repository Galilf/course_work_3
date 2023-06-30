import os.path
from src.utils import get_operations, get_executed_operations, get_sorted_operations, executed_operations_for_view


OPERATIONS_FILE = os.path.join('..', 'operations.json')


def main():
    operations = get_operations(OPERATIONS_FILE)
    sorted_operations = get_sorted_operations(operations)
    sorted_executed_operations = get_executed_operations(sorted_operations)
    for i in range(5):
        print(executed_operations_for_view(sorted_executed_operations[i]))


if __name__ == "__main__":
    main()
