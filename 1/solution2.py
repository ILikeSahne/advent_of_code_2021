import os
import sys

def numOfIncreases():
    file_path = os.path.join(sys.path[0], "input.txt")
    input = open(file_path, 'r')
    lines = input.readlines()
    prev = sumOf3(lines, 0)
    increaseCount = 0
    for i, line in enumerate(lines):
        if(i > len(lines) - 3):
            break
        x = sumOf3(lines, i)
        if(x > prev):
            increaseCount += 1
        prev = x
    return increaseCount

def sumOf3(lines, pos):
    return int(lines[pos]) + int(lines[pos + 1]) + int(lines[pos + 2])

print("Increased", numOfIncreases(), "times")