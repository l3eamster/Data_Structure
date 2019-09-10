from Class import node 
class list
    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def __str__(self):
        temp = self.head
        str = None
        while(temp.next != None):
            str = str + temp.data + ' '
            temp.data = temp.next
        str = str + temp.data
        return str

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        n = node(data)
        if self.head is None:
            self.head = n
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p

    def addHead(self, data):
        n = node(data, self.head)
        self.head = n
        self.size += 1

    def isIn(self, data):
        temp = self.head
        while temp.data != data and temp.next != None:
            temp = temp.next
        return temp.data == data

    def before(self, data):
        #return ref of node before node te me data hai

    def remove (self, data):
        #remove and return node te chai data

    def removeTail(self):
        #remove and return last node

    def removeHead(self):
        #remove and return first node