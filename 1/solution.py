import os
import sys

file_path = os.path.join(sys.path[0], "input.txt")
input = open(file_path, 'r')
lines = input.readlines()
prev = int(lines[0])
increaseCount = 0
for line in lines:
    x = int(line)
    if(x > prev):
        increaseCount += 1
    prev = x

print("Increased", increaseCount, "times")