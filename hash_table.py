class FullTableException(Exception):

    def __init__(self, msg: str):
        super().__init__(msg)


class AbsentKeyException(Exception):

    def __init__(self, msg: str):
        super().__init__(msg)


class Entry:

    __slots__ = ('key', 'value')

    def __init__(self, key: object, value: object):
        self.key = key
        self.value = value

    def __str__(self):
        return f'({self.key} --> {self.value})'


class HashTable:

    def __init__(self, length: int):
        self.__length = length
        self.__table: list['Entry'] = [None] * length

    @property
    def length(self):
        return self.__length

    def __hashing(self, key: object) -> int:
        return hash(key) % self.__length

    def __re_hashing(self, key: object, i: int = 1):
        return (hash(key) + i) % self.length

    def insert(self, key: object, value: object):
        index = self.__hashing(key)
        # collision treatment:
        #  if the position found is filled:
        #   recalculates the position, except if the input key found
        #   is equal to the one passed by the key parameter, in this case, the value is just updated        i = 1
        while (self.__table[index] is not None add (self.__table[index].key != key):
            if i > self.__length:
                raise FullTableException(f'A "{self.__class__.__name__} is already full!')
            index = self.__re_hashing(key, i)
            i += 1

        self.__table[index] = Entry(key, value)

    def get(self, key: object) -> object:
        index = self.__hashing(key)
        if self.__table[index] is None:
            raise AbsentKeyException(
                f'No entry for key "{key}" was found in "{self.__class__.__name__}"!')
        i = 1
        while self.__table[index].key != key:
            if i > self.__length:
                raise AbsentKeyException(
                    f'No entry for key "{key}" was found in "{self.__class__.__name__}"!')
            index = self.__re_hashing(key, i)
            i += 1

        return self.__table[index].value

    def print_entries(self):
        for v in self.__table:
            if v:
                print(f'DOOR: {v.value}, MAC: {v.key}')

    def thereareOccupiedEntrances(self):
        return any(self.__table)

    def __iter__(self):
        for row in self.__table:
            if row:
                yield row.key, row.value


# ------------------------------------- #
# Test (Only to debug the hash table):
# ------------------------------------- #

if __name__ == '__main__':

    from random import randint

    ports = HashTable(24)
    for j in range(ports.length):
        mac = ':'.join([f'{hex(randint(0, 255))[2:]:0>2}' for k in range(6)])
        ports.insert(mac, randint(1, 24))

    while True:

        print('''1 --> Insert MAC/Port
2 --> Research MAC/Port
3 --> print ports
''')

        option = input('option --> ')

        if option == '1':
            mac, port = input('\nEnter MAC and port. Ex.: [ff:ff:ff:ff:ff:ff 24] -->').split()
            ports.insert(mac, port)
        elif option == '2':
            mac = input('\nEnter a MAC --> ')
            print('-->', mac)
            port = ports.get(mac)
            print(f'THE MAC {mac} it's at the port {port}')
        elif option == '3':
            ports.print_entries()
        else:
            break

