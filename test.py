#linkedlist
from ClassNode import Node
from ClassList import List
    

l = List()
l.addHead('a')
l.append('B')
l.append('C')
l.addHead('0')

print(l)
l.removeHead()
print(l)
l.remove('C')
print(l)