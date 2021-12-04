def countIncreases(nums):
    count = 0
    for i in range(1, len(nums)):
        if int(nums[i - 1]) < int(nums[i]):
            count += 1
    return count

def countIncreasesWindows(nums, windowSize):
    count = 0
    for i in range(0, len(nums) - windowSize):
        if int(nums[i]) < int(nums[i + windowSize]):
            count += 1
    return count

def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    print(countIncreases(inputs))
    print(countIncreasesWindows(inputs, 3))

if __name__ == "__main__":
    main()