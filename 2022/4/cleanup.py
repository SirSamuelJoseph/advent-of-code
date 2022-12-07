def doesPairHaveOverlap(s1, e1, s2, e2):
    if s1 <= s2 and e1 >= e2:
        return True
    if s1 >= s2 and e1 <= e2:
        return True
    return False

def hasAnyOverlap(s1, e1, s2, e2):
    if s1 < s2 and e1 < s2:
        return False
    if s2 < s1 and e2 < s1:
        return False
    return True

def partOne(inputs):
    sum = 0
    for line in inputs:
        parts = line.split(',')
        partsOne = parts[0].split('-')
        partsTwo = parts[1].split('-')
        s1 = int(partsOne[0])
        e1 = int(partsOne[1])
        s2 = int(partsTwo[0])
        e2 = int(partsTwo[1])
        if doesPairHaveOverlap(s1, e1, s2, e2):
            sum += 1
    print(sum)

def partTwo(inputs):
    sum = 0
    for line in inputs:
        parts = line.split(',')
        partsOne = parts[0].split('-')
        partsTwo = parts[1].split('-')
        s1 = int(partsOne[0])
        e1 = int(partsOne[1])
        s2 = int(partsTwo[0])
        e2 = int(partsTwo[1])
        if hasAnyOverlap(s1, e1, s2, e2):
            sum += 1
    print(sum)


def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    partTwo(inputs)

if __name__ == "__main__":
    main()