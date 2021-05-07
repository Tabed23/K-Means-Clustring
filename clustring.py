import random
import math
from matplotlib import pyplot as plt


def genreate_points(data):
    points = []
    for i in range(0, len(data)):
        for j in range(len(data[i])):
            if data[i][j] is 1:
                points.append([i, j])
    return points


def read_from_file(filemane='dataset.txt'):
    f = open(filemane, 'r')
    lines = f.read().splitlines()
    itmes = []
    for i in range(0, len(lines)):
        line = lines[i].split(',')
        items_data = []
        for j in range(len(line)):
            v = int(line[j])
            items_data.append(v)
        itmes.append(items_data)
    return genreate_points(itmes)


def make_centroid(data_set):
    cord = random.randint(0, len(data_set))
    if cord > len(data_set):
        cord = make_centroid(data_set)
    return data_set[cord]


def get_coords(data_set, index):
    if index > len(data):
        return make_centroid(data_set)
    return data_set[index]


def euler_distance(point, centroid):
    avg = []
    for i in range(0, 3):
        X = math.pow(centroid[i][0] - point[0], 2)
        Y = math.pow(centroid[i][1] - point[1], 2)
        val = math.sqrt(X + Y)
        avg.append(math.floor(val))
    if (avg[0] < avg[1]) and (avg[0] < avg[2]):
        return 0, avg[0]
    elif (avg[1] < avg[0]) and (avg[1] < avg[2]):
        return 1, avg[1]
    else:
        return 2, avg[2]


def distance(data_set, centroids):
    c1 = []
    c2 = []
    c3 = []
    for i in range(len(data_set)):
        X = data_set[i]
        cluster, dis = euler_distance(data_set[i], centroids)
        if cluster is 0:
            c1.append(dis)
        if cluster is 1:
            c2.append(dis)
        if cluster is 2:
            c3.append(dis)
    return c1, c2, c3


def my_mean(values):
    n = 0
    Sum = 0.0
    for v in values:
        Sum += v
        n += 1
    if n is 0:
        return 0
    return Sum / n


if __name__ == '__main__':
    k = 3
    data = read_from_file()
    centroids = []
    for _ in range(0, k):
        centroids.append(make_centroid(data))
    c1 = []
    c2 = []
    c3 = []
    for _ in range(0, 3):
        c1, c2, c3 = distance(data, centroids)
        c1_mean = math.floor(my_mean(c1))
        c2_mean = math.floor(my_mean(c2))
        c3_mean = math.floor(my_mean(c3))
        centroids.clear()
        centroids = [get_coords(data, c1_mean), get_coords(data, c2_mean), get_coords(data, c3_mean)]

    print("c1 cluster ->", c1)
    print("c2 cluster ->", c2)
    print("c3 cluster ->", c3)