# 开发人员：DYL
# 开发时间：2022/10/8 19:29
import chapter_02


# 绑定
class Garden:
    t = chapter_02.Fish()
    c = chapter_02.Cat()
    d = chapter_02.Dog()

    def say(self):
        self.t.say()  # 就是这么绑定的，self就是对象本身，将实例对象和对象进行绑定
        self.c.say()
        self.d.say()


# 构造函数，__init__()，只需要在定义类的时候定义这个方法就行，和java里面的面向对象也差不多
class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def mul(self):
        return self.x * self.y


c = C(2, 3)
print(c.add())
print(c.mul())
print(c.__dict__)
d = C(4, 5)
print(d.__dict__)
print(d.add())
print(d.mul())


# 方法的重写
class D(C):
    def __init__(self, x, y, z):
        C.__init__(self, x, y)
        self.z = z

    def add(self):
        return C.add(self) + self.z

    def mul(self):
        return C.mul(self) * self.z


d = D(2, 3, 4)
print(d.add())
print(d.mul())


# 钻石继承
class A:
    def __init__(self):
        print("我是A")


class B1(A):
    def __init__(self):
        A.__init__(self)
        print("我是B1")


class B2(A):
    def __init__(self):
        A.__init__(self)
        print("我是B2")


class C(B1, B2):
    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)
        print("我是C")


c = C()
print("\n")


# 发现A出现了两次，因为多重继承，的两个都继承自A，钻石继承可以用supper()方法来避免
class B1(A):
    def __init__(self):
        super().__init__()
        print("我是B1")


class B2(A):
    def __init__(self):
        super().__init__()
        print("我是B2")


class C(B1, B2):
    def __init__(self):
        super().__init__()
        print("我是C")


c1 = C()  # 现在就不会重复了，只要使用了super方法去查找父类中的方法，它就会按照MRO(方法解析顺序)顺序去搜索相关方法
# ，并且避免重复的问题
print(C.mro())
print(B1.mro())
print(C.__mro__)
print(B2.__mro__)
