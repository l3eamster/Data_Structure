
print('')
print('---------------------------- SORT ----------------------------')
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
print('bubble sort    >>',bubble(l))

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
print('shell sort     >>', shell(l, dIncrements))

def merge(l, left, right, rightEnd): 
    start = left 
    leftEnd = right-1 
    result = [] 
    while left <= leftEnd and right <= rightEnd: 
        if l[left] < l[right]: 
            result.append(l[left]) 
            left += 1 
        else: 
            result.append(l[right]) 
            right += 1 
    while left <= leftEnd: # copy remaining left half if any 
        result.append(l[left]) 
        left += 1 
    while right <= rightEnd: # copy remaining right half if any 
        result.append(l[right]) 
        right += 1

    for ele in result: # copy result back to list l 
        l[start] = ele 
        start += 1 
        if start > rightEnd: 
            break

def mergeSort(l, left, right): 
    center =  (left+right)//2 
    if left < right: 
        mergeSort(l, left, center) 
        mergeSort(l, center+1, right) 
        merge(l, left, center+1, right)
    return l
l = [5,3,6,1,2,7,8,4] 
print('merge sort     >>', mergeSort(l,0, len(l)-1))

# def quick(l, left, right): 
#     if left == right+1: #only 2 elements 
#         if l[left] > l[right]:
#             l[left], l[right] = l[right], l[left] #swap 
#         return 
#     if left < right: 
#         #partition 
#         pivot = l[left] #first element pivot 
#         i, j = left+1, right 
#         while i<j: 
#             while i<right and l[i]<=pivot: 
#                 i += 1 
#             while j>left and l[j]>=pivot: 
#                 j -= 1 
#             if i < j: 
#                 l[i], l[j] = l[j], l[i] #swap 
#         if left is not j: 
#             l[left], l[j] = l[j], pivot # swap pivot to index j 
#         quick(l, left, j-1) 
#         quick(l, j+1, right)
#     return l

# l = [5,1,4,9,6,3,8,2,7,0] 
# print('quick sort     >>', quick(l,0,len(l)-1))

def quick(l, left, right): 
    """last element pivot""" 
    if left == right+1: #only 2 elements 
        if l[left] > l[right]: 
            l[left], l[right] = l[right], l[left] #swap 
            return 
    if left < right: 
        #partition 
        pivot = l[right] #last element pivot 
        #print('-------------------------------------') 
        #print(' 0  1  2  3  4  5  6  7  8  9 ', ' (left=', left, ' right=', right, ' pivot=', pivot,')', sep='') 
        #print(l)        
        i, j = left, right-1 
        while i<j: 
            while i<right and l[i]<=pivot: 
                i += 1 
            while j>left and l[j]>=pivot: 
                j -= 1 
            if i<j: 
                l[i], l[j] = l[j], l[i] #swap 
                #print(l , '(swap', l[i], '-',l[j],')') 
        if right is not i: 
            l[right], l[i] = l[i], pivot # swap pivot to index i 
            #print(l, '(swap pivot',l[i] , '-',l[right],')') 
        quick(l, left, i-1) 
        quick(l, i+1, right) 
    return l
        
        
l = [5,1,4,9,0,3,8,2,7,6] 
print('quick sort     >>', quick(l,0,len(l)-1))


print('--------------------------------------------------------------')
print('')