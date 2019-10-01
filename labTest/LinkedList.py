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

class List:
    def __init__(self, head = None):
        self.head = head

    def str(self):
        if self.size() is 0:
            return 'Empty LinkedList'
        else:
            s = ''
            temp = self.head
            while temp is not None:
                s = s + str(temp.data) + ' '
                temp = temp.next
            return s

    def size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def isEmpty(self):
        return self.size is 0

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.data
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next 
            temp.next = newNode
            temp.next.next = None

    def addHead(self, data):
        addNode = Node(data)
        if self.head is None:
            self.head = addNode
        else:
            temp = self.head
            self.head = addNode
            addNode.next = temp

    def isIn(self, data):
        temp = self.head
        while temp.data is not hNode and temp.next is not None:
            temp = temp.next
        return temp.data is data

    def before(self, data):
        if self.head is None or self.head.data is data:
            return
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
        tail = None
        if self.head.next is None:
            tail = self.head
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            tail = temp
            temp = temp.next
        return tail

    def removeHead(self):
        head = None
        if self.head is not None:
            head = self.head
            self.head = self.head.next
            head.next = None
        return head 

    #def addByIndex(self, index, data):

            
        