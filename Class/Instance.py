class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count +=1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

#@property

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value

    @property
    def resolution(self):
        return self._height*self._width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


class A(object):
    def __init__(self):
        self.name="A"

class B(object):
    def __init__(self):
        self.name="B"

class C(B,A,object):
    pass

c=C()

print(c.name)

