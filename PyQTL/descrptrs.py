import logging
import sys

if sys.argv[0].find('client_dist') == -1:
    logger = logging.getLogger('server_dist')
else:
    logger = logging.getLogger('client_dist')


class Port:
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError('Порт не долджен быть меньше 0')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

