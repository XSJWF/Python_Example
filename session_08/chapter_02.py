# 开发人员：DYL
# 开发时间：2022/9/29 14:56

# 关键字参数，在调用函数的时候直接写出关键字的对应赋值;

def func(i, j, k):
    print("i:", i, "j:", j, "k:", k)


func(j=0, i=-2, k=9)

# 位置参数就是每个位置一一对应
func(1, 2, 3)

# 位置参数和关键字参数混合使用,位置参数必须写在默认参数之前,而且参数传递不能重复（即不能给同一个参数传递两个值）
func(2, 3, k=1)


# 默认参数，即函数在定义的时候就指定好参数的值，那么当调用该函数没有传递该参数的值的时候就会使用默认的值，当然如果传了值的就使用传的值
# 注意如果要使用默认参数的话，那么久得把默认参数放到最后面
def duck(i, k=2):
    print("i:", i, "k:", k)


duck(3)
duck(i=4)
duck(i=1, k=1)
duck(9, 8)


# 搜集参数
def dunk(*args):
    print("有{}个参数".format(len(args)))
    print("第2个参数是：{}".format(args[1]))
    print(args)
    print(type(args))


dunk(1, "傻逼", "瓜娃子")


# 如果在使用了搜集参数后还要使用其他的参数，就必须用关键字指定，不然python就会把所有的参数纳入到收集参数中
def dunk(*args, o, lx):
    print(args, o, lx)


dunk(1, 2, 3, o=4, lx=5)


# 搜集参数除了能打包为元组还能打包为字典
def func(**kwargs):
    print(kwargs)


func(a=1, b=2, c=3)


# 混合参数模式
def func(a, *b, **c):
    print(a, b, c)


func(1, 2, 3, 4, x=5, y=6)
# 解包参数
args = (1, 2, 3, 4)


def func(a, b, c, d):
    print(a, b, c, d)


func(*args)
kwargs = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
func(**kwargs)
