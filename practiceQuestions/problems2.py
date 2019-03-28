# Question 1:
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.currentSize = 0

    def size(self):
        return self.currentSize

    def put(self, key):
        if self.root:
            self._put(key, self.root)
        else:
            self.root = TreeNode(key)
        self.currentSize = self.currentSize + 1

    def _put(self, key, currentNode):
        if currentNode.key > key: 
            if currentNode.hasLeftChild():
                self._put(key, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,parent=currentNode)
                self.currentSize = self.currentSize + 1
        else:
            if currentNode.hasrightChild():
               self._put(key, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, parent=currentNode)
                self.currentSize = self.currentSize + 1

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            return res

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        if currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def constructBST(self, bst, alist):
        for item in alist:
            bst.put(item)
        return bst
            


class TreeNode:
    def __init__(self, key, lc=None, rc=None, parent=None):
        self.key = key
        self.leftChild = lc
        self.rightChild = rc
        self.parent = parent

    def getKey(self):
        return self.key

    def hasLeftChild(self):
        return self.leftChild

    def hasrightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.hasleftChild == self

    def isRightChild(self):
        return self.parent and self.parent.hasrightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.hasLeftChild or self.hasrightChild)

    def hasAnyChildren(self):
        return self.hasLeftChild or self.hasrightChild

    def hasBothChildren(self):
        return self.hasLeftChild and self.hasrightChild

def findLCA(root, n1, n2):
    if root == None:
        return None
    elif root.key > n1 and root.key > n2:
        return findLCA(root.leftChild, n1, n2)
    elif root.key > n1 and root.key > n2:
        return findLCA(root.rightChild, n1, n2)
    else:
        return root

def findDistance(root, key):
    if root.key == key:
        return 0
    elif root.key > key:
        return 1 + findDistance(root.leftChild, key)
    else:
        return 1 + findDistance(root.rightChild, key)

def buildTree(values, n, node1, node2):
    bst = BinarySearchTree()
    bst.constructBST(bst, values)
    if not(node1 and node2):
        return -1
    n1 = bst.get(node1)
    n2 = bst.get(node2)

    node = findLCA(bst.root, node1, node2)

    if node1 == node2:
        return 0
    elif not (n1 and n2):
        return -1
    else:
        lca = findLCA(bst.root, node1, node2)
        distance = findDistance(lca, node1) + findDistance(lca, node2)
    return distance


print(buildTree([5,6,3,1,2,4], 6, 2, 7))



# Question 2:
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

# Time is O(n)

def isBalanced(str):
    strList = list(str)
    parenStack = Stack()
    curlStack = Stack()
    brackStack = Stack()
    carotStack = Stack()

    for item in strList:
        if item in '({[<':
            if item == '(':
                parenStack.push(item)
            elif item == '{':
                curlStack.push(item)
            elif item == '[':
                brackStack.push(item)
            else:
                carotStack.push(item)

        elif item in ')}]>':
            if item == ')' and not parenStack.isEmpty():
                parenStack.pop()
            elif item == '}' and not curlStack.isEmpty():
                curlStack.pop()
            elif item == ']' and not brackStack.isEmpty():
                brackStack.pop()
            elif item == '>' and not carotStack.isEmpty():
                carotStack.pop()
            else:
                return 0
    if parenStack.isEmpty() and curlStack.isEmpty() and brackStack.isEmpty() and carotStack.isEmpty():
        return 1
    else:
        return 0

# print(isBalanced('[]{}<>()'))
