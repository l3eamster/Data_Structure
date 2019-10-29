from math import log2 
from math import floor 

def bubble(l):
    for last in range(len(l)-1, -1, -1):
        swap = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                l[i] = temp
                swap = True
        if not swap:
            break
    return l

def selection(l):
    for last in range(len(l)-1, -1, -1):
        biggest = l[0]
        biggest_i = 0
        for i in range(last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        l[last], l[biggest_i] = l[biggest_i], l[last] 
    return l

def insertion(l):

l = [8, 3, 9, 4, 5]
print(selection(l))

# def print90(h, i, max_i): 
#     if i < max_i: 
#         indent = floor(log2(i+1)) 
#         print90(h, (i*2)+2, max_i) 
#         print('   ' * indent, h[i]) 
#         print90(h, (i*2)+1, max_i)
