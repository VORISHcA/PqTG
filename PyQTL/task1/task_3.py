from task_2 import host_range_ping
from tabulate import tabulate


def host_range_ping_tab():
    dict_task_1 = host_range_ping(True)
    print(tabulate([dict_task_1], headers='keys', tablefmt='fancy_grid'))


if __name__ == "__main__":
    host_range_ping_tab()
