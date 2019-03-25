# O(logn)
def binary_search(alist, item):
    start = 0
    end = len(alist) - 1
    found = False

    while start <= end and not found:
        middle = (end + start)//2
        if alist[middle] == item:
            found = True
        elif alist[middle] < item:
            start = middle + 1
        elif alist[middle] > item:
            end = middle - 1
        else:
            return found

    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))

print(9//2)