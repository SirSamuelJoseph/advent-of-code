def getElfWithMostFood(inputs): 
    tempBiggest = -1
    currentElfCount = 0
    for input in inputs:
        if input == '':
            print('current elf: ' + str(currentElfCount))
            if currentElfCount > tempBiggest:
                tempBiggest = currentElfCount
            currentElfCount = 0
        else:
            currentElfCount += int(input)
    return max(tempBiggest, currentElfCount)

def getAllElfFoodCount(inputs):
    results = []
    currentElfCount = 0
    for input in inputs:
        if input == '':
            results.append(currentElfCount)
            currentElfCount = 0
        else:
            currentElfCount += int(input)
    results.sort()
    return results

def getThreeMostCaloricElves(inputs):
    allCounts = getAllElfFoodCount(inputs)
    return allCounts[-1] + allCounts[-2] + allCounts[-3]

def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    print(getThreeMostCaloricElves(inputs))

if __name__ == "__main__":
    main()