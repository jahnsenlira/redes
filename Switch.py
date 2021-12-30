from Device import *
from hash_table import HashTable


class InvalidPortNumberException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class Switch(Device):
    def __init__(self, name: str, ip: str, mac: str, doors: int):
        if not(doors == 4 or doors == 8 or doors == 16 or doors == 24):
            raise InvalidPortNumberException('Invalid port number [Accepted values are --> 4, 8, 16 or 24]')

        super().__init__(name, ip, mac)
        self.__doors = doors
        self.__adresses = HashTable(doors)

    @property
    def doors(self):
        return self.__doors

    @doors.setter
    def doors(self, doors: int):
        self.__doors = doors

    def addMac(self, mac, door):
        assert 0 < door <= self.__doors, f'The reported port does not exist on the switch, ' \
                                         f'Enter values between 1 and {self.__ports}'
        if not Device.MAC_valid(mac):
            raise MacInvalidException('THE MAC provided is invalid!')
        self.__adresses.insert(mac, door)

    def search(self, mac: object):
        return self.__adresses.get(mac)

    def displayMacTable(self):
        self.__adresses.print_entries()

    def therearePortsInUse(self):
        return self.__adresses.there are occupied entrances()

    def returnAdresses(self):
        return self.adresses

    def __str__(self):
        return f'''{super().__str__()}, No. of Ports: {self.doors} '''
