def quicksort(list, mode):
    global count
    if mode == 'low':
        pivotIndex = 0
    elif mode == 'high':
        pivotIndex = len(list)-1
    elif mode == 'mid':
        pivotIndex = (len(list)-1)//2

    less =[]
    equal = []
    greater = []
    if len(list) - 1 > 0:
        pivot = list[pivotIndex]
        for x in list:
            if x < pivot:
                count += 1
                less.append(x)
            elif x == pivot:
                count += 1
                equal.append(x)
            elif x > pivot:
                count += 1
                greater.append(x)
        return quicksort(less,mode)+equal+quicksort(greater,mode)
    else:
        return list


# l = [5]
# l = [193,362,534,402,0,0,0,0,0]
# l = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
# l = [10,99,85,12,36,47,97,35,62,44,33,11,63,13,18,29]

l =[1,5,5,5,5,5,1]


print('----------------------------------')


print('List :                        ==>',l)
count=0
FIRST = quicksort(l,'low')
print('quick low sort : count  =>',count,'==>',FIRST)


count=0
END = quicksort(l,'high')
print('quick high sort : count =>',count,'==>',END)


count=0
MID = quicksort(l,'mid')
print('quick mid sort : count  =>',count,'==>',MID)

print('----------------------------------')