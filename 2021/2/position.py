def getPositionFromDirections(directions):
    depth, horizontal = 0,0
    for direction in directions:
        components = direction.split()
        angular, radial = components[0], int(components[1])
        if angular == 'forward':
            horizontal += radial
        elif angular == 'down':
            depth += radial
        elif angular == 'up':
            depth -= radial
    return depth * horizontal

def getComplexPositionFromDirections(directions):
    depth, horizontal, aim = 0,0,0
    for direction in directions:
        components = direction.split()
        angular, radial = components[0], int(components[1])
        if angular == 'forward':
            horizontal += radial
            depth += (aim * radial)
        elif angular == 'down':
            aim += radial
        elif angular == 'up':
            aim -= radial
    return depth * horizontal

def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    print(getPositionFromDirections(inputs))
    print(getComplexPositionFromDirections(inputs))

if __name__ == "__main__":
    main()