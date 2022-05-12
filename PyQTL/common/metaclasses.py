import dis


class ClientVerifier(type):
    def __init__(cls, class_name, bases, class_dict):
        methods = []
        for local in class_dict:
            res = dis.get_instructions(class_dict[local])
            for x in res:
                if x.opname == 'LOAD_GLOBAL':
                    if x.argval not in methods:
                        methods.append(x.argval)

        if 'get_message' not in methods or 'send_message' not in methods:
            raise TypeError('использование сокетов для работы по TCP')
        for command in ('listen', 'accept'):
            if command in methods:
                raise TypeError('отсутствие вызовов accept и listen для сокетов;')
        super().__init__(class_name, bases, class_dict)


class ServerVerifier(type):
    def __init__(cls, class_name, bases, class_dict):
        methods = []
        attrs = []
        for local in class_dict:
            ret = dis.get_instructions(class_dict[local])
            for x in ret:
                print(x)
                if x.opname == 'LOAD_GLOBAL':
                    if x.argval not in methods:
                        methods.append(x.argval)
                if x.opname == 'LOAD_ATTR':
                    if x.argval not in attrs:
                        attrs.append(x.argval)
        for command in ('connect'):
            if command in methods:
                raise TypeError('отсутствие вызовов connect для сокетов;')
        for att in ('SOCK_STREAM', 'AF_INET'):
            if att not in methods:
                raise TypeError('использование сокетов для работы по TCP')
        super().__init__(class_name, bases, class_dict)


