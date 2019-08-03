from functools import reduce

'''
def f(x):
    return x*x

r=map(f,[1,2,3,4,5,6,7])
print(list(r))

print(list(map(str,[1,2,3,4,5,6,7])))

for i in map(str,[1,2,3]):
    print(i)

def add(x,y):
    return x+y
dd=lambda x,y:x+y

print(reduce(dd,[1,2,3,4,5]))

'''

def normalize(name):
    return name.title()
    #return name.capitalize()

L1=['adam','LISA','barT']

L2=list(map(normalize,L1))
print(L2)

def prod(L):
    return reduce(lambda x,y:x*y,L)

print('3*5*7*9=',prod([3,5,7,9]))

def str2float(s):
    m,n=s.split('.')
    tra=lambda x:int(x)
    return reduce(lambda x,y:x*10+y,map(tra,m))+reduce(lambda x,y:x*0.1+y,map(tra,n[::-1]))*0.1


print('str2float(\'123.456\')=',str2float('123.456'))
if abs(str2float('123.456')-123.456)<0.00001:
    print("Success")
else:
    print("False")

def str2float1(s):
    m,n=s.split('.')
    tra=lambda x:int(x)
    def tt(n):
        return lambda x,y:x*n+y
    return reduce(tt(10),map(tra,m))+reduce(tt(0.1),map(tra,n[::-1]))*0.1

print(str2float1('123.456'))