import argparse
from collections import defaultdict


class Map():
    def __init__(self, map):
        self.nodes = []
        self.data = map
        self.edges = defaultdict(list)
        self.fields_dict = []

    def start(self):
        data = self.data
        self.set_adjacency(data)
        self.parse_nodes(data)
        self.algorithm()

    #Funkcja sprawdzajaca mozliwe ruchy
    def set_adjacency(self, data):
        map = data
        n = len(map) - 1
        x = 0
        for idx, val in enumerate(map):
            for i, v in enumerate(val):
                if i < n:
                    self.edges[int(val[i])].append(int(val[i + 1]))
                if idx < n:
                    self.edges[int(val[i])].append(int(map[idx + 1][i]))
                x += 1

    def parse_nodes(self, data):
        for x in data:
            for l in x:
                self.nodes.append(int(l))

    def algorithm(self):
        nodes = self.nodes
        visited = {nodes[0]: nodes[0]}
        goal = nodes[-1]
        path = {}
        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.edges[min_node]:
                weight = current_weight + edge
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        print(visited[goal])


#Pierwszy problem - jak wczytac dane z pliku by umozliwialy przetwarzanie wielu map?
def load_file(path):
    rows = []
    with open(path) as file:
        for l in file:
            tmp = []
            for _ in range(int(l)):
                line = file.readline().split(',')
                tmp.append(line)

            rows.append(tmp)

    return rows


#Argumenty z cmd
parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file_path',\
                    help="Path to file with data",  default=False)

args = parser.parse_args()

if args.file_path:
    data = load_file(args.file_path)
    for d in data:
        Map(d).start()
else:
    print('I need file path! [-f "path"]')
