import os
import sys

def calcMove():
    y = x = aim = 0
    file_path = os.path.join(sys.path[0], "input.txt")
    input = open(file_path, 'r')
    lines = input.readlines()
    for line in lines:
        words = line.split()
        direc = words[0]
        move = int(words[1])
        if(direc == "forward"):
            x += move
            y += aim * move
        elif(direc == "down"):
            aim += move
        elif(direc == "up"):
            aim -= move
    return x * y

print("Horizontal pos times depth is", calcMove())