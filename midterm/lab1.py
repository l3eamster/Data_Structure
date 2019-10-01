def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum*i
    return sum

def multiples_of_3_and_5(n):
    sum = 0
    for i in range(3,n):
        if i%3 == 0 or i%5 == 0:
            sum = sum+i
    return sum

def integer_right_triangles(p):
    res = []
    for a in range(1,p):
        for b in range(1,p):
            for c in range(1,p):
                if(a<=b<c and c*c == a*a+b*b and a+b+c==p):
                    res.append((a,b,c))
    return res    

def aLine(s):     
    res = '' #result     
    for i in range(1, len(s)):         
        res = s[i] + res     
    res = res + s     
    res = '*'.join(res)     
    res = res      
    return res

def gen_pattern(chars):
    n = 3*len(s)-1     
    mid = aLine(s) + '\n'     
    for i in range(1,len(s)):         
        r = aLine(s[i:len(s)])         
        r = r.center(n,'*')         
        r = r + '\n'         
        mid = r + mid + r     
    return mid

#print(multiples_of_3_and_5(10))
#print(integer_right_triangles(60))
s = 'wxyz' 
print(gen_pattern('wxyz')) 