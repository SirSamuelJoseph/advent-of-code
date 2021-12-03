
def getPowerConsumption(binaries):
    bitLength = len(binaries[0]) - 1 # subtract the newline
    mostCommon = [0] * bitLength
    for i in range(bitLength):
        mostCommon[i] = getMostCommonBitFromPosition(binaries, i)
    leastCommonString = ''.join(['1' if i == '0' else '0' for i in mostCommon])
    mostCommonString = ''.join(mostCommon)
    gamma = int(mostCommonString, 2)
    epsilon = int(leastCommonString, 2)
    product = gamma * epsilon
    returnString = "Gamma: {}, Epsilon: {}, Product: {}"
    print(returnString.format(gamma, epsilon, product))

def getLifeSupportRating(binaries):
    oxygen = int(getLifeSupportSubsystem(binaries, True), 2)
    co2 = int(getLifeSupportSubsystem(binaries, False), 2)
    product = oxygen * co2
    returnString = "Oxygen: {}, CO2: {}, Product: {}"
    print(returnString.format(oxygen, co2, product))

def getLifeSupportSubsystem(binaries, isOxygen):
    contenders =  binaries
    index = 0
    while(len(contenders) > 1):
        mostCommonNum = getMostCommonBitFromPosition(contenders, index)
        contenders = [x for x in contenders if binaryCounted(x, index, mostCommonNum, isOxygen)]
        index += 1
    return contenders[0]

def importBinaries(path):
    file = open(path, 'r')
    binaries = file.readlines()
    return binaries

def getMostCommonBitFromPosition(binaries, position):
    vals = [int(x[position], 2) for x in binaries]
    mean = float(sum(vals)) / len(binaries)
    if mean > .5:
        return "1"
    if mean == .5:
        return "2"
    return "0"

def binaryCounted(binary, index, mostCommon, isOxygen):
    bit = binary[index]
    if isOxygen:
        if mostCommon == '2':
            return bit == '1'
        else:
            return bit == mostCommon
    else:
        if mostCommon == '2':
            return bit == '0'
        else:
            return bit != mostCommon

getPowerConsumption(importBinaries("input.txt"))
getLifeSupportRating(importBinaries("input.txt"))