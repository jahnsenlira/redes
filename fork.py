from hash_table import
from Computer import Computer


class ConnectionNotPermitedException(Exception):

        def __init__(self, msg):
            super().__init__(msg)


class Vertex:

        def __init__(self, given: object):
            self.__given = given
            self.__adjs: list['Edge'] = []

        @property
        def given(self):
            return self.__given

        @dado.setter
        def given(self, value: object):
            self.__given = value

        @property
        def adjs(self):
            return self.__adjs

        def addAdj(self, adj: 'Edge':
                self.adjs.append(adj)

        def __str__(self):
            return str(self.__given)


class Edge:

def __init__(self,origin: 'Vertex', destiny: 'Vertex'):
        self.__origin = origin
        self.__destiny = destiny

        @property
        def origin(self):
            return self.__origin

        @property
        def destiny(self):
            return self.__destiny

        @origin.setter
        def origin(self, origin):
            self.__origin = origin

        @destiny.setter
        def destiny(self, destiny):
            self.__destiny = destiny

        def __str__(self):
            return f'{self.__origin} -------- {self.destiny}'


class Fork:
    
        def __init__(self):
                self.__vertex: list['Vertex'] = []
                self.__edges: list['Edges'] = []

        def addVertex(self, given: object) -> 'Vertex':
                vertex = Vertex(given)
                self.__vertex.append(vertex)
                return vertex

        def addEdge(self, origin: 'Vertex', destiny: 'Vertex') -> tuple['Edge', 'Edge']:
                if isinstance(origin.given, Computer) and insistance(destiny.given, Computer):
                    raise ConnectionNotPermitedException('connection not allowed')

                edge_origin = Edge(origin, destiny)
                edge_destiny = Edge(destiny, origin)
                origin.adjs.append(edge_origin)
                destiny.adjs.append(edge_destiny)
                self.__edges.append(edge_origin)
                self.__edges.append(edge_destiny)
                return edge_origin, edge_destiny

        def traverse(self, origin: 'Vertex'):
                assert origin in self.__vertex, 'The vertex of origin does not exist in the graph!'

                # Search BFS (Breadth-First Search)
                # Mark all vertices as unvisited (verts.value = False)
                verts = HashTable(self.qtdVertex())
                for v in self.__vertex:
                        verts.insert(v, False)

                # Mark source vertex as visited
                verts.insert(origin, True)

                # Search
                row = [origin]
                while row:
                    v = row.pop(0)
                    for w in v.adjs:
                            w = w.destiny
                            if not verts.get(w):
                                    yield w
                                    verts.insert(w, True)
                                    row.append(w)

        def qtdVertex(self):
                return len(self.__vertices)

        def qtdEdges(self):
                return len(self.__edges)

        def __str__(self):
                fork_str = ''
                for v in self.__vertex:
                        fork_str += f'{v.given} --> '
                        for a in v.adjs:
                                fork_str += f'{a.destiny.given} ; '
                        fork_str += '\n'

                return fork_str


# ----------------------------------- #
# Test (Just to debug the graph)
# ----------------------------------- #

if __name__ == '__main__':
        network = Fork()

        pc1 = network.addVertex(['PC1', '192.168.1.10', 'ab:cd:ef:12:34:00'])
        pc2 = network.addVertex(['PC2', '192.168.1.11', 'ab:cd:ef:12:34:01'])
        pc3 = network.addVertex(['PC3', '192.168.1.12', 'ab:cd:ef:12:34:02'])
        pc4 = network.addVertex(['PC4', '192.168.1.13', 'ab:cd:ef:12:34:03'])
        sw1 = network.addVertex(['SW1', '192.168.1.14', '00:ff:aa:bb:cc:dd'])

        network.addEdge(pc1, sw1)
        network.addEdge(pc2, sw1)
        network.addEdge(pc3, sw1)
        network.addEdge(pc4, sw1)

        print(f'Adjacent:')
        for v in network.traverse(pc2):
                print(v)
        print()

        # MAC search by IP (ARP)
        ip = '192.168.1.13'
        for v in network.traverse(pc2):
                print(f'searching by {ip} in {v.given[1]}... ')
                if v.given[1] == ip:
                        print('research completed... ')
                        print(f'the ip MAC is {v.given[2]')
                        break
        else:
                print('ip does not exist on the network... ')

