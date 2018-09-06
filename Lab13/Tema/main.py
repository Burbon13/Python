from service.back_it import bktIt
from service.back_rec import bktRec

points = []

file = open('data.txt')

for line in file:
    line = line.strip()
    line = line.split()

    x = int(line[0])
    y = int(line[1])

    points.append((x, y))

print("---- Bkt rec ----")

bktRec(points)

print("---- Bkt it ----")

bktIt(points)

print("---- END ----")