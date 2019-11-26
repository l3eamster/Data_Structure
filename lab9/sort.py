
print('')
print('---------------------------- SORT ----------------------------')

class LinkedList:

  class Node:
    def __init__( self, data, next=None ):
      self.data = data
      self.next = next
    
    def __str__( self ):
      return str(self.data)

  def __init__( self ):
    self.head = self.Node(None)
  
  def __str__( self ):
    linked_data = ''
    p = self.head.next
    while p is not None:
      linked_data += str(p.data)
      linked_data += ' -> ' if p.next is not None else ''
      p = p.next
    return linked_data
  
  def __len__( self ):
    p = self.head.next
    count = 0
    while p is not None:
      count += 1
      p = p.next
    return count
  
  def index( self, i ):
    p = self.head.next
    for _ in range(i):
      if p.next is not None:
        p = p.next
      else:
        return None
    return p
  
  def append( self, data ):
    p = self.head
    while p.next is not None:
      p = p.next
    new_node = self.Node(data)
    p.next = new_node

# def bubble(l):
#     for last in range(l.__len__()-1, -1, -1):
#         swap = False
#         for i in range(last):
#             if l.index(i).data > l.index(i+1).data:
#                 l.index(i).data, l.index(i+1).data = l.index(i+1).data, l.index(i).data
#                 swap = True
#         if not swap:
#             break
#     return l

# def selection(l):
#     for last in range(l.__len__()-1, -1, -1):
#         biggest = l.index(0).data
#         biggest_i = 0
#         for i in range(last+1):
#             if l.index(i).data > biggest:
#                 biggest = l.index(i).data
#                 biggest_i = i
#         l.index(last).data, l.index(biggest_i).data = l.index(biggest_i).data, l.index(last).data 
#     return l

# def insertion(l):
#     for i in range(1, l.__len__()):
#         ins = l.index(i).data
#         for j in range(i, -1, -1):
#             if ins < l.index(j-1).data and j > 0:
#                 l.index(j).data = l.index(j-1).data
#             else:
#                 l.index(j).data = ins
#                 break
#     return l

# def shell(l, dIncrements): 
#     for inc in dIncrements: #for each deminishing increment     
#         for i in range(inc,l.__len__()): #insertion sort 
#             iEle = l.index(i).data   #inserting element 
#             for j in range(i, -1, -inc): 
#                 if iEle < l.index(j-inc).data and j >= inc: 
#                     l.index(j).data = l.index(j-inc).data
#                 else: 
#                     l.index(j).data = iEle 
#                     break 
#     return l

# def merge(l, left, right, rightEnd): 
#     start = left 
#     leftEnd = right-1 
#     result = LinkedList() 
#     while left <= leftEnd and right <= rightEnd: 
#         if l.index(left).data < l.index(right).data: 
#             result.append(l.index(left).data) 
#             left += 1 
#         else: 
#             result.append(l.index(right).data) 
#             right += 1 
#     while left <= leftEnd: # copy remaining left half if any 
#         result.append(l.index(left).data) 
#         left += 1 
#     while right <= rightEnd: # copy remaining right half if any 
#         result.append(l.index(right).data) 
#         right += 1

#     for ele in range(result.__len__()): # copy result back to list l 
#         l.index(start).data = result.index(ele).data
#         start += 1 
#         if start > rightEnd: 
#             break

# def mergeSort(l, left, right): 
#     center =  (left+right)//2 
#     if left < right: 
#         mergeSort(l, left, center) 
#         mergeSort(l, center+1, right) 
#         merge(l, left, center+1, right)
#     return l

def quickHigh( l, low=None, high=None ): 
  low = 0 if low is None else low
  high = l.__len__()-1 if high is None else high

  if low < high: 
    pi = partitionHigh(l,low,high) 

    quickHigh(l, low, pi-1) 
    quickHigh(l, pi+1, high) 

