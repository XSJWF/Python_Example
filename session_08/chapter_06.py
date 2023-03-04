# 开发人员：DYL
# 开发时间：2022/10/3 18:04

# 递归和迭代的对比


def dieDai(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


print(dieDai(50))


def diGui(n):
    if n == 1:
        return 1
    else:
        return n * diGui(n - 1)


print(diGui(50))


# 斐波那契数列
def fib(n):
    a, b = 1, 1
    while n > 2:
        a, b = b, a + b
        n -= 1
    return b


print(fib(12))


def fiber(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fiber(n - 1) + fiber(n - 2)


print(fiber(12))


# 递归的应用，汉诺塔算法，详细可看我的博客
def Hanoi(n, current, transit, target):
    if n == 1:
        print(current, "-->", target)
    else:
        Hanoi(n - 1, current, target, transit)
        print(current, "-->", target)
        Hanoi(n - 1, transit, current, target)


num = int(input("输入汉诺塔的层数："))
Hanoi(num, 'A', 'B', 'C')
