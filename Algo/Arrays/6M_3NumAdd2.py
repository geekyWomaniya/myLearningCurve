def threeNumberSum(array, targetSum):
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

output = threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6], 0)

print(output)