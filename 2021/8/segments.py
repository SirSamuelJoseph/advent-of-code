def getOccurencesOfGivenDigitsCount(output, digits):
    count = 0
    for val in output:
        if len(val) in digits:
            count += 1
    return count

def getTotalOccurencesofAllGivenDigits(inputs, digits):
    count = 0
    for input in inputs:
        print(input)
        output = input.split('|')[1].split()
        count += getOccurencesOfGivenDigitsCount(output, digits)
    return count

def getTotalOccurencesofAllDigits(inputs):
    count = 0
    for input in inputs:
        guide = ['' for x in range(10)]
        components = input.split('|')
        displays = components[0].strip().split()
        for pattern in displays:
            key = len(pattern)
            if key == 2:
                guide[1] = ''.join(sorted(pattern))
            elif key == 3:
                guide[7] = ''.join(sorted(pattern))
            elif key == 4:
                guide[4] = ''.join(sorted(pattern))
            elif key == 7:
                guide[8] = ''.join(sorted(pattern))
        guide = completeGuide(guide, displays)
        outputs = components[1].split()
        builder = ""
        for digit in outputs:
            for key, val in enumerate(guide):
                if ''.join(sorted(digit)) == val:
                    builder += str(key)
        count += int(builder)
        print(builder)
    return count

def completeGuide(guide, inputs):
    # Find the top letter - difference between 7 and 1
    topLetter = list(set(guide[7]) - set(guide[1]))[0]
    # Find the middle letter - only common between both values of length 5 (2 and 5) and 4
    fives = [x for x in inputs if len(x) == 5]
    for elem in fives:
        if len(set(elem).intersection(set(guide[1]))) == 2:
            guide[3] = ''.join(sorted(elem))
            fives.remove(elem)
    commonFives = set(fives[0]).intersection(set(fives[1]))

    middleLetter = list(set(guide[4]).intersection(commonFives))[0]
    # Get zero by looking for 6 length string without the middle leter
    zero = [x for x in inputs if set(x) - set(middleLetter) == set(x) and len(x) == 6]
    guide[0] = ''.join(sorted(zero[0]))

    sixes = [x for x in inputs if len(x) == 6 and ''.join(sorted(x)) != guide[0]]
    # It's going to be six or nine- check overlap with 1 to see which
    if len(set(sixes[0]).intersection(set(guide[1]))) == len(guide[1]):
        guide[6] = ''.join(sorted(sixes[1]))
        guide[9] = ''.join(sorted(sixes[0]))
    else:
        guide[9] = ''.join(sorted(sixes[1]))
        guide[6] = ''.join(sorted(sixes[0]))

    # Get top right letter
    topRightLetter = list(set(guide[8]) - set(guide[6]))[0]
    if topRightLetter in fives[0]:
        guide[2] = ''.join(sorted(fives[0]))
        guide[5] = ''.join(sorted(fives[1]))
    else:
        guide[5] = ''.join(sorted(fives[0]))
        guide[2] = ''.join(sorted(fives[1]))

    return guide

def getLenKey(val):
    return [6, 2, 5, 5, 4, 5, 6,3,7,6][val]

def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    print(getTotalOccurencesofAllDigits(inputs))

if __name__ == "__main__":
    main()