def partitionHigh( l, low, high ): 
  i = low-1                  
  pivot = l.index(high).data            

  for j in range(low, high):  
    if l.index(j).data <= pivot: 
      i += 1          
      l.index(i).data, l.index(j).data = l.index(j).data, l.index(i).data 
      #print(l)

  l.index(i+1).data, l.index(high).data = l.index(high).data, l.index(i+1).data 
  return i+1

def quickLow( l, low=None, high=None ): 
  low = 0 if low is None else low
  high = l.__len__()-1 if high is None else high

  if low < high: 
    pi = partitionLow(l,low,high) 

    quickLow(l, low, pi-1) 
    quickLow(l, pi+1, high)     

def partitionLow( l, low, high ): 
  i = low+1                  
  pivot = l.index(low).data            

  for j in range(low+1, high+1):  
    if l.index(j).data <= pivot: 
      if j != i:     
        l.index(i).data, l.index(j).data = l.index(j).data, l.index(i).data 
      i += 1 

  l.index(low).data = l.index(i-1).data 
  l.index(i-1).data = pivot

  return i-1

def quickMid( l, left, right): 
  if left >= right:
    return
  leftI = left
  rightI = right
  pivot = (right + left)//2
  while leftI <= rightI:
    while l.index(leftI).data < l.index(pivot).data:
      leftI+=1
    while l.index(rightI).data > l.index(pivot).data:
      rightI-=1
    if leftI <= rightI:
      l.index(leftI).data, l.index(rightI).data = l.index(rightI).data, l.index(leftI).data
      leftI+=1
      rightI-=1
  print(l)
  if left <= rightI:
    quickMid(l, left, rightI)
  if leftI <= right:
    quickMid(l, leftI, right)
        
#=======================================================


        
# lb = [10,11,1,0,13,2,6,4,12,5,8,7,9,3] 
# llb = LinkedList()

# for i in lb:
#   llb.append(i)

# print('LinkedList     >>', llb)
# print('bubble sort    >>',bubble(llb)) 
# print()

# ls = [6, 9, 8, 5, 4] 
# lls = LinkedList()

# for i in ls:
#   lls.append(i)

# print('LinkedList     >>', lls)
# print('selection sort >>',selection(lls))
# print()

# li = [8, 6, 7, 5, 9]
# lli = LinkedList()

# for i in li:
#   lli.append(i)

# print('LinkedList     >>', lli)
# print('insertion sort >>', insertion(lli))
# print()

# lh = [10,11,1,13,2,6,4,12,5,8,7,9,3] 
# dIncrements = [5,3,1]
# llh = LinkedList()

# for i in lh:
#   llh.append(i)

# print('LinkedList     >>', llh)
# print('shell sort     >>', shell(llh, dIncrements))
# print()

# lm = [5,3,6,1,2,7,8,4] 
# llm = LinkedList()

# for i in lm:
#   llm.append(i)

# print('LinkedList     >>', llm)
# print('merge sort     >>', mergeSort(llm,0, llm.__len__()-1))
# print()
        
# lqh = [5,1,4,9,0,3,8,2,7,6] 
# llqh = LinkedList()

# for i in lqh:
#   llqh.append(i)

# print('LinkedList     >>', llqh)
# quickHigh(llqh)
# print('quick sort     >>', llqh)
# print()

# lql = [5,1,4,9,0,3,8,2,7,6] 
# llql = LinkedList()

# for i in lql:
#   llql.append(i)

# print('LinkedList     >>', llql)
# quickLow(llql)
# print('quick sort     >>', llql)
# print()

lqm = [5,1,4,9,0,3,8,2,7,6] 
llqm = LinkedList()

for i in lqm:
  llqm.append(i)

print('LinkedList     >>', llqm)
#countM3 = quickM3(llqm,0,llqm.__len__()-1,0)
#print('After QuickM3 : ','count: ',countM3)
# count = 0
quickMid(llqm, 0, llqm.__len__()-1)
print('quick mid sort >>', llqm)
print()

#print(llqm.index(7).data>llqm.index(2).data)

print('--------------------------------------------------------------')
print('')
