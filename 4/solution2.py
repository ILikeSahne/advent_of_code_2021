import os
import sys

class BingoBoard:
    def __init__(self, inputs) -> None:
        board = []
        for i in inputs:
            row = []
            for num in i.split():
                row.append(int(num))
            board.append(row)
        self.board = board
        self.generateChecks()

    def generateChecks(self):
        checks = [
            # [0, 0], [1, 1],
            # [0, 4], [1, -1],
        ]

        for i in range(5):
            checks.append([0, i])
            checks.append([1, 0])

            checks.append([i, 0])
            checks.append([0, 1])

        self.checks = checks

    def bingo(self, numbers):
        i = 0
        while i < len(self.checks):
            pos = self.checks[i].copy()
            plus = self.checks[i + 1].copy()
            allPlaced = True
            for j in range(5):
                if not self.isPlaced(numbers, pos[0], pos[1]):
                    allPlaced = False
                    break
                pos[0] += plus[0]
                pos[1] += plus[1]
            if allPlaced:
                return numbers[len(numbers) - 1]
            i += 2
        return -1
    
    def isPlaced(self, numbers, x, y):
        bingoNum = self.board[y][x]
        for num in numbers:
            if num == bingoNum:
                return True
        return False

    def calcUnplaced(self, numbers):
        sum = 0
        for y in range(5):
            for x in range(5):
                if not self.isPlaced(numbers, x, y):
                    sum += self.board[y][x]

        return sum

def printNum():
    file_path = os.path.join(sys.path[0], "input.txt")
    input = open(file_path, 'r')
    lines = input.readlines()
    numbers = lines[0].split(',')
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    i = 2
    boards = []
    while i < len(lines):
        boards.append(BingoBoard(lines[i:i+5]))
        i += 6

    for i in range(len(numbers)):
        for index, b in enumerate(boards):
            bingo = b.bingo(numbers[0:i])
            if bingo != -1:
                if(len(boards) == 1):
                    b = boards[0]
                    print(bingo)
                    print("Board", index, "is Bingo")
                    unplaced = b.calcUnplaced(numbers[0:i])
                    print("Unplaced", unplaced)
                    print("Unplaced times last", unplaced * bingo)
                boards.remove(b)


printNum()