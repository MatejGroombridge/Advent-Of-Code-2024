# Advent of Code
# Day 3

# Part 1
def part1():
    total = 0
    num1 = 0
    num2 = 0
    firstLength = 0
    
    with open("Day #3/input.txt", "r") as file:
        lines = file.readlines()
        
        for line in range(0, len(lines)):
            for char in range(0, len(lines[line])):
                if lines[line][char:char+4] == "mul(":
                    if lines[line][char+4].isnumeric() and lines[line][char+5] == ",":
                        num1 = int(lines[line][char+4])
                        firstLength = 1
                    elif lines[line][char+4:char+5].isnumeric() and lines[line][char+6] == ",":
                        num1 = int(lines[line][char+4:char+6])
                        firstLength = 2
                    elif lines[line][char+4:char+6].isnumeric() and lines[line][char+7] == ",":
                        num1 = int(lines[line][char+4:char+7])
                        firstLength = 3
                    else:
                        num1 = 0

                    if num1 != 0:
                        if lines[line][char+firstLength+5].isnumeric() and lines[line][char+firstLength+6] == ")":
                            num2 = int(lines[line][char+firstLength+5])
                        elif lines[line][char+firstLength+5:char+firstLength+6].isnumeric() and lines[line][char+firstLength+7] == ")":
                            num2 = int(lines[line][char+firstLength+5:char+firstLength+7])
                        elif lines[line][char+firstLength+5:char+firstLength+7].isnumeric() and lines[line][char+firstLength+8] == ")":
                            num2 = int(lines[line][char+firstLength+5:char+firstLength+8])
                        else:
                            num2 = 0
                        
                    total += num1 * num2
    print(total)

part1()