def advanceDay(state):
    newFish = []
    fishToAdd = 0
    for fish in state:
        num = int(fish)
        if num > 0:
            newFish.append(num - 1)
        elif num == 0:
            newFish.append(6)
            fishToAdd += 1
    for i in range(fishToAdd):
        newFish.append(8)
    return newFish

def advanceDay2(state):
    newFish = [int(x) - 1 if int(x) > 0 else 6 for x in state]
    for i in range(state.count(0)):
        newFish.append(8)
    return newFish

def advanceDay3(state):
    oldState = list(state)
    for i in range(9):
        state[8 - i] = oldState[9 - i]
    # Add the zeroes to the 6 and 8 day piles
    state[6] += oldState[0]
    state[8] += oldState[0]
    return state

def advanceGivenDays(state, days):
    for i in range(days):
        state =  advanceDay3(state)
        print("Day {}: {} Fish".format(i + 1, sum(state)))

def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    initial = inputs[0].split(',')
    counts = [0] * 10
    for num in initial:
        counts[int(num)] += 1
    advanceGivenDays(counts, 80)

if __name__ == "__main__":
    main()