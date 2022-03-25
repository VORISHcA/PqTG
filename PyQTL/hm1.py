import ipaddress
from tabulate import tabulate

ip_list = ['10.0.1.1/24', '10.0.1.0/24']


def host_ping(ip_roster):
    for check_ip in ip_roster:
        try:
            ipaddress.ip_network(check_ip)
            print(f'{check_ip} узел доступен')
        except ValueError:
            print(f'{check_ip} узел не доступен')


def host_range_ping(ip, first, last, right=0):
    all_h = list((ipaddress.ip_network(ip)).hosts())
    for local in range(first - 1, last):
        try:
            ipaddress.ip_network(all_h[local:][0])
            print(f'{all_h[local:][0]} узел доступен')
            right += 1
        except ValueError:
            print(f'{all_h[local:][0]} узел не доступен')
    print(f'Здоровых {right}, больных {last - right - first - 1}')


def host_range_ping_tab(ip, first, last):
    columns_right = ['Reachable']
    columns_wrong = ['Unreachable']
    list_right = []
    list_wrong = []
    all_h = list((ipaddress.ip_network(ip)).hosts())
    first -= 1
    for local in range(first, last):
        try:
            ipaddress.ip_network(all_h[local:][0])
            list_right.append([local - first, all_h[local:][0]])
        except ValueError:
            list_wrong.append([local - first, all_h[local:][0]])
    print(tabulate(list_right, headers=columns_right))
    print(tabulate(list_wrong, headers=columns_wrong))


host_ping(ip_list)

host_range_ping('10.0.1.0/24', 50, 100)

host_range_ping_tab('10.0.1.0/24', 50, 100)