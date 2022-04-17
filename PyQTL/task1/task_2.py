from task_1 import host_ping
from ipaddress import ip_address


def host_range_ping(get_list=False):
    first_ip = ip_address(input("Введите первоначальный адрес: "))
    count = input("Сколько адресов проверить?: ")
    all_host = []
    [all_host.append(str(first_ip + x)) for x in range(int(count))]
    if not get_list:
        host_ping(all_host)
    else:
        return host_ping(all_host)


if __name__ == "__main__":
    host_range_ping()

