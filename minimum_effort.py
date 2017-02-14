import argparse
import csv
import math
from collections import defaultdict

class Map():
    def __init__(self, map):
        self.rows = []
        self.data = map
        self.n = int(math.sqrt(len(map)))
        self.adjacency_list = []
        print(map)

    def set_adjacency(self, data):
        tmp = []
        for node in data:
            pass


parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file_path',\
                    help="Path to file with data",  default=False)

args = parser.parse_args()


'''
    Pierwszy problem - jak wczytac dane z pliku by móc przetwarzac wiele map?
        -Stworzyc liste, w ktorej każdy index będzie osobną mapą.

'''


def load_file(path):
    rows = []
    with open(path) as file:
        for l in file:
            tmp = []
            for _ in range(int(l)):
                line = file.readline().split(',')
                #for x in line:
                tmp.append(line)
            rows.append(tmp)

    return rows

data = load_file('data')
for d in data:
    Map(d)

edges = defaultdict(list)
# for d in data:
#     edges[d].append(d)

print('here')
map=data[1]
n = len(map) -1
for idx, val in enumerate(map):
    print(val)
    for i, v in enumerate(val):
        if i < n:
            edges[int(val[i])].append(int(val[i+1]))
        if idx < n:
            edges[int(val[i])].append(int(map[idx+1][i]))
        if idx == n and i == n:
            edges[int(val[i])].append(False)


print(edges)