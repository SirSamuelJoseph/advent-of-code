## X/A = Rock, Y/B = Paper, Z/C = Scissors
def getScoreForRow(opp, player): 
    if player == 'X':
        if opp == 'A':
            return 1 + 3
        elif opp == 'B':
            return 1 + 0
        elif opp == 'C':
            return 1 + 6
    elif player == 'Y':
        if opp == 'A':
            return 2 + 6
        elif opp == 'B':
            return 2 + 3
        elif opp == 'C':
            return 2 + 0
    elif player == 'Z':
        if opp == 'A':
            return 3 + 0
        elif opp == 'B':
            return 3 + 6
        elif opp == 'C':
            return 3 + 3

def getScoreForRow2(opp, outcome):
    if opp == 'A':
        if outcome == 'X':
            return 3 + 0
        if outcome == 'Y':
            return 1 + 3
        if outcome == 'Z':
            return 2 + 6
    elif opp == 'B':
        if outcome == 'X':
            return 1 + 0
        if outcome == 'Y':
            return 2 + 3
        if outcome == 'Z':
            return 3 + 6
    elif opp == 'C':
        if outcome == 'X':
            return 2 + 0
        if outcome == 'Y':
            return 3 + 3
        if outcome == 'Z':
            return 1 + 6

def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    score = 0
    for input in inputs:
        score += getScoreForRow2(input[0], input[2]) 
    print(score)

if __name__ == "__main__":
    main()