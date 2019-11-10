def eat(n):     
    if n==1:         
        print('eat', n)     
    else:    
        eat(n-1)       
        print('eat', n)   # line 1         
                # line 2  
        
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

#print(fac(3))

def sum1ToN(n):
    if n < 1:
        return 0
    else:
        return n + sum1ToN(n-1)

#print(sum1ToN(5))

def print1ToN (n):
    if n == 1:
        print(1, end=' ')
    else:
        print1ToN(n-1)
        print(n, end=' ')

#print1ToN(5)


def fib(n):
    if n ==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
# def fib(n): 
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return  fib(n-2) + fib(n-1)

for i in range(1, 7):
    print(fib(i))

def binarySearch(lo, hi, x, l):
    mid = (lo+hi)//2
    if x == l[mid]:
        return mid
    elif lo == hi:
        return None
    else:
        if x < l[mid]:
            hi = mid-1
        elif x > l[mid]:
            lo = mid+1
        return binarySearch(lo, hi, x, l)



# def binarySearch(lo, hi, x, l):
#     mid = (lo + hi)//2

#     if l[mid] == x:
#         return mid
#     elif lo == hi:
#         return None
#     else:
#         if x > l[mid]:
#             lo = mid + 1
#         elif x < l[mid]:
#             hi = mid - 1
#         return binarySearch(lo, hi, x, l)



def move(n, start, dest):
    if n == 1:
        print(n, 'move from', start, 'to', dest)
    else:
        l = ['A', 'B', 'C']
        start = l.pop(l.index(start))
        dest = l.pop(l.index(dest))
        tmp = l.pop(0)
        move(n-1, start, tmp)
        print(n, 'move from', start, 'to', dest)
        move(n-1, tmp, dest)

    
# def move(n,start, dest):
#     if n == 1:
#         print(n, 'move from',start, 'to', dest)
#     else:
#         l = ['A', 'B', 'C']
#         start = l.pop(l.index(start))
#         dest = l.pop(l.index(dest))
#         temp = l[0]
#         move(n-1,start, temp)
#         print(n, 'move from', start, 'to', dest)
#         move(n-1, temp, dest)

def sum1(n, l):
    if n == 0:
        return 0
    else:
        return l[n-1] + sum1(n-1, l)

# def sum2():
#     return None



l = [1,2,3,4,5,6,7,8]
print(binarySearch(0, 7, 6, l))
move(3,'A','C')
print(sum1(3,l))

def printSack(sack, maxi):     
    global good     
    global name     
    for i in range (maxi+1):         
        print(name[sack[i]], good[sack[i]], end = ' ')         # print(name[sack[i]],good[sack[i]], end = ' ')     
    print() 
 
def pick(sack, i, mLeft, ig):     
    global N     
    global good     
    if ig < N:    # have something left to pick         
        price = good[ig]    # good-price         
        if mLeft < price:   # cannot afford that ig             
            pick(sack, i, mLeft, ig+1) # try to pick next good          
        else:               # can buy             
            mLeft -= price  # pay             
            sack[i] = ig    # pick that ig to the sack at i             
            if mLeft == 0:  # done                 
                printSack(sack, i)             
            else:           # still have moneyLeft                 
                pick(sack, i+1, mLeft, ig+1)             
            pick(sack, i, mLeft+price, ig+1)  # take the item off the sack for other solutions  
 
good = [20,10,5,5,3,2,20,10] 
name = ['soap', 'potato chips', 'loly pop', 'toffy', 'pencil', 'rubber', 'milk','cookie'] 
N = len(good)   # numbers of good 
 
sack = N*[-1]   # empty sack 
mLeft = 20      # money left 
i = 0           # sack index 
ig = 0          # good index 
pick(sack, i, mLeft,ig)  