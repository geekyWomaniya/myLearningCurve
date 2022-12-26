# def sortedSquaredArray(inputArray):
#     for i in range(len(inputArray)):
#         inputArray[i] = inputArray[i] * inputArray[i]

#     inputArray.sort()
#     return inputArray

def sortedSquaredArray(inputArray):
    sortedSquares = [0 for _ in inputArray]
    startIndex = 0
    endIndex = len(inputArray) - 1

    for i in reversed(range(len(sortedSquares))):
        startIndexValue = inputArray[startIndex]
        endIndexValue = inputArray[endIndex]
        
        print(sortedSquares[i])

        if abs(startIndexValue) < abs(endIndexValue):
            sortedSquares[i] = endIndexValue * endIndexValue
            endIndex -= 1
        else:
            sortedSquares[i] = startIndexValue * startIndexValue
            startIndex += 1
    
    return sortedSquares

output = sortedSquaredArray([-5, -4, -3, -2, -1, 0 , 9])

print(output)
