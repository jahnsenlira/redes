from Computer import Computer
from fork import *


devices = []
network = Fork()


def load_topology(pcs, switches):
        global devices

        devices = [
                network.addVertex(switches[0]),  # SW1
                network.addVertex(pcs[0]),  # C1
                network.addVertex(pcs[1]),  # C2
                network.addVertex(pcs[2]),  # C3
                network.addVertex(switches[1]),  # SW2
                network.addVertex(pcs[3]),  # C4
                network.addVertex(pcs[4]),  # C5
                network.addVertex(pcs[5]),  # C6
                network.addVertex(switches[2]),  # SW3
                network.addVertex(pcs[6]),  # C7
                network.addVertex(pcs[7]),  # C8
                network.addVertex(pcs[8]),  # C9
        ]

        try:
                network.addEdge(devices[1], devices[0])
                network.addEdge(devices[2], devices[0])
                network.addEdge(devices[3], devices[0])
                network.addEdge(devices[0], devices[4])
                network.addEdge(devices[5], devices[4])
                network.addEdge(devices[6], devices[4])
                network.addEdge(devices[7], devices[4])
                network.addEdge(devices[4], devices[8])
                network.addEdge(devices[9], devices[8])
                network.addEdge(devices[10], devices[8])
                network.addEdge(devices[11], devices[8])

        except ConnectionNotPermitedException as cnpe:
                raise ConnectionNotPermitedException('Connection between computers is not allowed!')

        return network


def ARP(ip: str, origin: 'Vertex'):
        if ip == origin.given.ip:
                return origin.given.mac

        for v in rede.traverse(origin):
                if v.given.ip == ip:
                        return v.given.mac


def show_topology():
        for i, disp in enumerate(devices):
                print(i, disp.given)
