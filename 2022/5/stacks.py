
def getColumnNumberFromIndex(index):
    if index == 1:
        return 0
    else:
        diff = index - 1
        return diff // 4

def buildStateFromInputs(inputs):
    columns = 9
    state = [[] for i in range(columns)]
    for line in inputs:
        for index, letter in enumerate(line):
            if letter == '[':
                column = getColumnNumberFromIndex(index + 1)
                state[column].append(line[index + 1])
    return state
            
def moveCrates(state, fromCol, toCol):
    topBlock = state[fromCol].pop(0)
    state[toCol].insert(0, topBlock)
    return state

def moveCrates2(state, fromCol, toCol, count):
    blocksToMove = []
    for x in range(count):
        blocksToMove.append(state[fromCol].pop(0))
    # Reverse the list to add them in the right order
    blocksToMove.reverse()
    for x in range(count):
        state[toCol].insert(0, blocksToMove[x])
    return state

def partOne(inputs):
    state = buildStateFromInputs(inputs)
    for line in inputs:
        if 'move' in line:
            chunks = line.split(' ')
            iterations = int(chunks[1])
            fromCol = int(chunks[3]) - 1
            toCol = int(chunks[5]) - 1
            for x in range(iterations):
                state = moveCrates(state, fromCol, toCol)
    result = ''
    for x in range(len(state)):
        if (len(state[x]) > 0):
            result = result + (state[x][0])
    print(result)

def partTwo(inputs):
    state = buildStateFromInputs(inputs)
    for line in inputs:
        if 'move' in line:
            chunks = line.split(' ')
            iterations = int(chunks[1])
            fromCol = int(chunks[3]) - 1
            toCol = int(chunks[5]) - 1
            state = moveCrates2(state, fromCol, toCol, iterations)
    result = ''
    for x in range(len(state)):
        if (len(state[x]) > 0):
            result = result + (state[x][0])
    print(result)




def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    partTwo(inputs)

if __name__ == "__main__":
    main()