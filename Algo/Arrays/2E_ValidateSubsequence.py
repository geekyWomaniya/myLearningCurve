def isValidSubsequence(array, inputSequence):
    idx = 0
    for i in range(len(array)):
        if array[i] == inputSequence[idx]:
            if array[i] == inputSequence[len(inputSequence)-1] and idx == len(inputSequence)-1:
                return True
            idx += 1
    
    return False

# output = isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, -2])
output = isValidSubsequence( [5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6])


print(output)















# def isValidSubsequence(array, inputSequence):
#     nums = []
#     array.sort()
#     inputSequence
#     sequenceCopy = inputSequence[:] 

#     sorted(sequenceCopy)
    
#     for i in range(len(array)):
#         if array[i] in sequenceCopy:
#             nums.append(array[i])
#             sequenceCopy.pop(0)
#             # print("--", inputSequence)

#     nums.sort()
#     print("nums--",nums)
#     print("inputSeq--",inputSequence)
#     return nums == inputSequence 

#     return True

# # output = isValidSubsequence([1,1,1,1],[1,1,1])
# output = isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[5, 1, 25, 22, 6, -1, 8, 10])

# print(output)