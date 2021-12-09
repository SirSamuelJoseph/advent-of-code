def getTreesForPath(trees, xChange, yChange, start):
    pos = start
    treeCount = 0
    while pos[1] < len(trees):
        if trees[pos[1]][pos[0]] == '#':
            treeCount += 1
        newX, newY = (pos[0] + xChange) % len(trees[0]), pos[1] + yChange
        pos = (newX, newY)
    return treeCount

def getTreeCountForManySlopes(trees, start, slopes):
    product = 1
    for slope in slopes:
        treeCount = getTreesForPath(trees, slope[0], slope[1], start)
        product = product * treeCount
    return product


def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    print(getTreesForPath(inputs, 3, 1, (0,0)))
    slopes = [(1, 1), ( 3, 1), (5,1), (7,1), (1, 2)]
    print(getTreeCountForManySlopes(inputs, (0,0), slopes))

if __name__ == "__main__":
    main()

