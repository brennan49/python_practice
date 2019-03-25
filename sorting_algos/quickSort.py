def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitPoint-1)
        quickSortHelper(alist,splitPoint+1, last)

def swap(alist, x, y):
    alist[x], alist[y] = alist[y], alist[x]

def get_pivot(alist, low, hi):
    mid = (low+hi)//2
    pivot = hi
    if alist[low] < alist[mid]:
        if alist[mid] < alist[hi]:
            pivot = mid
        elif alist[low] > alist[hi]:
            pivot = low

    return pivot

def partition(alist, low, hi):
    print("partition begin: ")
    pivot = get_pivot(alist, low, hi)
    pivotValue = alist[pivot]
    print("pivot value: ", pivotValue)
    alist[low], alist[pivot] = alist[pivot], alist[low]

    border = low
    
    for compare in range(low+1, hi+1):
        if alist[compare] < pivotValue:
            print("swap value: ", alist[compare])
            border = border + 1
            swap(alist, border, compare)
            compare = compare + 1
        else:
            compare = compare + 1

    print("final border value: ", border)
    swap(alist, low, border)
    print("final list for pass:", alist)
    return border


alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
