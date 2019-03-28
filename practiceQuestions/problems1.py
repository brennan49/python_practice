from pprint import pprint

# Question 1:

def get_all_substrings(string, k):
    substring = []
    i = 0
    while k <= len(string):
        substring.append(string[i:k])
        i = i + 1
        k = k + 1
    return substring

def getSubstringRepeat(string, k):
    subList = get_all_substrings(string,k)
    retList = []
    for item in subList:
        count = 0
        repeatDict = {}
        for char in item:
                if char in repeatDict:
                    count = count + 1
                else:
                    repeatDict[char] = None
        repeatDict.clear()
        if count == 1:
            retList.append(item)

    return retList

# print(getSubstringRepeat('generalkerby', 4))


# Question 2:
'''
    O(n) timing due to having to iterate through the whole list.  However memory is O(n*k) where
    k is the total number of unique shots in the list.
'''
def findIntersections(inputDict, length):
    prevMax = None
    total = 0
    totals = []
    for key,value in inputDict.items():
        currStart = value['start']
        currMax = value['max']
        if prevMax == None:
            prevMax = currMax
            total = value['count']
        elif currStart < prevMax:
            if prevMax < currMax:
                prevMax = currMax
            total = total + value['count']
        else:
            totals.append(total)
            total = value['count']
            prevMax = currMax
    totals.append(total)
    return totals


def getSubsequences(inputList):
    shotDict = {}
    elem = 0
    dictLength = 0

    for item in inputList:
        if item in shotDict:
            shotDict[item]['count'] += 1
            shotDict[item]['max'] = elem
        else:
            shotDict[item] = {
                'count': 1,
                'start': elem,
                'max': elem
            }
            dictLength += 1
        elem += 1

    if dictLength == len(inputList):
        subseqList = [1] * len(inputList)
        return subseqList
    else:
        return findIntersections(shotDict, len(inputList))

print(getSubsequences(['a','b','a','b','c','b','a','c','a','d','e','f','e','g','d','e','h','i','j','h','k','l','i','j']))
print(getSubsequences(['a','b','a','b','c','d','e','e','f','d','e','f','f','g','i','h','h','g','j']))