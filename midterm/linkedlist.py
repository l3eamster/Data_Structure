class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

import math
class List:

    def __init__(self, head = None):
        self.head = head

    def __str__(self):
        if self.size() is 0:
            return 'Empty Linkedlist'
        else:
            temp = self.head
            s = ''
            while temp is not None:
                s += str(temp.data)+' '
                temp = temp.next
            return s

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def isEmpty(self):
        return self.size() is 0

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while True:
                if temp.next is None:
                    temp.next = newNode
                    break
                else:
                    temp = temp.next
        
    def addHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def isIn(self, data):
        temp = self.head
        while temp.data is not data and temp.next is not None :
            temp = temp.next
        return temp.data is data

    def before(self, data):
        if self.head is None or self.head.data is data:
            return None
        else: 
            temp = self.head
            found = False
            while temp.next is not None:
                if temp.next.data is data:
                    found = True
                    break 
                temp = temp.next
            if found:
                return temp
            else: 
                return None

    def remove(self, data):
        dataRef = self.before(data)
        removeNode = None
        if dataRef is not None:
            temp = self.head
            while temp.next is not dataRef:
                temp = temp.next
            removeNode = temp.next
            temp.next = temp.next.next
        else: 
            if self.head.data == data and self.head is not None:
                removeNode = self.head
                self.head = self.head.next
        return removeNode

    def removeTail(self):
        removeNode = None
        if self.head is not None:
            if self.head.next is None:
                removeNode  = self.head
                self.head = None
            else:
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next
                removeNode = temp.next
                temp.next = None
        return removeNode

    def removeHead(self):
        h = self.head
        if self.head != None:
            self.head = self.head.next
            if self.head != None:
                h.next = None
        return h

    def addByIndex(self, index, data):
        # if isinstance(data, Node):
        #     newNode = data
        # else:
        #     newNode = Node(data)  
        newNode = Node(data)
        if index == 0:
            if self.head == None:
                self.head = newNode
            else:
                newNode.next = self.head
                self.head = newNode
        else:
            temp = self.head
            for i in range(0, index-1):
                temp = temp.next
            aNode = temp.next
            temp.next = newNode
            newNode.next = aNode

    def removeByIndex(self, index):
        removedNode = None
        if index == 0:
            if self.head != None:
                removedNode = self.head
                self.head = self.head.next
                removedNode.next = None
        else:
            temp = self.head
            for i in range(0, index - 1):
                temp = temp.next
            removedNode = temp.next
            temp.next = temp.next.next
            removedNode.next = None
        return removedNode

    def bottomUp(self, percent):
        if self.size() is 0:
            return 'Empty Linked List'
        if percent is 100 or 0:
            return
        count = math.floor(int(percent / 10))
        for i in range(0, count):
            self.append(self.removeHead())
        return self

    def deBottomUp(self, percent):
        if self.size() is 0:
            return 'Empty Linked List'
        if percent is 100 or 0:
            return
        n = math.floor(int(percent / 10))
        for i in range(0, n):
            self.addHead(self.removeTail())
        return self
        

    def riffle(self, percent):
        n = math.floor(int(percent / 10))
        loop = self.size() - n
        if n <= 5:
            loop = n-1
        index = 1
        for i in range(0, loop):
            temp = self.removeByIndex(n)
            self.addByIndex(index, temp)
            n += 1
            index += 2
        return self
        

    def deRiffle(self, percent):
        n = math.floor(int(percent / 10)) 
        indexToAdd = self.size() - 1
        if n > 5:
            n = self.size() - n
        else:
            n = n - 1
            indexToAdd = n * 2
        for i in range(0, n):
            temp = self.removeByIndex(i + 1)
            self.addByIndex(indexToAdd, temp)
        return self

l = List()

for i in range(1, 11):
    l.append(i)

l.append('A')
print(l)
print('bottomup:', l.bottomUp(50))
print('riffle:', l.riffle(50))
print('deriffle:', l.deRiffle(50))
print('debottomup:', l.deBottomUp(50))
print('')

# a = Node('A')
# my = List(a)
# my.append('B')
# my.append('C')
# my.addHead('0')

# print(my)
# my.removeHead()
# print(my)
# print(my.isIn('B'))
# my.remove('G')
# print(my)