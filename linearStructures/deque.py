class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

def palindromeChecker(palindrome):
    alist = list(palindrome)
    paldeque = Deque()

    for item in alist:
        paldeque.addRear(item)

    while not paldeque.isEmpty() and paldeque.size() > 1:
        if paldeque.removeRear() != paldeque.removeFront():
            return False
            
    return True

print(palindromeChecker(""))