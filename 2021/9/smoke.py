def getRiskLevelsForAllLowPoints(heightmap):
    risks = 0
    lowPoints = []
    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            val = int(heightmap[y][x])
            lowestAround = True
            if x != 0:
                lowestAround = lowestAround and val < int(heightmap[y][x - 1])
            if x != len(heightmap[0]) - 1:
                lowestAround = lowestAround and val < int(heightmap[y][x + 1])
            if y != 0:
                lowestAround = lowestAround and val < int(heightmap[y - 1][x])
            if y != len(heightmap) - 1:
                lowestAround = lowestAround and val < int(heightmap[y + 1][x])

            if lowestAround:
                lowPoints.append((x, y))
                risks += val + 1
    return risks, lowPoints

def getAllBasinSizes(lowpoints, heightmap):
    basinSizes = []
    for lowpoint in lowpoints:
        basinSize = getBasin(heightmap, [lowpoint])
        basinSizes.append(basinSize)
    return basinSizes

def getBasin(heightmap, positions):
    newPositions = set(positions)
    for position in positions:
        x, y = position[0], position[1]
        val = int(heightmap[y][x])
        if x != 0:
            if int(heightmap[y][x - 1]) != 9:
                newPositions.add((x-1, y))
        if x != len(heightmap[0]) - 1:
            if int(heightmap[y][x + 1]) != 9:
                newPositions.add((x+1, y))
        if y != 0:
            if int(heightmap[y - 1][x]) != 9:
                newPositions.add((x, y - 1))
        if y != len(heightmap) - 1:
            if int(heightmap[y + 1][x]) != 9:
                newPositions.add((x, y + 1))

    if len(positions) == len(newPositions):
        return len(positions)
    else:
        return getBasin(heightmap, list(newPositions))


def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    risks, lowPoints = getRiskLevelsForAllLowPoints(inputs)
    basinSizes = getAllBasinSizes(lowPoints, inputs)
    print(sorted(basinSizes)[-3:])

if __name__ == "__main__":
    main()