def getFuelCostToMoveToPoint(positions, destination):
    return sum([abs(int(x) - destination) for x in positions])


def getFuelCostToMoveToPointBurn(positions, destination):
    diffs = [abs(int(x) - destination) for x in positions]
    fuelCost = 0
    for num in diffs:
        myFuelCost =  (num * (num + 1)) / 2
        fuelCost += myFuelCost

    return fuelCost




def getCheapestConvergence(positions, isEfficient = False):
    minPoint, maxPoint = int(min(positions)), int(max(positions))
    convergencePoint = None
    cost = 0
    for point in range(minPoint, maxPoint):
        if isEfficient:
            newCost = getFuelCostToMoveToPoint(positions, int(point))
        else:
            newCost = getFuelCostToMoveToPointBurn(positions, int(point))
        print(point, newCost)
        if not convergencePoint or newCost < cost:
            convergencePoint = int(point)
            cost = newCost
    return (convergencePoint, cost)

def main():
    inputs = [line.rstrip().split(',') for line in open("input.txt")][0]
    print(getCheapestConvergence(inputs))

if __name__ == "__main__":
    main()