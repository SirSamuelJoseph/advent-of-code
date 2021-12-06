def validatePassword(password, min, max, character):
    count = password.count(character)
    return count >= min and count <= max

def validatePassword2(password, index1, index2, character):
    return password[index2 - 1] != character if password[index1 - 1] == character else password[index2 - 1] == character

def countValidPasswords(inputs):
    count = 0
    for line in inputs:
        components = line.split(' ')
        nums = components[0].split('-')
        min, max = int(nums[0]), int(nums[1])
        character = components[1][0]
        if validatePassword2(components[2], min, max, character):
            count += 1
    return count

def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    print(countValidPasswords(inputs))

if __name__ == "__main__":
    main()