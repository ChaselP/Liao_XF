import functools
int2=functools.partial(int,base=2)

print(int2('1010101010',base=10))

kw = { 'base': 2 }
print(int('10010', **kw))
