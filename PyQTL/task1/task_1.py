import platform
import subprocess
from ipaddress import ip_address


def host_ping(hosts_list):
    for_three = {"Не доступные": "", 'Доступные': ""}
    for host in hosts_list:
        try:
            try:
                ipv4 = ip_address(host)
            except ValueError:
                raise Exception('Ошибка в ip')
        except Exception:
            print(f'Домен {host}')
            ipv4 = host

        param = '-n' if platform.system().lower() == 'windows' else '-c'
        response = subprocess.Popen(["ping", param, '1', '-w', '1', str(ipv4)],
                                    stdout=subprocess.PIPE)

        if response.wait() == 0:
            print(f'Доступный {ipv4}')
            for_three["Доступные"] += f"{ipv4}\n"
        else:
            print(f'Не доступный {ipv4}')
            for_three["Не доступные"] += f"{ipv4}\n"
    return for_three


if __name__ == '__main__':
    hosts_list = ['192.168.0.1', 'google.com', '34.232.4.1']
    host_ping(hosts_list)
