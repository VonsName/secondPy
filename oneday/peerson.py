# __author:  Administrator
# __date:  2018/8/10/010


class Person:
    def run(self, arg):
        print(self.name, self.age, arg)


# takes 2 positional arguments but 3 were given
obj = Person()
obj.name = '赵璐'
obj.age = '33'
obj.run(666)


class User:
    # 初始化方法(构造方法)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        print(self.name, self.age)

        print('%s-%s' % (self.name, self.age))


# user = User('王五', 23)
# user.foo()


# 继承
class Child(User):
    def foo(self):
        # super(Child, self).foo()
        print('a')


c = Child()
c.foo()
