# 开发人员：DYL
# 开发时间：2022/3/27 12:43

# 列表的切片操作，一次获取多个元素
# 语法：列表名[start:stop:step]

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

print(list1[1:6:1])

print("原列表", id(list1))

list2 = list1[1:6:1]

print("切的片段", id(list2))  # 新的对象

print(list1[1:6])  # 不写步长，默认步长为1

print(list1[1:6:])

print(list1[1:6:2])

print(list1[:6:2])  # 不写起始位置，默认起始位置为0

print(list1[1::2])  # 不写结束位置，默认结束位置为（N-1）即列表末端

print(list1[::-1])  # 起始和结束位置默认，步长为负数的话就相当于倒着输出

print(list1[7::-1])

print(list1[6::-2])

print(list1[6:0:-1])

# 仔细体会上述的输出
