# 开发人员：DYL
# 开发时间：2022/9/29 20:57

# lambda表达式 格式：lambda arg1,arg2,...,argN : expression

func = lambda x: x * x
print(func(2))
print(func)

func = [lambda x: x * x, 2, 3]
print(func[0](func[1]))

map1 = map(lambda x: ord(x) + 10, "sjk")
print(list(map1))
print(list(filter(lambda x: x % 2, range(10))))


# 生成器(generator),每调用一次提供一个数据，并且会记住当前的状态，支持next()函数
def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1


print(counter())
for i in counter():
    print(i)

c = counter()
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


# print(c[2])是错误的，生成器不支持索引下标

# 用生成器实现斐波那契数列
def fib():
    back1, back2 = 0, 1
    while True:
        yield back1
        back1, back2 = back2, back1 + back2


f = fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

# 生成器表达式
print(i ** 2 for i in range(10))
t = (i ** 2 for i in range(10))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
for i in t:
    print(i)



