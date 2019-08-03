import functools,time

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('2015-3-25')
#
# now()
#
# print(now.__name__)


def metric(fn):
    @functools.wraps(fn)
    def duration(*args,**kw):
        start=time.time()
        result=fn(*args,**kw)
        end=time.time()
        print('%s executed in %s ms' % (fn.__name__, end-start))
        return result
    return duration

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')