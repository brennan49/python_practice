from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for item in fplist:
        if item == "(":
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif item.isnumeric():
            currentTree.setRootVal(int(item))
            currentTree = pStack.pop()
        elif item in '+-/*':
            currentTree.setRootVal(item)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif item == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError("token '{}' is not a valid integer".format(item))
    
    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder()  #defined and explained in the next section

# buildParseTree("( 3 + ( 4 * 6 ) )")

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

def postOrderEval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postOrderEval(tree.getLeftChild())
        res2 = postOrderEval(tree.getRightChild())
        if res1 and res2:
            fn = opers[tree.getRootVal()]
            return fn(res1, res2)
        else:
            return tree.getRootVal()

def printExp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printExp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printExp(tree.getRightChild()) + ')'
    return sVal

print(printExp(pt))