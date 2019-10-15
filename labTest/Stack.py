class Stack :     
    def __init__(self,list = []) :   #สร้าง empty list 
        if list == []:
            self.items = []
        else:
            self.items = list

    def __str__(self) :         #พิมพ์ของที่อยู่ใน stack จากล่างขึ้นบน     
        return str(self.items)

    def __len__(self) :         #ส่งค่าจำนวนสมาชิกใน stack    
        return len(self.items)

    def isEmpty(self) :         #ส่งค่า True ถ้า Stack ว่าง, False ถ้าไม่ว่าง  
        return len(self.items) == 0

    def push(self,i) :          #นำของเก็บใน stack     
        self.items.append(i)

    def pop(self) :             #นำของออกจาก stack 
        if self.items != []:
            return self.items.pop()

    def peek(self) :
        return self.items[-1]

def checkPriority(current, next):
    priorCur = 0
    priorNext = 0
    if current in ['+','-']:
        priorCur = 1
    else:
        priorCur = 2
    if next in ['+','-']:
        priorNext = 1
    else:
        priorNext = 2
    return priorCur >= priorNext

def operation(infix):
    count = 0
    for i in infix:
        if i in ['+','-','*','/']:
            count += 1
    return str(count)

def operand(infix):
    count = 0
    for i in infix:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            count += 1
    return str(count)

def inToPost(infix):
    s = Stack()
    postFix = ''
    for i in infix:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            postFix += i
        elif i == '(':
            s.push(i)
        elif i == ')':
            while not s.isEmpty():
                if s.peek() == '(':
                    s.pop()
                    break
                postFix += s.pop()
        elif i in ['+','-','*','/']:
            while not s.isEmpty() and checkPriority(s.peek(), i):
                if s.peek() == '(':
                    break
                postFix += s.pop()
            s.push(i)
    while not s.isEmpty():
        postFix += s.pop()
    return postFix

def inToPre(infix):
    reversed_infix = ''
    tmp = infix[::-1]
    for i in tmp:
        if i == '(':
            reversed_infix += ')'
        elif i == ')':
            reversed_infix += '('
        else :
            reversed_infix += i
    prefix = inToPost(reversed_infix)
    prefix = prefix[::-1]
    return prefix

def postToIn(postfix):
    infix = ''
    s = Stack()
    for i in postfix:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            s.push(i)
        elif i in ['+','-','*','/']:
            tmp1 = s.pop()
            tmp2 = s.pop()
            tmp = '(' + tmp2 + i + tmp1 + ')'
            s.push(tmp)
    while not s.isEmpty():
        infix += s.pop()
    return infix


# s1 = 'a+b*c-d'
# s2 = 'a+b*c-(d/e+f)*g'
# s3 = '(a+b)*c/d'


# result1 = abc*+d-
# result2 = abc*+de/f+g*-
# result3 = ab+c*d/

# s1 = input('Enter infix expression    : ')
# print('Result postfix expression : '+ inToPost(s1)) 
# print('Number of operation       : '+ operation(s1)) 
# print('Number of operand   : '+ operand(s1))   
# s2 = input('Enter infix expression    : ')
# print('Result postfix expression : '+ inToPost(s2))
# print('Number of operation       : '+ operation(s2))
# print('Number of operand   : '+ operand(s2))
# s3 = input('Enter infix expression    : ')
# print('Result postfix expression : '+ inToPost(s3)) 
# print('Number of operation       : '+ operation(s3)) 
# print('Number of operand   : '+ operand(s3))

# s1 = input('Enter infix expression    : ')
# print('Result prefix expression : '+ inToPre(s1))

s1 = input('Enter postfix expression    : ')
print('Result infix expression : '+ postToIn(s1))