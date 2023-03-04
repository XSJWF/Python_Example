# 开发人员：DYL
# 开发时间：2022/4/25 19:11

# 元组：Python的内置数据结构之一，是一个不可变序列
# 不可变序列：字符串，元组（没有增、删、改操作）
# 可变序列：列表、字典（可以执行增、删、改操作，对象地址不发生变化）

# 可变序列：
list1 = [1, 2, 3]
print(id(list1))
list1.append(4)
print(id(list1))  # 地址不改变

# 不可变序列：
s = 'Hello'
print(id(s))
s += 'World'
print(id(s))  # 地址改变了

# 元组的创建方式
# 第一种
t = (1, 2, 3, 4, 5)
print(t)
print(type(t))

t1 = '网吧', '傻逼', 3, 4, 5  # 省略小括号的写法
print(t1)
print(type(t1))

t2 = ('month')
print(t2)
print(type(t2))  # 此时输出的类型为str类型，即便是元组类只有一个元素也不能省略逗号此处因写成('month',)

# 第二种
T = tuple((1, 2, 3, 4, 5, 6))
print(T)
print(type(T))

# 空元组的创建方式：

t3 = ()
t4 = tuple()
print(type(t3))
print(type(t4))
