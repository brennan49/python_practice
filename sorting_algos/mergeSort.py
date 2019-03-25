# Avg time is O(nlogn)
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist) > 1:
        mid = len(alist)//2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                alist[k] = leftHalf[i]
                i = i + 1
            else:
                alist[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalf):
            alist[k] = leftHalf[i]
            i = i + 1
            k = k + 1
        
        while j < len(rightHalf):
            alist[k] = rightHalf[j]
            j = j + 1
            k = k + 1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)