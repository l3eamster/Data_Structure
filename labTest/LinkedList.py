class LinkedList:

  class Node:
    def __init__( self, data, next=None ):
    self.data = data
    self.next = next
    
def __init__( self ):
    self.head = self.tail = self.Node(None)

  def __str__( self ):
    l = []
    p = self.head.next
    while p is not None:
      l.append(p.data)
      p = p.next
    return str(l)
  
  def __len__( self ):
    size = 0
    p = self.head.next
    while p is not None:
      size += 1
      p = p.next
    return size
  
  def isEmpty( self ):
    return len(self) == 0

  def append( self, data ):
    new_node = self.Node(data)
    self.tail.next = new_node
    self.tail = new_node
  
  def getNode( self, data ):
    p = self.head.next
    while p is not None:
      if p.data == data:
        return p
      p = p.next

  def before( self, data ):
    p = self.head
    while p.next is not None:
      if p.next.data == data:
        return p
      p = p.next

  def remove( self, data ):
    if self.getNode(data) is not None:
      removed_node = self.getNode(data)
      self.before(data).next = removed_node.next
      return removed_node
  
  # order linkedlist
  def add( self, data ):
    if self.isEmpty():
      self.append(data)
    else:
      p = self.head.next
      while p is not None:
        if data < p.data:
          new_node = self.Node(data)
          new_node.next = p
          self.before(p.data).next = new_node
          break
        elif data >= p.data:
          if p.next is None:
            self.append(data)
            break
          elif data <= p.next.data:
            new_node = self.Node(data)
            new_node.next = p.next
            p.next = new_node
            break
        p = p.next

# class LinkedList :     
#     class Node :            
#         def __init__(self,data = None,next = None) :  #สร้างโหนดเพื่อเก็บข้อมูล  
#             self.data = data
#             self.next = next
#             if next is None:
#                 self.prev = None
#             else:
#                 self.next.prev = self

#         def setNext(self, next):
#             self.next = next
#             self.next.prev = self
        
#     def __init__(self):            #สร้าง linked list ว่าง     
#         self.head = self.tail = self.Node()
#         self.size = 0

#     def __str__(self) :           #แสดงข้อมูลจากหัวไปหาง
#         s = ''
#         tmp = self.head.next
#         while tmp.next is not None:
#             s = s + str(tmp.data) + ' '
#             tmp = tmp.next
#         s = s + str(tmp.data)
#         return s
        
#     def __len__(self) :  #ส่งค่าจำนวนสมาชิก   
#         return self.size  
        
#     def isEmpty(self) :  #ส่งค่า True ถ้า linked list ว่าง, False ถ้าไม่ว่าง    
#         return self.size == 0 
    
#     def append(self,data) :  #เพิ่มข้อมูลต่อท้าย
#         newNode = self.Node(data)
#         self.tail.next = newNode
#         newNode.prev = self.tail
#         self.tail = newNode  
#         self.size += 1 

#     def isIn(self, data):
#         check = 0
#         tmp = self.head
#         while tmp.next is not None:
#             if tmp.data is data:
#                 check+=1
#             tmp = tmp.next
#         if tmp.data is data:
#             check+=1
#         return check != 0
    
#     def remove(self,data) :  #ลบข้อมูลตัวนั้นออก
#         if self.isEmpty():
#             return
#         elif self.isIn(data):
#             tmp = self.head.next
#             while tmp.data is not data:
#                 tmp = tmp.next
#             tmp.prev.setNext(tmp.next)
#             self.size-=1
#             return tmp.data
#         else:
#             return
                 
#     def add(self,data) :  #ตามข้อกำหนดข้อ 2.1
#         if self.isEmpty():
#             self.append(data)
#         else:
#             tmp = self.head.next
#             newNode = self.Node(data)
#             while tmp is not None:
#                 if data <= tmp.data:
#                     p = tmp.prev
#                     newNode.next = tmp
#                     tmp.prev.next = newNode
#                     tmp.prev = newNode
#                     newNode.prev = p
#                     return
#                 tmp = tmp.next
#             self.append(data)   


def mean(ll):
    s = 0
    count = 0
    tmp = ll.head.next
    while tmp is not None:
        s = s + tmp.data
        count += 1
        tmp = tmp.next
    return float(s/count)

def mode(ll):
    s = []
    tmp = ll.head.next
    while tmp is not None:
        s.append(tmp.data)
        tmp = tmp.next
    maxcount = max(map(s.count, s)) 
    result = []
    for i in s:
        if s.count(i) == maxcount:
            result.append(i)
    result = list(dict.fromkeys(result))
    return result
            

def median(ll):
    s = []
    tmp = ll.head.next
    while tmp is not None:
        s.append(tmp.data)
        tmp = tmp.next
    median = float((s[5] + s[6]) /2)
    return median

# s1 = 7 9 3 2 1 2 3 4 8 9 3 15
# s2 = 7  6  74  44  6  37  55  35  3  31  3  10
ll = LinkedList()
s1 = list(input('Enter 12 number :  ').split())
for i in s1:
    ll.add(int(i))
print('LinkedList data : ', ll) 
print('Mean = ', mean(ll)) 
print('Mode = ', mode(ll))
print('Median = ', median(ll)) 

ll2 = LinkedList()
s2 = list(input('Enter 12 number :  ').split())
for j in s2:
    ll2.add(int(j))
print('LinkedList data : ', ll2) 
print('Mean = {0:.2f}'.format(mean(ll2))) 
print('Mode = ', mode(ll2))
print('Median = ', median(ll2))

# ll = LinkedList()
# ll.add(5)
# print(ll)
# ll.add(9)
# print(ll)
# ll.add(7)
# print(ll)
# ll.add(3)
# print(ll)
# ll.add(11)
# print(ll)
# ll.add(2)
# print(ll)
# ll.add(3)
# print(ll)
# ll.add(4)
# print(ll)
# ll.add(8)
# print(ll)
# ll.add(9)
# print(ll)
# ll.add(3)
# print(ll)
# ll.add(15)
# print(ll)