#linkedlist
from ClassNode import Node
from ClassList import List

# mode = 0
# l = list()
    
# while True:
#     print('___scramble simulation___\nMENU')
#     print('[1] append\n[2]addHead\n[3]remove\n[4]remove tail\n[5]remove head\n[6]bottomUp')
#     print('[7]debottomUp\n[8]riffle')
#     mode = int(input())
#     if mode is 1:
#         i = input()
#         l.append(i)

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
