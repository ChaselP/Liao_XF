class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender in ('male','female'):
            self.__gender=gender
        else:
            print('Wrong Gender')


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


class Animal(object):
    def __init__(self):
        pass
    a=5

class Dog(Animal):
    pass

b=Animal()
print(b.a)
c=Dog()
print(c.a)


print(hasattr(c,'a'))
print(isinstance(c,object))