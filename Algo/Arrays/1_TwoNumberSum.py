######################## SOLUTION 01
# def twoNumberSum(array, targetSum):
#     resultant = []
    
#     for i in array:
#         for j in array:
#             if i == j:
#                 continue
#             elif i + j == targetSum:
#                 resultant.append(i)
#                 resultant.append(j)
#                 return resultant
#     return resultant

# def twoNumberSum2(array, targetSum):
    # nums = {}
    # for num in array:
    #     potentialNum = targetSum - num

    #     if potentialNum in nums:
    #         return [potentialNum, num]
    #     else:
    #         nums[num] = True
    
    # return[]

def twoNumberSum3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1
    
    return []


# output = twoNumberSum([10,20,30],40)
# output = twoNumberSum2([10,20,30],40)
output = twoNumberSum3([10,20,30],40)

print(output)