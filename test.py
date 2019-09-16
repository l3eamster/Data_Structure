#linkedlist
from ClassNode import Node
from ClassList import List

mode = 0
l = list()
    
while True:
    print('___scramble simulation___\nMENU')
    print('[1] append\n[2]addHead\n[3]remove\n[4]remove tail\n[5]remove head\n[6]bottomUp')
    print('[7]debottomUp\n[8]riffle')
    mode = int(input())
    if mode is 1:
        i = input()
        l.append(i)



# a = Node('A')
# l = List(a)
# l.append('B')
# l.append('C')
# l.addHead('0')

# print(l)
# l.removeHead()
# print(l)
# print(l.isIn('B'))
# print(l)