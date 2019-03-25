# Extra inefficient version
def bubbleSort(alist):
    for passNum in range(len(alist)-1, 0, -1):
        for i in range(passNum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1],alist[i]
    
    return alist

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
bubbleSort(alist)
print(alist)

# Optimized version
def shortBubbleSort(alist):
    count = 1

    for passNum in range(len(alist)-1, 0, -1):
        print(passNum)
        if count == 0:
            print(passNum)
            break
        else:
            count = 0;
        for i in range(passNum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1],alist[i]
                count = count + 1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)
