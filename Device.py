from abc import ABC, abstractmethod
from re import match


class MacInvalidException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class Device(ABC):

    def __init__(self, name: str, ip: str, mac: str):

        if not Device.MAC_valid(mac):
            raise MacInvalidException('THE MAC provided is invalid')

        self.__name = name
        self.__ip = ip
        self.__mac = mac

    @property
    def name(self):
        return self.__name

    @property
    def ip(self):
        return self.__ip

    @property
    def mac(self):
        return self.__mac

    @name.setter
    def name(self, name: str):
        self.__name = name

    @ip.setter
    def ip(self, ip: str):
        self.__ip = ip

    @mac.setter
    def mac(self, mac: str):
        self.__mac = mac

    @staticmethod
    def MAC_valid(mac: str) -> bool:
        return match('^(([0-9a-f]{2}:){5}([0-9a-f]{2})$', mac.lower())

    def __str__(self):
        return ("Name: %s, IP: %s, MAC: %s"%(self.__nome,self.__ip,self.__mac))
