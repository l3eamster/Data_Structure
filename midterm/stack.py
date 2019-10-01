class Stack:
    def __init__(self, list=[]):
        if list is None:
            self.items = []
        else: 
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        if self.items != []:
            return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items is None

    def size(self):
        return len(self.items)

def depart(self, car):
    if not self.items is []:
        found = False
        temp = Stack()
        s = ''
        while not found and not self.items is []:
            carFound = self.items.pop()
            s += "pop " + str(carFound) + ', '
            if(carFound == car):
                found = True
                break
            if(not found):
                temp.push(carFound)
        while not temp.isEmpty():
            carTemp = temp.pop()
            self.items.push(carTemp)
            s += "push " + str(carTemp) + ', '
        if(not found):
            print("car", car, "cannot depart: No car",car)
        else :
            print(s[:len(s)-2])
        print("space left", 4 - self.items.size())
    else:
        print("car", car, "cannot depart:soi empty")

def arrive(self, newCar):
    if(not (self.items.size() == 4)):
        self.items.push(newCar)
        print("car", newCar, "arrive  space left", 4- self.items.size())
    else:
        print("car", newCar, " cannot arrive: SOI FULL")

def isFull(self):
    return len(self.items.size()) == 4

def soi(self):
    return self.items.items

# def match(open, c):
#     if(open == '(' and c == ')'):
#         return True
#     if(open == '{' and c == '}'):
#         return True
#     if(open == '[' and c == ']'):
#         return True
#     return False

# str1 = '( a+b-c *[d+e]/{f*(g+h) }'
# str2 = '[ ( a+b-c }*[d+e]/{f*(g+h) }'
# str3 = '( 3 + 2 ) / { 4**5 }'
# s = Stack()
# error = False
# for j in range(0,len(str3)):
#     i = str3[j]
#     print(i)
#     if i is '[' or '{' or '(':
#         s.push(i)
#     elif i is ']' or '}' or ')':
#         if s.isEmpty:
#             error = True
#         else:
#             open = s.pop
#             if not match(open,i):
#                 error = True
# if error:
#     print('MISMATCH')
# else:
#     if s.isEmpty:
#         print('MISMATCH')
#     else:
#         print('MATCH')


#CAR PARKING


    

park = Stack()
print(park.isEmpty())
park.depart(6)

park.arrive(2)
park.arrive(6)
park.arrive(3)
park.arrive(5)
park.arrive(1)
print(park.soi())

park.depart(7)

park.depart(3)
print(park.soi())