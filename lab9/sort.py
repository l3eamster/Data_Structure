from math import log2 
from math import floor 

def bubble(l):
    for last in range(len(l)-1, -1, -1):
        swap = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swap = True
        if not swap:
            break
    return l

l = [5,6,2,3,0,1,4] 
print('bubble sort >>',bubble(l))

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

l = [6, 9, 8, 5, 4] 
print('selection sort >>',selection(l))

def insertion(l):
    for i in range(1, len(l)):
        ins = l[i]
        for j in range(i, -1, -1):
            if ins < l[j-1] and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = ins
                break
    return l

l = [8, 6, 7, 5, 9]
print('insertion sort >>', insertion(l))

def shell(l, dIncrements): 
    for inc in dIncrements: #for each deminishing increment     
        for i in range(inc,len(l)): #insertion sort 
            iEle = l[i]   #inserting element 
            for j in range(i, -1, -inc): 
                if iEle<l[j-inc] and j >= inc: 
                    l[j] = l[j-inc] 
                else: 
                    l[j] = iEle 
                    break 
    return l

l = [10,11,1,13,2,6,4,12,5,8,7,9,3] 
dIncrements = [5,3,1] 
print(shell(l, dIncrements))



# def print90(h, i, max_i): 
#     if i < max_i: 
#         indent = floor(log2(i+1)) 
#         print90(h, (i*2)+2, max_i) 
#         print('   ' * indent, h[i]) 
#         print90(h, (i*2)+1, max_i)
