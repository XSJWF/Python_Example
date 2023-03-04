# 开发人员：DYL
# 开发时间：2022/3/26 17:38

# 比较运算符

a, b = 10, 20
print(a > b)
print(a < b)
print(a == b)
print(a >= b)
print(a <= b)
print(a != b)
# 一个“=”是赋值运算符，两个“=”是比较运算符，比较的是“==”两边的值
# 用“is”来比较是否是同一对象（即地址是否相同）
a = 10
b = 10
print(a == b)
print(a is b)  # 返回值为True说明是同一对象，False则说明不是同一对象
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
print(list1 == list2)
print(list1 is list2)
print(id(list1), id(list2))
print(list1 is not list2)  # 判定两个列表不是同一个对象，返回值True/False
