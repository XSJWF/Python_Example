# 开发人员：DYL
# 开发时间：2022/6/16 15:07

# 元组是不可变对象，所以没有生成式

# 列表生成式
list1 = [i*i for i in range(6)]
print(list1)
list2 = [i for i in range(6)]
print(list2)

# 集合生成式
s = {i*i for i in range(10)}
print(s)

