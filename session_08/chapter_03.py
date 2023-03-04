# 开发人员：DYL
# 开发时间：2022/9/29 15:43

# 在函数外部定义的变量作用域是全局的
i = 2


def func():
    print(i)


func()


# 如果函数内部出现和外部变量一样的变量那么在函数内部,内部的变量就会覆盖外部的变量
def func():
    i = 4
    print(i)


func()


# 在函数内部如果想修改全局变量的值可以用global来改
def func():
    global i
    i = 999
    print(i)


func()
print(i)


# 嵌套函数，内部嵌套的函数是不能直接被调用的,只能在定义的时候就直接调用
def A():
    print(111)

    def B():
        print(222)

    B()


A()


# 如何在内部函数修改外部函数的变量，nonlocal语句
def A():
    k = 222111

    def B():
        nonlocal k
        k = 890908
        print(k)
    B()
    print(k)


A()
# 外层函数中的变量并不会在调用结束后就消失不见，而是会以某种方式保存下来
