# Gets the power consumption for the given binaries
def getPowerConsumption(binaries):
    bitLength = len(binaries[0]) - 1 # subtract the newline
    mostCommon = [0] * bitLength
    for i in range(bitLength):
        mostCommon[i] = getMostCommonBitFromPosition(binaries, i)
    # Invert the list to find the least common bit for each position
    leastCommonString = ''.join(['1' if i == '0' else '0' for i in mostCommon])
    mostCommonString = ''.join(mostCommon)
    # Convert from binary to base 10
    gamma = int(mostCommonString, 2)
    epsilon = int(leastCommonString, 2)
    product = gamma * epsilon
    returnString = "Gamma: {}, Epsilon: {}, Product: {}"
    print(returnString.format(gamma, epsilon, product))

# Gets the life support rating for the given binaries
def getLifeSupportRating(binaries):
    oxygen = int(getLifeSupportSubsystem(binaries, True), 2)
    co2 = int(getLifeSupportSubsystem(binaries, False), 2)
    product = oxygen * co2
    returnString = "Oxygen: {}, CO2: {}, Product: {}"
    print(returnString.format(oxygen, co2, product))

# Handles a single life support subsystem (Oxygen or CO2)
def getLifeSupportSubsystem(binaries, isOxygen):
    contenders =  binaries
    index = 0
    while(len(contenders) > 1):
        mostCommonNum = getMostCommonBitFromPosition(contenders, index)
        # Stay in the list if your binary string should count for this index, mostCommonNum
        contenders = [x for x in contenders if binaryCounted(x, index, mostCommonNum, isOxygen)]
        index += 1
    return contenders[0]

# Import the binaries and put them into an array of strings
# NOTE: This will keep the newlines- we'll deal with that later
def importBinaries(path):
    file = open(path, 'r')
    binaries = file.readlines()
    file.close()
    return binaries

# Gets the most common bit for the given position among the binaries
def getMostCommonBitFromPosition(binaries, position):
    vals = [int(x[position], 2) for x in binaries]
    mean = float(sum(vals)) / len(binaries)
    # Return strings here to make it easier to recombine into a single string at the end
    if mean > .5:
        return "1"
    if mean == .5:
        return "2"
    return "0"

# Returns true if this binary string meets the conditions of its given subsystem
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