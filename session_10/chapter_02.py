# 开发人员：DYL
# 开发时间：2022/10/8 10:07

# 类的继承、多重继承、组合

# 和java里面讲的也差不多
class A:
    x = 520

    @staticmethod
    def hello():
        print("你好，我是A")


class B(A):  # 小括号中就是继承的对象，也就是父类
    pass


b = B()
b.hello()


class B(A):
    x = 888

    def hello(self):  # 和父类中的方法一样，相当于重写了父类中的方法，和java中的面向对象的理念是一致的
        print("你好，我是B")


b = B()
print(b.x)
b.hello()

# isinstance()方法可以判断某个对象是否属于某一个类
print(isinstance(b, B))
print(isinstance(b, A))
# issubclass()用于检测一个类是否是另一个类的子类
print(issubclass(B, A))
print(issubclass(A, B))


# 多重继承，python里面一个类是可以继承多个类的
class B:
    x = 880
    y = 250

    @staticmethod
    def hello():
        print("你好，我是B")


class C(A, B):  # 访问顺序是从左到右的，也就是A中找不到了，才回去B中找
    pass


c = C()
print(c.x)
c.hello()
print(c.y)


# 组合
class Fish:
    def say(self):
        print("故不积跬步，无以至千里；不积小流，无以成江海。")


class Cat:
    @staticmethod
    def say():
        print("喵喵喵")


class Dog:
    @staticmethod
    def say():
        print("哦豁，我是一只小狗")


class Garden:
    t = Fish()
    c = Cat()
    d = Dog()

    def say(self):
        self.t.say()
        self.c.say()
        self.d.say()


g = Garden()
g.say()
