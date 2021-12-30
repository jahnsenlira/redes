import topology

from Device import MacInvalidException
from hash_table import *
from Switch import InvalidPortNumberException
from SwitchModel import *
from fork import ConnectionNotPermitedException
import ComputerModel


# Function to display the list of switches or computers
def display_devices(list):
        try:
                print('\033[1;36m-------------------------------------')
                print(f'{"Their " + list[0].__class__.name__ + "es":^35}')
                print('-------------------------------------')
        except IndexError:
                print('Device list in empty!')
        else:
                for i, disp in enumerate(list):
                        print(i, disp)

                print('-------------------------------------\033[0;0m')


def display_topology():
        print('\033[1;33m-------------------------------------')
        print(f'{"Devices of your current topology:":^35~}')
        print('-------------------------------------')
        topology.show_topology()
        print('\033[0;0m')


switch_list = index()
list_of_computers = ComputerModel.index()

try:
        topology.load_topology(list_of_computers, switch_list)
except ConnectionNotPermitedException as cnpe:
        print(cnpe)


print('\n-------------------------------------')
print("Wellcome to Device Manager".upper())

option = None

while option != '0':
        display_devices(switch_list)

        print()
        print('Choose one of the following options :\n')
        print('1 - Register switch')
        print('2 - Register computer')
        print('3 - Display switches')
        print('4 - View computers')
        print('5 - Add MAC to switch')
        print('6 - Discover port by MAC')
        print('7 - Discover MAC by IP (ARP)')
        print('8 - View devices in network topology')
        print('0 - Save and exit manager')

        option = input('\nOption --> ')
        print()

        # register switch
        if option == '1':
                # possible exceptions
                # invalid Mac
                # empty fields
                # non-numeric port
                # door out of range
                while True:
                        try:
                                new_switch = None
                                while True:
                                        print('\033[1;33mENTER NEW SWITCH DATA')
                                        name = input('Name --> ')
                                        ip = input('IP --> ')
                                        mac = input('MAC --> ')
                                        doors = int(input('Number of ports [4, 8, 16, 24] --> \033[0;0m'))

                                        if not name and not ip and not mac:
                                                print('\033[1;31mNo empty fields allowed!\n\033[0;0m')
                                                continue
                                        new_switch = Switch(name, ip, mac, doors)
                                        break
                        except ValueError:
                                print('\033[1;31mIn the ports field, only numeric values are allowed!\033[0;0m')
                        except InvalidPortNumberException as ipne:
                                print(f'\033[1;31m{inpe}\033[0;0m')
                        except MacInvalidException as mie:
                                print(f'\033[1;31m{mie}\033[0;0m')
                        else:
                                switch_list.append(new_switch)
                                print('\033[1;32mSwitch registered successfully!\033[0;0m')
                                break
        
        # register computer
        elif option == '2':
                while True:
                        try:
                                new_pc = None
                                while True:
                                        print('\033[1;33mENTER NEW COMPUTER DATA')
                                        name = input('Name --> ')
                                        ip = input('IP --> ')
                                        mac = input('MAC --> ')

                                        if not name and not ip and not mac:
                                                print('\033[1;31mNo empty fields allowed!\n\033[0;0m')
                                                continue
                                        new_pc = ComputerModel.Computer(name, ip, mac)
                                        break
                        except MacInvalidException as mie:
                                print(f'\033[1;31m{mie}\033[0;0m')
                        else:
                                list_of_computers.append(new_pc)
                                print('\033[1;32mComputer registered successfully!\033[0;0m')
                                break

        # display switches
        elif option == '3':
                display_devices(switch_list)

        # display computers
        elif option == '4':
                display_devices(list_of_computers)

        # Connect device to switch
        elif option == '5':
                while True:
                        try:
                                display_devices(switch_list)
                                print()
                                sw = int(input('\033[1;33mWhich switch do you want to add a MAC to the table on? '))
                                mac = input('Enter the MAC of the device to be connected: ')
                                door = int(input('Enter the port to which the device will be connected: \033[0;0m'))

                                switch_list[sw].addMac(mac, door)
                        except ValueError:
                                print('\033[1;31mEnter only numeric values for the switch and port fields!\033[0;0m')
                        except IndexError:
                                print('\033[1;31mSwitch not found!\033[0;0m')
                        except InvalidPortNumberException as ipne:
                                print(f'\033[1;31m{ipne}\033[0;0m')
                        except AssertionError as ae:
                                print(f'\033[1;31m{ae}\033[0;0m')
                        except MacInvalidException as mie:
                                print(f'\033[1;31m{mie}\033[0;0m')
                        except FullTableException:
                                print('\033[1;31mThe switch MAC table is already full!\033[0;0m')
                        else:
                                print('\033[1;32mConnected device!!\033[0;0m')
                                break

        # Discover port by MAC
        elif option == '6':
                while True:
                        try:
                                display_devices(switch_list)
                                print()
                                sw = int(input('\033[1;33mWhich switch do you want to do the port lookup on? '))
                                mac = input('Enter the MAC of the device you want to search port: \033[0;0m')

                                print(f'\033[1;32mThe door is {switch_list[sw].search(mac)}\033[0;0m')
                        except ValueError:
                                print('\033[1;31mType only numeric values into the switch!\033[0;0m')
                        except IndexError:
                                print('\033[1;31mSwitch not found!\033[0;0m')
                        except MacInvalidException as mie:
                                print(f'\033[1;31m{mie}\033[0;0m')
                        except AbsentKeyException:
                                print('\033[1;31mThe MAC searched does not exist in the MAC table of this switch!\033[0;0m')
                        else:
                                break

        # Discover MAC by IP (ARP)
        elif option == '7'
                try:
                        display_topology()
                        pc = int(input('From which device do you want to make the ARP request? '))
                        ip = input('IP of device you want to discover MAC? ')

                        mac = topology.ARP(ip, topology.devices[pc])
                except ValueError:
                        print('The device code must be numeric!')
                except IndexError:
                        print('Computer does not exist in topology!)
                else:
                        if mac is None:
                                print('MAC not found!')
                        else:
                                print(f'THE MAC of {ip} is {mac}')
        
        # display devices in topology
        elif option == '8':
                display_topology()

        # Save and exit
        elif option == '0':
                save(switch_list)
                ComputerModel.save(list_of_computers)
                print('\033[1;34mbye')
                continue

        # Option unavailable
        else:
                print('\033[1;31mOption unavailable\033[0;0m')

        input('\n\033[1;36mENTER to return to menu... \n\033[0;0m')
