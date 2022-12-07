class FileTree:
    def __init__(self, files, dirs, parent, name):
        self.files = files
        self.dirs = dirs
        self.parent = parent
        self.name = name
    
    def calculateSize(self):
        sum = 0
        for file in self.files:
            sum += int(file[0])
        for dir in self.dirs:
            sum += self.dirs[dir].calculateSize()
        return sum
    
    def getSizesUnderLimit(self, limit):
        sum = 0
        if self.calculateSize() < limit:
            sum += self.calculateSize()
        for dir in self.dirs:
            sum += self.dirs[dir].getSizesUnderLimit(limit)
        return sum

def getAllDirectoriesOverSize(tree, limit):
    results = []
    meSize = tree.calculateSize()
    if (tree.calculateSize() > limit):
        results.append(tree)
    for dir in tree.dirs:
        results = results + getAllDirectoriesOverSize(tree.dirs[dir], limit)
    return results

def partTwo(tree):
    maxSize = 70000000
    requiredSpace = 30000000
    startingSpace = tree.calculateSize()
    availableSpace = maxSize - startingSpace
    limit = requiredSpace - availableSpace
    dirs = getAllDirectoriesOverSize(tree, limit)
    minSize = maxSize
    for dir in dirs:
        size = dir.calculateSize()
        if size < minSize:
            minSize = size
    print(minSize)

def buildFileStructure(inputs):
    startTree = FileTree([], {}, None, '/')
    currFile = startTree
    for line in inputs:
        ## Commands
        if '$' in line:
            if line == '$ cd ..':
                currFile = currFile.parent
            elif line == '$ cd /':
                currFile = startTree
            elif 'cd ' in line:
                newDir = line.split(' ')[2]
                currFile = currFile.dirs[newDir]
        elif 'dir ' in line:
            dirName = line.split(' ')[1]
            newTree = FileTree([], {}, currFile, dirName)
            currFile.dirs[dirName] = newTree
        else:
            parts = line.split(' ')
            newFile = (parts[0], parts[1])
            currFile.files.append(newFile)
    return startTree

def main():
    inputs = [line.rstrip() for line in open("input.txt")]
    tree = buildFileStructure(inputs)
    partTwo(tree)

if __name__ == "__main__":
    main()