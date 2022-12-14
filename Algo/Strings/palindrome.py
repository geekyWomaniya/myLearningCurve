# Palindrome

def isPalindrome(inputString):
    for i in range(int(len(inputString)/2)):
        # print(inputString[-i-1])
        if inputString[-i-1] != inputString[i]:
            return False
    return True

inputString = "abca"

output = isPalindrome(inputString)

print(output)