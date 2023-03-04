# 开发人员：DYL
# 开发时间：2022/3/26 22:08

# 列表类似于数组，但是列表可以存储不同类型的变量，动态分配和回收内存

# 第一种创建方式
list1 = ["Hello", "World", 98]
print(id(list1))
print(id(list1[0]))
print(id(list1[1]))
print(id(list1[2]))  # 内存并不连续
print(type(list1))
print(list1)

# 第二种创建方式利用内置函数list()
list2 = list(["Hello", "王八蛋", "二百五"])
print(list2[-2])  # 负数下标就是倒着取列表的元素，负几就是倒数第几个元素，和正数下标不同的是，负数下标从-1开始
print(list2)

# 正向索引0-(N-1),逆向索引 (-N)-(-1)
