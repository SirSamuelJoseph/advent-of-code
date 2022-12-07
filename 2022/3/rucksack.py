def getPriorityForLetter(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def getDoubledLetterPerLine(line):
    line1 = line[:len(line)//2]
    line2 = line[len(line)//2:]
    for letter in line1:
        if letter in line2:
            return letter

def getTripleOccurancePerThreeLines(lines):
    for letter in lines[0]:
        if letter in lines[1] and letter in lines[2]:
            return letter

def partTwo(inputs, sum):
    if len(inputs) < 3:
        print(sum)
    sum += getPriorityForLetter(getTripleOccurancePerThreeLines(inputs))
    return partTwo(inputs[3:], sum)
    

def partOne(inputs):
    sum = 0
    for line in inputs:
        sum += getPriorityForLetter(getDoubledLetterPerLine(line))
    print(sum)

def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    print(partTwo(inputs, 0))

if __name__ == "__main__":
    main()