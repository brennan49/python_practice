def insertionSort(alist):
    for index in range(1, len(alist)):
        val = alist[index]
        position = index
        while position > 0 and alist[position-1] > val:
            alist[position] = alist[position-1]
            position = position - 1
        
        alist[position] = val

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
insertionSort(alist)
print(alist)