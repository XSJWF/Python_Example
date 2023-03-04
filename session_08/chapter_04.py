# 开发人员：DYL
# 开发时间：2022/9/29 16:01

# 闭包，简单来说就是一个函数定义中引用了函数外定义的变量，并且该函数可以在其定义环境外被执行。这样的一个函数我们称之为闭包。
# 利用嵌套函数的外层作用域具有记忆能力的特性，让数据保存在外层函数的参数或者变量中；将内层函数作为返回值返回，这样就可以从外部直接调用内层的函数。
def power(esp):
    def esp_op(base):
        return base ** esp

    return esp_op


suo = power(2)
cu = power(3)
print(suo(2), suo(6))
print(cu(2), cu(5))


def outer():
    x = 0
    y = 0

    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print("现在，x = {}，y = {}".format(x, y))

    return inner


move = outer()
move(1, 2)
move(-2, 2)

# python装饰器就是在不改动原函数代码的基础上，给原函数增加新的功能
import time


def time_master(func5):
    def call_func():
        print("程序开始运行...")
        start = time.time()
        func5()
        stop = time.time()
        print("程序结束运行...")
        print("一共耗费了{:.2f}s".format(stop - start))

    return call_func


@time_master  # 相当于应用装饰器，这种简写的方式相当于语法糖，更为方便，代替了time_master(func)
def func():
    time.sleep(2)
    print("我爱NLP")


func()


# 同时使用多个装饰器
def add(func5):
    def inner():
        x = func5()
        return x + 1

    return inner


def cube(func5):
    def inner():
        x = func5()
        return x * x * x

    return inner


def square(func5):
    def inner():
        x = func5()
        return x * x

    return inner


@add
@cube
@square
def test():
    return 2


print(test())

# 如何给装饰器传递参数


def logger(msg):
    def time_master1(func3):
        def call_func():
            start = time.time()
            func3()
            stop = time.time()
            print(f"[{msg}]一共耗费了{(stop - start):.4f}")

        return call_func

    return time_master1


@logger(msg="王八蛋")
def func1():
    time.sleep(1)
    print("正在调用func1")


@logger(msg="傻子")
def func2():
    time.sleep(1)
    print("正在调用fun2")


func1()
func2()
