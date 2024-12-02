# Advent of Code
# Day 1

def part1():
    leftList = []
    rightList = []
    total =  0
    difference = 0

    # split the input into two lists
    with open('Day #1/input.txt', 'r') as file:
        data = file.read()
        data = data.split('\n')
        for line in data:
            leftList.append(int(line.split('   ')[0]))
            rightList.append(int(line.split('   ')[1]))

    # sort the two lists
    leftList.sort()
    rightList.sort()

    # sum the differenc of elements of each list
    for i in range(len(leftList)):
        difference = abs(leftList[i] - rightList[i])
        total = total + difference

    return total

def part2():
    leftList = []
    rightList = []
    similarityScore =  0
    similarValues = 0

    # split the input into two lists
    with open('Day #1/input.txt', 'r') as file:
        data = file.read()
        data = data.split('\n')
        for line in data:
            leftList.append(int(line.split('   ')[0]))
            rightList.append(int(line.split('   ')[1]))

    # calculate simlarity score
    for i in range(len(leftList)):
        location = leftList[i]
        similarValues = rightList.count(location)
        similarityScore = similarityScore + similarValues * location
    
    return similarityScore

# print(part1())
print(part2())