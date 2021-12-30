from Device import *


class Computer(Device):

        def __init__(self, name: str, ip: str, mac: str):
            super().__init__(name, ip, mac)
