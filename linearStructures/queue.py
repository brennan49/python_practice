import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self):
        if self.currentTask != None:
            return True
        return False

    def startNext(self, newTask):
        if self.currentTask == None:
            self.currentTask = newTask
            self.timeRemaining = newTask.pages * 60/self.pagerate
        
class Task:
    def __init__(self, time):
        self.pages = random.randrange(1,21)
        self.timestamp = time

    def getTimestamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timestamp

def simulation(numSeconds, pagesPerMinute):
    labPrinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            newTask = Task(currentSecond)
            printQueue.enqueue(newTask)
        if not labPrinter.busy() and not printQueue.isEmpty():
            curTask = printQueue.dequeue()
            labPrinter.startNext(curTask)
            waitTime = curTask.waitTime(currentSecond)
            waitingTimes.append(waitTime)
        
        labPrinter.tick()

    avgTime = sum(waitingTimes)/len(waitingTimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(avgTime,printQueue.size()))        

def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600, 5)