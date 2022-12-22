def threeNumberSum(array, targetSum):
    array.sort()
    resultant = []
    finalList = []
    i = 0
    for i in array:
        for j in array:
            for k in array:
                if i == j or j == k or k == i:
                    continue
                elif i + j + k == targetSum:
                    # resultant.append(i) 
                    # resultant.append(j) 
                    # resultant.append(k)
                    if i > j and i > k: 
                        resultant.append(i)
                        if j > k:
                            resultant.append(j)
                            resultant.append(k)
                        elif j < k:
                            resultant.append(k)
                            resultant.append(j)
                        resultant.sort()

                    
                    if j > i and j > k: 
                        resultant.append(j)
                        if i > k:
                            resultant.append(i)
                            resultant.append(k)
                        elif i < k:
                            resultant.append(k)
                            resultant.append(i)
                        resultant.sort()
                    
                    if k > i and k > j: 
                        resultant.append(k)
                        if i > j:
                            resultant.append(i)
                            resultant.append(j)
                        elif i < j:
                            resultant.append(j)
                            resultant.append(i)
                        resultant.sort()

                    finalList.append(resultant)
                    resultant = []
                    # i += 1
    print("**",finalList)
    print("**********************")
    uniqueData = [list(x) for x in set(tuple(x) for x in finalList)]
    uniqueData.sort(key=lambda x: x[0])
    # print("uniqueData", uniqueData)
    # print("****", finalList)
    # # finalList =  set(finalList)
    # print("****", finalList)
    if len(uniqueData) < 1:
        return []
    else: 
        return uniqueData

output = threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6], 0)
# output = threeNumberSum([1, 2, 3], 6)

print(output)