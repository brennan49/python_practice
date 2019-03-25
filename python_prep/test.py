class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))

class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        
        if a==1 and b==1:
            return 1
        else:
            return 0

# g1 = AndGate("G1")
# print(g1.getOutput())

def quadraticList(numList):
    smallest = numList[0]
    for i in numList:
        for j in numList:
            if i > j:
                break
            elif i <= j and i <= smallest:
                smallest = i
            else:
                pass
    return smallest
                

def linearList(numList):
    smallest = numList[0]
    for i in numList:
        if i < smallest:
            smallest = i

    return smallest


# print(quadraticList([1,6,4,7,8,5,4,56,7,1,90,5,4,6,65,76,0]))