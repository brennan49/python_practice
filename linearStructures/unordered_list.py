class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newItem):
        self.data = newItem

    def setNext(self, node):
        self.next = node

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        temp = self.head
        while temp != None:
            count = count + 1
            temp = temp.getNext()

        return count

    def search(self, item):
        current = self.head
        while current != None:
            currItem = current.getData()
            if currItem == item:
                return True

            current = current.getNext()

        return False

    def remove(self, item):
        prev = None
        curr = self.head

        if self.head.getData() == item:
            self.head = curr.getNext()

        while curr != None:
            currItem = curr.getData()
            if currItem == item and prev != None:
                prev.setNext(curr.getNext())
                break
            else:
                prev = curr
                curr = curr.getNext()


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
