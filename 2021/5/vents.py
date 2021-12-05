import math

def getLinesFromInput(inputs):
    map = []
    count = 0
    for line in inputs:
        components = line.split('->')
        start = components[0].split(',')
        end = components[1].split(',')
        start = [int(start[0]), int(start[1])]
        end = [int(end[0]), int(end[1])]
        pos = start
        while (pos[0] != end[0] or pos[1] != end[1]):
            mag = math.sqrt((end[0] - pos[0]) ** 2 + (end[1] - pos[1]) ** 2)
            x, y = int(pos[0]), int(pos[1])
            if len(map) <= y:
                for i in range(len(map) -1, y):
                    map.append([0])
            if len(map[y]) <= x:
                for i in range(len(map[y]) -1, x):
                    map[y].append(0)
            map[y][x] += 1
            count += 1
            newX, newY = x, y
            if pos[0] > end[0]:
                newX -= 1
            elif pos[0] < end[0]:
                newX = newX + 1

            if pos[1] > end[1]:
                newY -= 1
            elif pos[1] < end[1]:
                newY += 1
            pos = [newX, newY]
        # Do it once more outside of the loop to make sure to include the last element
        x, y = int(pos[0]), int(pos[1])
        if len(map) <= y:
            for i in range(len(map) -1, y):
                map.append([0])
        if len(map[y]) <= x:
            for i in range(len(map[y]) -1, x):
                map[y].append(0)
        map[y][x] += 1
            
    intersects = 0
    for _, row in enumerate(map):
        for val in row:
            if val > 1:
                intersects += 1
    print(intersects)

inputs = [line.rstrip() for line in open("input.txt")]
getLinesFromInput(inputs)