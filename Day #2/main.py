# Advent of Code
# Day 2

# part 2: cheated by finding out you can brute force it. all my own code though.

def part1():
    ascending = ""
    valid = True
    separation = 0
    validRecords = 0

    # split the input into an array of records
    with open('Day #2/input.txt') as inputs:
        records = inputs.readlines()

    for i in range(len(records)):
        record = records[i].split()  # split the record into an array of strings

        # save ascending status
        if int(record[0]) < int(record[1]):
            ascending = "ascending"
        else:
            ascending = "descending"

        # check for valid records
        for n in range(len(record)):
            if n != len(record) - 1:
                separation = abs(int(record[n]) - int(record[n+1]))

                if separation < 1 or separation > 3:
                    valid = False
                    break

                if ascending == "ascending" and (int(record[n + 1]) < int(record[n])):
                    valid = False
                    break

                if ascending == "descending" and int(record[n + 1]) > int(record[n]):
                    valid = False
                    break
            
            separation = 0
        
        if valid:
            validRecords += 1

        valid = True
    
    return validRecords

# attempt 1
# consistently returns 304, which is incorrect

# def part2():
#     ascending = ""
#     valid = True
#     separation = 0
#     validRecords = 0
#     errorIndex = 0

#     # split the input into an array of records
#     with open('Day #2/input.txt') as inputs:
#         records = inputs.readlines()

#     for i in range(len(records)):
#         record = records[i].split()  # split the record into an array of strings

#         # save ascending status
#         if int(record[0]) < int(record[1]):
#             ascending = "ascending"
#         else:
#             ascending = "descending"

#         # check for valid records
#         for n in range(len(record)):
#             if n != len(record) - 1:
#                 separation = abs(int(record[n]) - int(record[n+1]))

#                 if separation < 1 or separation > 3:
#                     valid = False
#                     errorIndex = n + 1
#                     break

#                 if ascending == "ascending" and (int(record[n + 1]) < int(record[n])):
#                     valid = False
#                     errorIndex = n + 1
#                     break

#                 if ascending == "descending" and int(record[n + 1]) > int(record[n]):
#                     valid = False
#                     errorIndex = n + 1
#                     break
            
#             separation = 0

#         if valid == False:
#             print("NEXT")
#             print(record)
#             print(errorIndex)

#             valid = True
#             record.pop(errorIndex)
#             print(record)

#             if int(record[0]) < int(record[1]):
#                 ascending = "ascending"
#             else:
#                 ascending = "descending"

#             for n in range(len(record)):
#                 if n != len(record) - 1:
#                     separation = abs(int(record[n]) - int(record[n+1]))

#                     if separation < 1 or separation > 3:
#                         valid = False
#                         break

#                     if ascending == "ascending" and (int(record[n + 1]) < int(record[n])):
#                         valid = False
#                         break

#                     if ascending == "descending" and int(record[n + 1]) > int(record[n]):
#                         valid = False
#                         break
                
#                 separation = 0
            
#             if valid:
#                 print("valid")
#             else:
#                 print("invalid")

#         if valid:
#             # print("valid")
#             validRecords += 1

#         valid = True
#         errorIndex = 0
    
#     return validRecords


# attempting to brute force the solution
def part2():
    ascending = ""
    valid = True
    separation = 0
    validRecords = 0

    # split the input into an array of records
    with open('Day #2/input.txt') as inputs:
        records = inputs.readlines()

    for i in range(len(records)):
        record = records[i].split()  # split the record into an array of strings

        # save ascending status
        if int(record[0]) < int(record[1]):
            ascending = "ascending"
        else:
            ascending = "descending"

        # check for valid records
        for n in range(len(record)):
            if n != len(record) - 1:
                separation = abs(int(record[n]) - int(record[n+1]))

                if separation < 1 or separation > 3:
                    valid = False
                    break

                if ascending == "ascending" and (int(record[n + 1]) < int(record[n])):
                    valid = False
                    break

                if ascending == "descending" and int(record[n + 1]) > int(record[n]):
                    valid = False
                    break
            
            separation = 0

        if valid == False:
            
            for p in range(len(record)):
                record = records[i].split()
                record.pop(p)

                if int(record[0]) < int(record[1]):
                    ascending = "ascending"
                else:
                    ascending = "descending"

                for n in range(len(record)):
                    if n != len(record) - 1:
                        separation = abs(int(record[n]) - int(record[n+1]))

                        if separation < 1 or separation > 3:
                            valid = False
                            break
                        elif ascending == "ascending" and (int(record[n + 1]) < int(record[n])):
                            valid = False
                            break
                        elif ascending == "descending" and int(record[n + 1]) > int(record[n]):
                            valid = False
                            break
                        else:
                            valid = True

                if valid:
                    break
        
        if valid:
            validRecords += 1

        valid = True
    
    return validRecords

# print("There are " + str(main()) + " valid records.")
print("There are " + str(part2()) + " valid records.")