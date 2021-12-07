def getFuelCostToMoveToPoint(positions, destination):
    return sum([abs(int(x) - destination) for x in positions])


def getFuelCostToMoveToPointBurn(positions, destination):
    diffs = [abs(int(x) - destination) for x in positions]
    fuelCost = 0
    for ind, num in enumerate(diffs):
        myFuelCost = 0
        for i in range(num + 1):
            myFuelCost += i
        fuelCost += myFuelCost

    return fuelCost




def getCheapestConvergence(positions):
    minPoint, maxPoint = int(min(positions)), int(max(positions))
    convergencePoint = None
    cost = 0
    for point in range(minPoint, maxPoint):
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