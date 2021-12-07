def getSumFromVals(vals, target):
    if len(vals) == 0:
        return -1
    dest = target - vals[0]
    if dest not in vals[1:]:
        return getSumFromVals(vals[1:], target)
    return  dest * vals[0]

def getSumFromThreeVals(vals, target):
    dest = target - vals[0]
    possible = getSumFromVals(vals, dest)
    if getSumFromVals(vals, dest) != -1:
        return vals[0] * possible
    else:
        return getSumFromThreeVals(vals[1:], target)

def main():
    inputs = [int(line.rstrip()) for line in open("input.txt")]
    print(getSumFromThreeVals(inputs, 2020))

if __name__ == "__main__":
    main()