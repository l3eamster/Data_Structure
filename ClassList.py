from ClassNode  import Node 
class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.size() is 0:
            return 'Empty Linked List'
        else:
            temp = self.head
            s = ''
            while temp is not None:
                s += temp.data
                s += ' '
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
        if len(data) is not 0:
            if self.size() is 0:
                n = Node(data)
                self.head = n
                self.tail = n
            else:
                n = Node(data)
                self.tail.next = n
                self.tail = n

    def addHead(self, data):
        if len(data) is  not 0:
            if self.size() is 0:
                n = Node(data)
                self.head = n
            else:
                n = Node(data)
                n.next = self.head
                self.head = n

    def isIn(self, data):
        temp = self.head
        while temp.data != data and temp.next != None:
            temp = temp.next
        return temp.data == data
        

    def before(self, data):    #return ref of node before node te me data hai
        temp = self.head
        while temp is not None:
            if temp.data is data:
                return None if temp.prev is None else temp.prev
            else:
                temp = temp.next
        return None

    def remove (self, data):   #remove and return node te chai data
        temp = self.head
        while temp is not None:
            if str(temp.data) is str(data):
                if temp.prev is None and temp.next is None:
                    self.head = None
                    self.tail = None
                
                if temp.prev is not None and temp.next is None:
                    self.tail = temp.prev
                    self.tail.next = None
                    temp.prev = None

                if temp.prev is None and temp.next is not None:
                    self.head = temp.next
                    self.head.prev = None
                    temp.next = None

                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp.next = None
                    temp.prev = None
                return temp
            else:
                temp = temp.next
        return None


    def removeTail(self):  #remove and return last node
        temp = self.tail
        if temp is not None:
            return self.remove(temp.data)

    def removeHead(self):  #remove and return first node
        temp = self.head
        if temp is not None:
            return self.remove(temp.data)

#     def bottomUp(self, percent):
#     if self.size is 0:
#         return 'Empty Linked List'
#     if percent is 100 or 0:
#         return
#     count = int(self.size * (percent / 100))

#     for j in range(count):
#         temp = self.head
#         self.remove(self.head.data)
#         self.append(temp.data)
        

#     # #link tail->head
#     # self.head.prev = self.tail
#     # self.tail.next = self.head

#     # #cut head and set new head
#     # temp = self.head
#     # for i in range(count):
#     #     temp = temp.next
#     # temp.prev.next = None
#     # temp.prev = None
#     # self.head = temp

#     # #set new tail
#     # temp = self.tail
#     # for i in range(count):
#     #     temp = temp.next
#     #     self.tail = temp


# def deBottomUp(self, percent):
#     if self.size is 0:
#         return 'Empty Linked List'
#     if percent is 100 or 0:
#         return
#     count = int(self.size * (percent / 100))
#     invert_count = self.size - count
#     # invert_percent = 100 * (invert_count/self.size)
#     # self.bottomUp(int(invert_percent))
#     for j in range(invert_count):
#         temp = self.head
#         self.remove(self.head.data)
#         self.append(temp.data)


# def riffle(self, percent):
#     if self.size is 0:
#         return 'Empty Linked List'
#     if percent is 100 or 0:
#         return
#     count = int(self.size * (percent / 100))
    
#     temp = self.head
#     for i in range(count)
#         temp = temp.next
#     self.tail = temp.prev
#     self.tail.next = None
#     temp_head = temp
#     temp_head.prev = None
#     while temp.next is not None:
#         temp = temp.next
#     temp_tail = temp

#     #insert temp list to main list
#     temp_main = self.head
#     temper = temp_head
#     while temper is not None and temp_main is not None:
#         #store next item
#         main_next =