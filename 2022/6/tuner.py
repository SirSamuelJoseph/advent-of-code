def hasRepeatChars(input):
    listVersion = list(input)
    setVersion = set(listVersion)
    return len(listVersion) == len(setVersion)

def solution(input, consecutive):
    index = 0
    found = False
    while (not found):
        found = hasRepeatChars(input[index: index + consecutive])
        if not found:
            index += 1
    print(index + consecutive)


def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    solution(inputs[0], 14)

if __name__ == "__main__":
    main()