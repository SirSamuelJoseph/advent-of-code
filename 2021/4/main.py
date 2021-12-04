class Board:
    def __init__(self, rows):
        self.rows = rows
    
    def hasBoardWon(self, drawn):
        # Horizontal victory?
        hrows = [row for row in self.rows if set(row) <= set(drawn)]
        if len(hrows) > 0:
            return True
        
        # Vertical victory?
        for i in range(len(self.rows)):
            vvals = [row[i] for row in self.rows if row[i] in drawn]
            if len(vvals) == len(self.rows):
                return True
    
    def getScore(self, drawn):
        sum = 0
        for rInd, row in enumerate(self.rows):
            for cInd in range(len(self.rows)):
                val = self.rows[rInd][cInd]
                if val not in drawn:
                    sum += int(val)
        return sum * int(drawn[-1])


class GameState:
    def __init__(self, path, boardSize):
        inputs = [line.rstrip() for line in open(path)]
        self.draws = inputs[0].split(",")
        self.drawn = []
        boards = []
        for i in range(1, len(inputs[1:]), boardSize + 1):
            rows = []
            for j in range(boardSize):
                row = inputs[i + j + 1].split()
                rows.append(row)
            boards.append(Board(rows))
        self.boards = boards

    def draw(self):
        drawn = self.draws[:len(self.drawn) + 1]
        self.drawn = drawn
    
    def isGameOver(self):
        for board in self.boards:
            if board.hasBoardWon(self.drawn):
                return True
        return False

    def playGame(self):
        while not self.isGameOver():
            self.draw()
        for board in self.boards:
            if board.hasBoardWon(self.drawn):
                return board.getScore(self.drawn)
    
    def playGameUntilLastWin(self):
        while len(self.boards) > 1:
            while not self.isGameOver():
                self.draw()
            for board in self.boards:
                if board.hasBoardWon(self.drawn):
                    self.boards.remove(board)
        return self.playGame()
    
        
        

state = GameState("input.txt", 5)
print(state.playGameUntilLastWin())