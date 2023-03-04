# 开发人员：DYL
# 开发时间：2022/10/4 10:01
import functools


# functools——高阶函数

# reduce(param1,param2)函数的作用就是将可迭代参数对象依次传入到第一个参数指定的函数中，最终返回累积的结果
def add(x, y):
    return x + y


print(functools.reduce(add, [1, 2, 3, 4, 5]))  # 相当于下面这种做法
print(add(add(add(add(1, 2), 3), 4), 5))

print(functools.reduce(lambda x, y: x * y, range(1, 11)))

# 偏函数:二次包装已有的函数
square = functools.partial(pow, exp=2)
print(square(2))

