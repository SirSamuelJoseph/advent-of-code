def advanceDay(state):
    oldState = list(state)
    for i in range(9):
        state[8 - i] = oldState[9 - i]
    # Add the zeroes to the 6 and 8 day piles
    state[6] += oldState[0]
    state[8] += oldState[0]
    return state

def advanceGivenDays(state, days):
    for i in range(days):
        state =  advanceDay(state)
        print("Day {}: {} Fish".format(i + 1, sum(state)))
    return sum(state)

def initState(inputs):
    initial = inputs[0].split(',')
    counts = [0] * 10
    for num in initial:
        counts[int(num)] += 1
    return counts

def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    counts = initState(inputs)
    advanceGivenDays(counts, 256)

if __name__ == "__main__":
    main()