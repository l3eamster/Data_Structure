from ClassNode  import Node 
import math
class List:
    def __init__(self, head = None):
        self.head = head

    def __str__(self):
        if self.size() is 0:
            return 'Empty Linked List'
        else:
            temp = self.head
            s = ''
            while temp is not None:
                s += str(temp.data) + ' '
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
        return self.size() == 0

    def append(self, data):
        # if isinstance(data, Node):
        #     newNode = data
        # else:
        #     newNode = Node(data) 
        newNode = Node(data)           
        if(self.head == None):
            self.head = newNode
        else:
            temp = self.head
            while True:
                if temp.next == None:
                    temp.next = newNode
                    break
                temp = temp.next

    def addHead(self, data):
        if isinstance(data, Node):
            newNode = data
        else:
            newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode


    def isIn(self, data): #check wa me data in list
        temp = self.head
        while temp.data != data and temp.next != None:
            temp = temp.next
        return temp.data is data
        

    def before(self, data):    #return ref of node before node te me data hai
        if self.head == None or self.head.data == data:
            return None
        else:
            temp = self.head
            found = False
            while temp.next != None:
                if(temp.next.data == data):
                    found = True
                    break
                temp = temp.next
            if found:
                return temp
            else:
                return None

    def remove (self, data):   #remove and return node te chai data
        dataRef = self.before(data)
        removedNode = None
        if dataRef != None: # ถ้า data not head
            temp = self.head
            while temp != dataRef:
                temp = temp.next
            removedNode = temp.next
            temp.next = temp.next.next
        else:
            if self.head != None and self.head.data == data:
                removedNode = self.head
                self.head = self.head.next
        return removedNode


    def removeTail(self):  #remove and return last node
        tail = None
        if self.head != None:
            if self.head.next == None: #if have one
                tail = self.head
                self.head = None
            else:
                temp = self.head
                while temp.next.next != None:
                    temp = temp.next
                tail = temp.next
                temp.next = None
        return tail

    def removeHead(self):  #remove and return first node
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
        
