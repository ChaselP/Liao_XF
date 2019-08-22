import itertools

def pi(N):
    odds=itertools.count(1,step=2)
    c=itertools.cycle((1,-1))
    #ns=itertools.takewhile(lambda x:x<10,odds)
    pi=0
    for i,n in zip(itertools.takewhile(lambda x:x<2*N,odds),c):
        pi+=4*n/i
    return pi

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')