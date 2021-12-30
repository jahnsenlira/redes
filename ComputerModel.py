import csv
from Computer import Computer

def index():
    computerlist = []

    with open('computers.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        for row in csv_reader:
            if len(row) > 0:
                computer = Computer(row[0], row[1], row[2])

                computerlist.append(computer)
            else:
                break

    return computerlist


def save(list: list):
    with open('computers.csv', 'w', newline='') as csv_file:
        archive = csv.writer(csv_file, delimiter=';')

        for computer in list:
            archive.writerow([computer.name, computer.ip, computer.mac])


if __name__ == '__main__':
    a = index()
    for b in a:
        print(b)

    c = Computer("Acer", "192.168.0.5", "bb:bb:bb:bb:bb:bb")
    a.append(c)
    save(a)
