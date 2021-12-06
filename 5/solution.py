import os
import sys
import math

class Line:
    def __init__(self, line) -> None:
        pos = line.split(' ')
        self.start = self.toVec(pos[0])
        self.end = self.toVec(pos[2])
        self.pos = self.start.copy()
        xDiff = self.end[0] - self.start[0]
        yDiff = self.end[1] - self.start[1]
        self.plus = [self.sign(xDiff), self.sign(yDiff)]
        print(self.plus)

    def sign(self, x):
        if int(x) == 0:
            return 0
        return abs(x) / x

    def toVec(self, pos):
        vec = pos.split(',')
        for i in range(len(vec)):
            vec[i] = int(vec[i])
        return vec

    def move(self):
        if self.pos[0] == self.end[0] and self.pos[1] == self.end[1]:
            return True
        self.pos[0] += self.plus[0]
        self.pos[1] += self.plus[1]
        return False

    

def printNum():
    dic = {}
    input = readFile()
    maxX = 0
    maxY = 0
    lines = []
    for line in input:
        l = Line(line)
        if l.plus[0] * l.plus[1] != 0:
            continue
        maxX = bigger(maxX, l.start[0])
        maxX = bigger(maxX, l.end[0])
        maxY = bigger(maxY, l.start[1])
        maxY = bigger(maxY, l.end[1])
        lines.append(l)

    wires = []
    for i in range(maxY + 1):
        wire = []
        for j in range(maxX + 1):
            wire.append('.')
        wires.append(wire)
    
    for l in lines:
        while True:
            pos = str(int(l.pos[0])) + " " + str(int(l.pos[1]))
            if not pos in dic:
                dic[pos] = 1
            else:
                dic[pos] += 1
            wires[int(l.pos[1])][int(l.pos[0])] = dic[pos]
            if l.move():
                break

    for wire in wires:
        s = ""
        for x in wire:
            s += str(x)
        print(s)

    counter = 0
    for key in dic:
        if dic[key] > 1:
            counter += 1
    print("Amount of line overlappings is", counter)

def bigger(maxX, x):
    if x > maxX:
        return x
    return maxX

def readFile():
    file_path = os.path.join(sys.path[0], "input.txt")
    input = open(file_path, 'r')
    lines = input.readlines()
    return lines

printNum()