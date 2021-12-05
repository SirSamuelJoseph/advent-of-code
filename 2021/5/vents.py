import math

def getPointsOnLine(start, stop):
    pos = start
    points = []
    while (pos[0] != stop[0] or pos[1] != stop[1]):
        points.append(pos)
        newX, newY = 0,0
        if pos[0] > stop[0]:
            newX -= 1
        elif pos[0] < stop[0]:
            newX = newX + 1

        if pos[1] > stop[1]:
            newY -= 1
        elif pos[1] < stop[1]:
            newY += 1
        pos = (pos[0] + newX, pos[1] + newY)
    points.append(stop)
    return points

def getIntersectionsAboveOne(inputs, counts, diagsCount):
    for line in inputs:
        components = line.split('->')
        start = components[0].split(',')
        end = components[1].split(',')
        start = (int(start[0]), int(start[1]))
        end = (int(end[0]), int(end[1]))
        isLineDiagonal = start[0] != end[0] and start[1] != end[1]
        
        if diagsCount or not diagsCount and not isLineDiagonal:
            pointsOnLine = getPointsOnLine(start, end)
            for point in pointsOnLine:
                if not point in counts:
                    counts[point] = 1
                else:
                    counts[point] += 1
    count = 0
    for key, value in counts.items():
        if value > 1:
            count += 1
    return count
                
def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    print(getIntersectionsAboveOne(inputs, {}, False))
    print(getIntersectionsAboveOne(inputs, {}, True))
 
if __name__ == "__main__":
    main()
