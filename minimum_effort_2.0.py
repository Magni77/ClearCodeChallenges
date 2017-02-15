from sys import maxsize
import argparse


class Field():
    def __init__(self, id):
        self.id = id
        self.neighbours = {}
        self.visited = False
        self.previous = None
        self.distance = maxsize

    def set_neighbour(self, neigh, cost):
        self.neighbours[neigh] = cost

    def say_hi(self):
        return 'im {} and i have {} fiends and im  {}'.format(self.id, self.neighbours, self.distance)

    def set_visited(self):
        self.visited = True

    def get_cost(self, neigh):
        return self.neighbours[neigh]

    def get_distance(self):
        return self.distance

    def set_distance(self, d):
        self.distance = d

    def set_previous(self, p):
        self.previous = p

    def get_id(self):
        return self.id


class Map():
    def __init__(self, map):
        self.nodes = []
        self.data = map
        self.fields_dict = []

    def add_field(self, node):
        self.fields_dict.append(Field(node))

    def parse_nodes(self, data):
        for x in data:
            for l in x:
                self.nodes.append(int(l))

    def set_fields(self):
        i=0
        for x in self.data:
            for _ in x:
                self.add_field(i)
                i+=1

    def get_fields_list(self):
        return self.fields_dict

    def get_unvisited(self):
        tmp = []
        for f in self.fields_dict:
            if not f.visited:
                tmp.append(f)
        return tmp

    def find_neigh(self):
        map = self.data
        x = 0
        n = len(map) - 1
        l = len(map)
        for idx, val in enumerate(map):
            for i, v in enumerate(val):
                if i < n:
                    self.fields_dict[x].set_neighbour(self.fields_dict[x + 1], int(val[i + 1]))
                if idx < n:
                    self.fields_dict[x].set_neighbour(self.fields_dict[x + l], int(map[idx + 1][i]))
                x += 1


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


def algorithm(map, start_distance):
    unvisited = map.get_unvisited()
    unvisited[0].set_distance(start_distance) # first fild value

    while len(unvisited):
        current = unvisited[0]
        current.set_visited()

        for next in current.neighbours:
            if next.visited:
                continue

            new_dist = current.get_distance() + current.get_cost(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        unvisited = map.get_unvisited()
    return map.fields_dict[-1].distance


parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file_path',\
                    help="Path to file with data",  default=False)

args = parser.parse_args()

if args.file_path:
    data = load_file(args.file_path)
    for d in data:
        obj = Map(d)
        obj.set_fields()
        obj.find_neigh()
        print(algorithm(obj, int(d[0][0])))
else:
    print('I need file path! [-f "path"]')