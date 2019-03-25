def selectionSort(alist):
    for passNum in range(len(alist)-1, 0, -1):
        maxPos = 0
        for i in range(1, passNum+1):
            if alist[i] > alist[maxPos]:
                maxPos = i
        alist[maxPos], alist[passNum] = alist[passNum], alist[maxPos]

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
selectionSort(alist)
print(alist)
