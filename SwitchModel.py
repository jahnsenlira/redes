import csv
from Switch import Switch


def index():
    switchlist = []

    with open('switchs.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        for row in csv_reader:
            if len(row) > 0:
                switch = Switch(row[0], row[1], row[2], int(row[3]))

                if len(row) == 5:
                    tableMac = row[4].split(',')

                    for adresses in tableMac:
                        arrayAddress = addresses.split('-')

                        switch.addMac(arrayAddress[1], int(arrayAddress[0])

                switchlist.append(switch)
            else:
                break

        return switchlist


def save(list: list):
    with open('switchs.csv', 'w', newline='') as csv_file:
        archive = csv.writer(csv_file, delimiter=';')

        for switch in list:
            if switch.doorsinuse():
                tabelaMac = switch.returnAdresses()
                string_entries = []

                for entry in tableMac:
                    string_entries.append(f'{str(entry[1]}-{entry[0]}')
                    # print(entry[0], entry[1])

                mac_table_string = ','.join(string_entries)
                archive.writerow([switch.name, switch.ip, switch.mac, switch.doors, mac_table_string])
            else:
                archive.writerow([switch.name, switch.ip, switch.mac, switch.doors])
